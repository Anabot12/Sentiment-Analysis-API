from nltk.corpus import movie_reviews
from nltk.classify import NaiveBayesClassifier
from nltk.classify.util import accuracy as nltk_accuracy


def extract_features(words):
    return dict([(word, True) for word in words])


def SentimentAnalyzer(text):
    # load movie reviews from sample data
    f_pos = movie_reviews.fileids('pos')
    f_neg = movie_reviews.fileids('neg')
    f_neu =movie_reviews.fileids('nue')

    features_pos = [(extract_features(movie_reviews.words(fileids=[f])),'Positive') for f in f_pos]
    features_neg = [(extract_features(movie_reviews.words(fileids=[f])),'Negative') for f in f_neg]
    features_neu = [(extract_features(movie_reviews.words(fileids=[f])),'Neutral') for f in f_neu]

    threshold = 0.8
    num_pos = int(threshold*len(features_pos))
    num_neg = int(threshold*len(features_neg))
    num_neu = int(threshold*len(features_neu))

    # creating training and testing data
    features_train = features_pos[:num_pos] + features_neg[:num_neg] + features_neu[:num_neu]
    features_test = features_pos[num_pos:] + features_neg[num_neg:] + features_neu[:num_neu]


    # training a naive bayes classifier
    classifier = NaiveBayesClassifier.train(features_train)
    print('Accuracy:',nltk_accuracy(classifier, features_test))

    probabilities = classifier.prob_classify(extract_features(text.split()))
    # Pick the maximum value
    predicted_sentiment = probabilities.max()
    print("Predicted sentiment:", predicted_sentiment)
    print("Probability:",round(probabilities.prob(predicted_sentiment), 2))

    #return predicted_sentiment
    print(predicted_sentiment)
