from config import config
from emoticons import emoticons
import tweepy
import json

# API Authentication
auth = tweepy.OAuthHandler(config['consumer_key'], config['consumer_secret'])
auth.set_access_token(config['access_token'], config['access_token_secret'])
api = tweepy.API(auth)

# Fetch tweets by username
def getTweets(username, count=10):
    timeline = api.user_timeline(username, count=count)
    tweets = [tweet.text.encode('utf-8') for tweet in timeline]
    return tweets

# Remove hashtags, mentions, links
def cleanTweets(tweets):
	clean_data = []
	for tweet in tweets:
	    item = ' '.join(word for word in tweet.split() \
	    	   if not word.startswith('#') and \
	    	   	  not word.startswith('@') and \
	    	   	  not word.startswith('http'))
	    if item == "" or item == "RT":
	        continue
	    clean_data.append(item)
	return clean_data

# Group tweets by emoticon score, positive or negative
def analyseTweetsByEmoticons(tweets):
	positives = []
	negatives = []
	for tweet in tweets:
		score = 0
		tokens = tweet.split()
		for token in tokens:
			if token in emoticons['positive']:
				score += 1
			if token in emoticons['negative']:	
				score -= 1
		if score > 0:
			positives.append(tweet)
		elif score < 0:
			negatives.append(tweet)
	return positives, negatives

# Export as json
def export(filename, data):
    with open(filename, "w") as output:
    	for line in data:
        	output.write(line+'\n')
