from django.shortcuts import render
from django.http import JsonResponse

from sentiment import SentimentAnalyzer
from .forms import SentimentForm
from chatbot.models import SentimentModel



def sentiment_ananya(request):
    form = SentimentForm(request.POST or None)
    context ={}
    if request.method == 'POST':
        if form.is_valid():
            sent = form.cleaned_data.get('comment')    # got the sentence
            textAns = SentimentAnalyzer(sent.split())
            context.append(textAns)

        else:
            form = SentimentForm()

    return JsonResponse(context)