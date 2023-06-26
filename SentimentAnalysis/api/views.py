from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework.response import Response
from rest_framework import status
from psycopg2._psycopg import connection

from django import generics
from chatbot.forms import SentimentForm

class PollList(generics.GenericAPIView):

	def post(self, request):
		data        = []
		language_id = int(1)
		tenant_info = SentimentForm(request)
		if tenant_info:
			tenant_id = request.session['tenant_id']
		member_id = int(self.request.data['member_id'])
		session_token = self.request.data['token']
		page = self.request.data['page']

		# Custom Inputs
		poll_status = self.request.data['poll_status']
		keyword = self.request.data['keyword']

		# Check member session
		check_session = function.checkMemberSession(member_id,tenant_id,session_token,language_id)
		if check_session=="ok":

			# Bulid WHERE condition form query inputs
			if poll_status =="all":
				poll_status_q   = ""
			elif poll_status == "active":
				poll_status_q   = " AND P.poll_status = 1 AND P.result_status = 1"
			elif poll_status == "pending":
				poll_status_q   = " AND P.poll_status = 1 AND P.result_status = 0"
			else:
				poll_status_q   = " AND P.poll_status = 0 "

			if keyword !="":
				sanitized_keyword = keyword.replace("'", "''").replace("\\", "\\\\")
				keyword_query = "AND P.question ILIKE '%%"+sanitized_keyword+"%%' "
			else:
				keyword_query = ""

			filter_query = poll_status_q+keyword_query

			with connection.cursor() as cursor:
				# Final Query
				query = """
					SELECT
						 P.id,P.question,P.end_timestamp,P.poll_status,P.has_deadline,P.has_credits,P.credit_value,P.result_type,P.result_timestamp,P.result_status,P.created_at,

						( SELECT COUNT(id)
                            FROM tenant_poll_answer_tbl
                            WHERE tenant_id = """+str(tenant_id)+""" AND poll_id= P.id
                        ) as total_votes,

						(SELECT poll_option_id
							FROM tenant_poll_answer_tbl
							WHERE tenant_id = """+str(tenant_id)+""" AND poll_id= P.id   AND member_id= """+str(member_id)+"""
						) as member_answer_option_id

					FROM tenant_polls_tbl P

					WHERE
						P.tenant_id = %s AND
						P.delete_status = 0
						"""+filter_query+"""
					ORDER BY {} {}


    	"""
				"""cursor.execute(query.format('id', 'DESC'), [tenant_id])
				#poll_list = dictfetchall(cursor)
				total_count = cursor.rowcount
				#current_time = utc_now(request)
				#for row in poll_list:
					#if row['has_deadline'] == 1:
						#deadline_date = utc_to_date_convertor(request,row['end_timestamp'])
						#deadline_days = get_utc_time_diff(row['end_timestamp'],current_time)
						#if current_time > row['end_timestamp']:
						overdue_alert = 1
						else:
							overdue_alert = 0
					else:
						deadline_date = ""
						deadline_days = ""
						overdue_alert = 0

					if row['has_credits'] == 1:
						credit_value = row['credit_value']
					else:
						credit_value = 0

					if row['result_type'] =="scheduled":
						result_date = utc_to_date_convertor(request,row['result_timestamp'])

					else:
						result_date =""

					if row['member_answer_option_id']!="" and row['member_answer_option_id'] != None:
						member_answer_option_id = row['member_answer_option_id']
					else:
						member_answer_option_id = 0

					if row['member_answer_option_id']:
						member_answered = 1
					else:
						member_answered = 0

					created_at = utc_to_date_convertor(request,row['created_at'])
					posted_on  =str(created_at['date_format_month'])

					# Get Poll options
					filter_items = {
					   	"tenant_id" : tenant_id,
						"poll_id" : row['id'],
						"member_id": member_id,
						"result_status" : row['result_status'],
						"total_votes" : row['total_votes']
					}
					#options_array = getPollOptions(filter_items)

					data.append({
						"id"                : row['id'],
						"question"          : row['question'],
						"has_deadline"      : row['has_deadline'],
						"deadline_date"     : deadline_date,
						"deadline_days"		: deadline_days,
						"overdue_alert"		: overdue_alert,
						"poll_status"       : row['poll_status'],
						#"option"            : options_array,
						"has_credits"       : row['has_credits'],
						"credit_value"      : credit_value,
						"result_type"       : row['result_type'],
						"result_date"       : result_date,
						"result_type"       : row['result_type'],
						"result_status"     : row['result_status'],
						"total_votes"		: row['total_votes'],
						"member_answer_option_id": member_answer_option_id,
						"member_answered" 	: member_answered,
						"posted_on"         : posted_on,
					})
"""
				paginator = Paginator(data, 5)
				try:
					data_list = list(paginator.page(page))
					items_per_page = len(list(data_list))
				except PageNotAnInteger:
					data_list = list(paginator.page(page))
					items_per_page = len(list(data_list))
				except EmptyPage:
					items_per_page = 0
					data_list = {
						#"message":get_translated_content(language_id, "e26"),
						"data": []
					}

			return Response({"status": "success", "message":"Poll Listed Successfully", "items_per_page":items_per_page, "data": data_list}, status=status.HTTP_200_OK)
		else:
			return Response({"status": "error", "message": check_session }, status=status.HTTP_400_BAD_REQUEST)
