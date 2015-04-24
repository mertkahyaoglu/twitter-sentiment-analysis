# -*- coding: utf-8 -*-
from config import config
from feelings import emoticons
from feelings import text_emoticons
from feelings import adjectives
import tweepy
import os

# API Authentication
auth = tweepy.OAuthHandler(config['consumer_key'], config['consumer_secret'])
auth.set_access_token(config['access_token'], config['access_token_secret'])
api = tweepy.API(auth)

# Fetch tweets by username
def getTweets(username, count=10):
    timeline = api.user_timeline(username, count=count)
    tweets = [tweet.text.encode('utf-8').translate(None, '!.,?') for tweet in timeline]
    return tweets

# Remove hashtags, mentions, links
def cleanTweets(tweets):
	clean_data = []
	for tweet in tweets:
	    item = ' '.join(word.lower() for word in tweet.split() \
	    	if not word.startswith('#') and \
	    	   not word.startswith('@') and \
	    	   not word.startswith('http') and \
	    	   not word.startswith('RT'))
	    if item == "" or item == "RT":
	        continue
	    clean_data.append(item)
	return clean_data

def groupTweets(tweets):
	positives, negatives = [], []

	for tweet in tweets:
		score = classify(tweet)
		if score > 0:
			positives.append(tweet)
		elif score < 0:
			negatives.append(tweet)
	return positives, negatives

#rule-based
def classify(tweet):
	pos_emos = emoticons['positive']
	neg_emos = emoticons['negative']
	pos_temos = text_emoticons['positive']
	neg_temos = text_emoticons['negative']
	pos_adj = adjectives['positive']
	neg_adj = adjectives['negative']

	score = 0
	tokens = tweet.split()
	#emoticon check
	for pe in pos_emos:
		if pe in tweet:
			score += 5
	for ne in neg_emos:
		if ne in tweet:
			score -= 5

	#text_emoticon check
	for token in tokens:
		for pte in pos_temos:
			if pte in token:
				score += 5
		for nte in neg_temos:
			if nte in token:
				score -= 5

	#check adjectives
	for token in tokens:
		for pa in pos_adj:
			if pa in token:
				score += 5
		for na in neg_adj:
			if na in token:
				score -= 5
	return score

def getTrainData():
	positives, negatives, traindata = [], [], []
	for filename in os.listdir("train"):
	    if filename == "positives.txt":
		    with open('train/'+filename) as f:
			    positives = [(tweet, 'positive') for tweet in f.readlines()]
	    if filename == "negatives.txt":
		    with open('train/'+filename) as f:
			    negatives = [(tweet, 'negative') for tweet in f.readlines()]

	for (words, sentiment) in positives + negatives:
		words_filtered = [e for e in words.split() if len(e) > 2]
		traindata.append((words_filtered, sentiment))

	return traindata

def export(filename, data, p):
    with open(filename, p) as output:
    	for line in data:
        	output.write(line)
