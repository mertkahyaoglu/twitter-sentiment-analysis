# -*- coding: utf-8 -*-
from __future__ import print_function
import utils
import os

for filename in os.listdir("data"):
    if filename.endswith(".txt"):
	    with open('data/'+filename) as f:
		    tweets = [tweet for tweet in f.readlines()]
		    clean_tweets = utils.cleanTweets(tweets)
		    filename = os.path.splitext(filename)[0]
		    utils.export("data/"+filename+"-clean.txt", tweets)

# group by emoticon analyses
