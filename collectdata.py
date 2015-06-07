# -*- coding: utf-8 -*-
import utils

usernames = ['sertaberener', 'DemetAkalin', 'hulyavsar', 'sertaberener', 'gulbenergen', 'MuratBoz', 'Niltakipte']

count = 200

for username in usernames:
	tweets = utils.cleanTweets(utils.getTweets(username, count))
	utils.export("data/"+username+"-tweets.txt", tweets, "w")
