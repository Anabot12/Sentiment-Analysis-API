from django.shortcuts import render
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
from psycopg2._psycopg import connection
from django.db import models
from rest_framework import generics
from chatbot.forms import SentimentForm
from chatbot.views import sentiment_ananya
from sentiment import SentimentAnalyzer

class ListAPI(generics.GenericAPIView):
    def post(self, request):
        comment_text = request.data.get('comment')

        if not comment_text:
            return Response({"status": "error", "message": "No comment provided"}, status=status.HTTP_400_BAD_REQUEST)

        sentiment = SentimentAnalyzer(comment_text)

        data = {
            'comment': comment_text,
            'sentiment': sentiment
        }

        return Response({"status": "success", "data": data}, status=status.HTTP_200_OK)