 # -*- coding: utf-8 -*-

import tweepy,random,time
#from our keys module (keys.py), import the keys dictionary
from replykeys import keys
from datetime import datetime,timedelta
from random import randint
 
 
CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']
argfile = str("liners.txt")
 
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
 

while True:
    
    trends1 = api.trends_place(2379574) #WOE id for Chicago
    hashtags = [x['name'] for x in trends1[0]['trends'] if x['name'].startswith('#')]

    trend_hashtag = hashtags[0]

    tweetSearchResults = api.search(q=trend_hashtag,count=50)     
    #list of specific strings we want to check for in Tweets
    filename=open(argfile,'r')
    f=filename.readlines()
    filename.close()
	
    
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
 
 
    for tweet in tweetSearchResults:
		#print tweet
		#print '\r\n'
		sn = tweet.user.screen_name
		message = f[randint(0,len(f)-1)] 
		m = "@{0}, {1} {2}".format(sn, message,trend_hashtag) 
		print m
		#print '\r\n'
		s = api.update_status(status=m, in_reply_to_status_id = tweet.id)
		
		TimeToSleep = randint(120,360)
		time.sleep(TimeToSleep)#Tweet every 2-4 minutes
    
	
    TimeToSleep = randint(3600,4000)#wait 10-20 minutes to look for a new topic
    time.sleep(TimeToSleep)#Tweet every 15 minutes
	