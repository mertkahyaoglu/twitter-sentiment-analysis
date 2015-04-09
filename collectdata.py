# -*- coding: utf-8 -*-
import utils

usernames = ['cmylmz','sertaberener', 'DemetAkalin', 'hulyavsar', 'sertaberener', 'gulbenergen', 'MuratBoz', 'Niltakipte']

count = 3000

for username in usernames:
	tweets = utils.cleanTweets(utils.getTweets(username, count))
	utils.export("data/"+username+"-tweets.txt", tweets)
