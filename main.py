import tweepy
import config

from datetime import datetime, timedelta

screen_name = config.screenName
consumer_key = config.consumerKey
consumer_secret = config.consumerSecret
access_token = config.accessToken
access_token_secret = config.accessSecret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

timeline = api.user_timeline()
lastTweetId = timeline[0].id

mentions = api.mentions_timeline(since_id=lastTweetId)
for mention in mentions:
    try:
        if mention.text.startswith(screen_name):
            fourHoursLess = datetime.now() + timedelta(hours=-4)
            if(mention.created_at > fourHoursLess):
                api.retweet(mention.id)
                print mention.text
    except:
	    print 'Error'
