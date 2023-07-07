import pandas as pd
from nltk.classify import NaiveBayesClassifier
from nltk.classify.util import accuracy as nltk_accuracy
from django.http import JsonResponse



def extract_features(words):
    return dict([(word, True) for word in words])




import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

def SentimentAnalyzer(comment):
    # Initialize the sentiment analyzer


    sid = SentimentIntensityAnalyzer()

    # Perform sentiment analysis on the comment
    sentiment_scores = sid.polarity_scores(comment)

    # Determine the sentiment label based on the compound score
    compound_score = sentiment_scores['compound']
    if compound_score >= 0.05:
        sentiment_label = 'Positive'
    elif compound_score <= -0.05:
        sentiment_label = 'Negative'
    else:
        sentiment_label = 'Neutral'

    


    return {'sentiment_label': sentiment_label, 'sentiment_scores': sentiment_scores}


'''
print("Sentiment Scores:")
print("  Positive: ", scores['pos'])
print("  Negative: ", scores['neg'])
print("  Neutral: ", scores['neu'])
print("  Compound: ", scores['compound'])

'''