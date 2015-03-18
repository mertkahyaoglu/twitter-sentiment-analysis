# Determine Feelings on Twitter

> Category: Sentiment Analysis

##Existing Technologies

[Stanford University NLP Project](http://nlp.stanford.edu/courses/cs224n/2009/fp/22.pdf)
The project considers tweets or status updates of [Twitter](https://twitter.com/) users. Based on the information contained in a tweet, program can answer the following question: does the author of the tweet feel happy, sad or neither about a particular word of her tweet. 
The project uses Python for parsing, MATLAB for analysis and SQLite database for storing the result of twitter keyword searches.

##Proposal

The aim of the project is to determine how people are feeling when they share something on twitter by analysing their tweets. I’m going to use [Twitter API](https://dev.twitter.com/rest/public) for collecting data for a certain user. Then I’m going to try to extract some information from that data by using simple and effective techniques.
For example, "Today is a perfect day!" sentence determines that the author feels happy and excited.

##Steps

* Create a [Twitter Developer Application](https://apps.twitter.com/app/new) to be able use developer API. (Authentication) :white_check_mark:
* Setup Twitter API library [Tweepy](http://www.tweepy.org/) :white_check_mark:
* Fetch tweets for a specific user using [Tweepy](http://www.tweepy.org/) :white_check_mark:
* Clean data
* First Solution: Process data programmatically for extracting emotions
* Second Solution: Train data and create a model for [openNLP](https://opennlp.apache.org/)
* Test results
