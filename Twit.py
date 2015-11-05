
import tweepy, time, sys, random
from random import randint
 
argfile = str("liners.txt")
 

 
#enter the corresponding information from your Twitter application:
CONSUMER_KEY =  'key'#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = 'key'#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = 'key'#keep the quotes, replace this with your access token
ACCESS_SECRET = 'key'#keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
 
filename=open(argfile,'r')
f=filename.readlines()
filename.close()
 
while True:
    for line in f:
        curtime= time.strftime("%H:%M:%S")
        curdate= time.strftime("%x")
        api.update_status("{0}---{1}, {2}".format(curdate,curtime,line)) 
        TimeToSleep = randint(780,1200)
        time.sleep(TimeToSleep)#Tweet every 15 minutes