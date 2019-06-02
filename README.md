# Determine Feelings on Twitter
The aim of the project is to determine how people are feeling when they share something on Twitter. The program classifies only Turkish tweets.

> Check out NodeJS web application [here](https://twitter-sentiment-analysis.now.sh/)

> Slides - [NLTK version](https://slides.com/mertkahyaoglu/twitter-sentiment-analysis), [Weka version ](http://slides.com/mertkahyaoglu/twitter-sentiment-analysis-4)

##Requirements

1. [Twitter Developer Application](https://apps.twitter.com/app/new)
2. [Tweepy Python Library](http://www.tweepy.org/)
3. [NLTK](http://www.nltk.org/)

##Run

`python classify.py`

##Project Development Steps

* Fetch tweets for a specific user :white_check_mark:
* Clean data (remove hashtags and mentioned users) :white_check_mark:
* Label positive and negative tweets :white_check_mark:
* Apply Naive Bayes Classifier algorithm :white_check_mark:
* Test results :white_check_mark:
