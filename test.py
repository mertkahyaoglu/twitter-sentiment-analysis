# -*- coding: utf-8 -*-
import utils

username = 'cmylmz'
count = 1000

tweets = utils.cleanTweets(utils.getTweets(username, count))
positives, negatives = utils.analyseTweetsByEmoticons(tweets)

print "----- o -----* POSITIVES *----- o -----"
for item in positives:
	print item

print "----- o -----* NEGATIVES *----- o -----"
for item in negatives:
	print item

utils.export("cmylmz-tweets.txt", tweets)
utils.export("cmylmz-positives.txt", positives)
utils.export("cmylmz-negatives.txt", negatives)