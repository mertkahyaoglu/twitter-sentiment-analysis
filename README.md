# Determine Feelings on Twitter
The aim of the project is to determine how people are feeling when they share something on twitter. The program classifies only Turkish tweets.

> [Web application](https://tsa-webapp.herokuapp.com)
> Slides available at [slides.com](https://slides.com/mertkahyaoglu/twitter-sentiment-analysis)

##Requirements

1. [Twitter Developer Application](https://apps.twitter.com/app/new)
2. [Tweepy Python Library](http://www.tweepy.org/)
3. [NLTK](http://www.nltk.org/)

##Run

`python classify.py`

##Project Development Steps

* Fetch tweets for a specific user :white_check_mark:
* Clean data (remove hashtags and mentioned users) :white_check_mark:
* Detect positive and negative emoticons and adjectives in a tweet for training data :white_check_mark:
* Apply Naive Bayes Classifier algorithm :white_check_mark:
* Test results
