from django.shortcuts import render

from django.shortcuts import render
from django.http import JsonResponse

from sentiment import SentimentAnalyzer
from .forms import SentimentForm

def sentiment(request):
    form = SentimentForm(request.POST or None)
    context = {}
    if request.method == 'POST':
        if form.is_valid():
            sent = form.cleaned_data.get('Sentence')    # got the sentence
            textAns = SentimentAnalyzer(sent)
            context['text'] = textAns
        else:
            form = SentimentForm()

    return JsonResponse

