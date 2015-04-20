# coding=utf-8
from traindata import traindata
import nltk

def get_words_in_tweets(tweets):
    all_words = []
    for (words, sentiment) in tweets:
      all_words.extend(words)
    return all_words

def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    word_features = wordlist.keys()
    return word_features

word_features = get_word_features(get_words_in_tweets(traindata))

def extract_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features

training_set = nltk.classify.apply_features(extract_features, traindata)
classifier = nltk.NaiveBayesClassifier.train(training_set)

def classify(tweet):
	print classifier.classify(extract_features(tweet.split()))

tweet = 'çok iyi hissediyorum :D'
classify(tweet)
