# -*- coding: utf-8 -*-
import utils
import os
import nltk

positives, negatives = [], []
for filename in os.listdir("data"):
    if filename.endswith(".txt"):
	    with open('data/'+filename) as f:
		    tweets = [tweet for tweet in f.readlines()]
            pos, neg = utils.groupTweets(tweets)

            utils.export("train/positives.txt", pos, "a")
            utils.export("train/negatives.txt", neg, "a")
