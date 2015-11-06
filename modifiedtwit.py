import tweepy, time, sys, random
from random import randint
from replykeys import keys

class Twitbot(object):

    def __init__(self):
        self.argfile = str("liners.txt")
        
        
        #enter the corresponding information from your Twitter application:
        CONSUMER_KEY = keys['consumer_key']
        CONSUMER_SECRET = keys['consumer_secret']
        ACCESS_KEY = keys['access_token']
        ACCESS_SECRET = keys['access_token_secret']
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.secure = True
        auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
        self.api = tweepy.API(auth)

    def tweet(self):
        argfile = str("liners.txt")
        filename=open(argfile,'r')
        f=filename.readlines()
        filename.close()
        
        
        for enter in f:
            self.api.update_status(status = enter)
        
twitter = Twitbot()
twitter.tweet()