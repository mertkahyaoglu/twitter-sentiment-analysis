# -*- coding: utf-8 -*-
import utils
import os
import nltk

positives, negatives, neutrals = [], [], []
for filename in os.listdir("data"):
    if filename.endswith(".txt"):
	    with open('data/'+filename) as f:
		    tweets = [tweet for tweet in f.readlines()]
            pos, neg, neut = utils.groupTweets(tweets)
            
            for p in pos:
            	positives.append((p, 'positive'))
            for n in neg:
            	negatives.append((n, 'negative'))
            for ne in neut:
                neutrals.append((ne, 'neutral'))

traindata = []
for (words, sentiment) in positives + negatives + neutrals:
    words_filtered = [e for e in words.split() if len(e) > 2]
    traindata.append((words_filtered, sentiment))
