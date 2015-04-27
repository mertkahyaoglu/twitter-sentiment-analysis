# Determine Feelings on Twitter

> Category: Sentiment Analysis

##Requirements

1. [Twitter Developer Application](https://apps.twitter.com/app/new)
2. [Tweepy Python Library](http://www.tweepy.org/)
3. [NLTK](http://www.nltk.org/)

##Proposal

The aim of the project is to determine how people are feeling when they share something on twitter by analysing their tweets. I’m going to use [Twitter API](https://dev.twitter.com/rest/public) for collecting data for a certain user. Then I’m going to try to extract some information from that data by using simple and effective techniques.
For example, "Today is a perfect day!" sentence determines that the author feels happy and excited.

##Steps

* Fetch tweets for a specific user :white_check_mark:
* Clean data (remove hashtags and mentioned users) :white_check_mark:
* Detect positive and negative emoticons in a tweet and give them score accordingly :white_check_mark:
* Train data according to the score :white_check_mark:
* Apply Naive Bayes Classifier algorithm :white_check_mark:
* Test results
