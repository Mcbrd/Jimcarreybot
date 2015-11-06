# Comments go here.

import tweepy, time, sys
from TwitterBotKeys import keys
from datetime import datetime, timedelta
from random import randint

CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

argfile = str("liners.txt")

try:
	filename = open(argfile, "r")
except IOError:
	print("cannot open", argfile)
	
f = filename.readlines()
filename.close()

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

try:
	redirect_url = auth.get_authorization_url()
except tweepy.TweepError:
	print("Error! Failed to get request token.")
	
api = tweepy.API(auth)

user = api.me()
 
print('Name: ' + user.name)
print('Location: ' + user.location)
print('Friends: ' + str(user.friends_count))

replyText = "Ace is on the case!"
for tweet in api.search(q="lost pet", count=2):
	sn = tweet.user.screen_name
	m = "@{0}, {1}".format(sn, replyText) 
	print(replyText)
	print(tweet.user.screen_name)
	s = api.update_status(status=m, in_reply_to_status_id = tweet.id)