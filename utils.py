from config import config
from feelings import emoticons
from feelings import adjectives
import tweepy

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
	    	   	  not word.startswith('http') and \
	    		  not word.startswith('RT'))
	    if item == "" or item == "RT":
	        continue
	    clean_data.append(item)
	return clean_data

# Group tweets by emoticon score, positive or negative
def analyseTweets(tweets):
	positives = []
	negatives = []
	for tweet in tweets:
		if analyseByEmoticons(tweet) == 1:
			positives.append(tweet)
		elif analyseByEmoticons(tweet) == -1:
			negatives.append(tweet)
	return positives, negatives

def analyseByEmoticons(tweet):
	pos_emos = emoticons['positive']
	neg_emos = emoticons['negative']

	for pe in pos_emos:
		if pe in tweet:
			return 1
	for ne in neg_emos:
		if ne in tweet:
			return -1
	return 0

def export(filename, data):
    with open(filename, "w") as output:
    	for line in data:
        	output.write(line+'\n')
