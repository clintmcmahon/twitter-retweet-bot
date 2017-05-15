## A Python based Twitter retweet bot.

A crowd-sourced Twitter retweet service that retweets people's tweets in real-time as they can create a single crowd sourced Twitter account.

## Synopsis

This is a Python based script to retweet tweets, mentions in this case, that are sent to a specific Twitter account. When a Twitter user sends a mention that starts with the specific Twitter account name, that tweet will be retweeted. 

Example:
If I tweet at the Twitter account @TamaleTracker "@tamaletracker Red cooler at the Green Eye!" the @TamaleTracker Twitter account retweets the tweet. Only tweets that start with the account user name will be retweeted. 

View live example of this in action at [@TamaleTracker](http://twitter.com/tamaletracker).

## Code Example/Configuration

You'll need to set up a Twitter developer account for the Twitter account to be retweeted. After you set up a dev account at https://dev.twitter.com/ you set the config values as neccessary.

screenName = "@your_twitter_account"

consumerKey = "consumerKey"

consumerSecret = "consumerSecret"

accessToken = "accessToken"

accessSecret = "accessSecret"

## Motivation

This is the generic version of the original project for a crowd-sourced Twitter retweet service that retweets people's tweets in real-time as they see the tamale guys selling tamales around the bars in Chicago. This as a personal project I developed so my friends and I could find where the tamale guys where at any given point during the night. 

The service is hooked into the Twitter streaming API so whenever someone tweets at the Tamale Tracker user describing where the tamale guys are, the account retweets that tweet through itself. Thus creating a single datasource for followers to recieve real-time updates.

This code is set up so that anyone who wants to have the same type of Twitter retweet bot can do the same with this code.

## Installation

To run the code just clone this repo, set the config.py parameters and run "python tamaletracker.py"

## License

Do whatcha wanna
