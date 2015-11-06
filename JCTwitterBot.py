# comments
import tweepy, time, sys
from TwitterBotKeys import keys
from datetime import datetime, timedelta
from random import randint
from os import listdir
from os.path import isfile, join
import os

class Twitbot:
	def __init__(self, keys):  
		CONSUMER_KEY = keys['consumer_key']
		CONSUMER_SECRET = keys['consumer_secret']
		ACCESS_TOKEN = keys['access_token']
		ACCESS_TOKEN_SECRET = keys['access_token_secret']
		auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
		#auth.secure = True
		auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
		self.api = tweepy.API(auth)
		user = self.api.me()
		print('Name: ' + user.name)
		print('Location: ' + user.location)
		print('Friends: ' + str(user.friends_count))
	
	def tweet(self, f):       
		for s in f:
			self.api.update_status(status = s)
			print(s)
			
	def updateStatusGIF(self):
		mypath = ".\gifs"
		onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
		for file in onlyfiles:
			relpath = mypath + "\\" + file
			statusGIF = os.path.abspath(relpath)
			print(statusGIF)
			self.api.update_with_media(filename=statusGIF, status="Smokin'!")

def getLines(filename):			
	argfile = str(filename)
	try:
		file = open(argfile, "r")
	except IOError:
		print("cannot open", argfile)
	f = file.readlines()
	file.close()
	return f
			
def main():
	JCBot = Twitbot(keys)
	f = getLines("liners.txt")
	#twitter.tweet(f)
	JCBot.updateStatusGIF()
	replyText = "Ace is on the case!"
	for tweet in JCBot.api.search(q="lost pet", count=1):
		sn = tweet.user.screen_name
		m = "@{0}, {1}".format(sn, replyText) 
		id = str(tweet.id)
		print(replyText)
		print(tweet.user.screen_name)
		print(id)
		x = JCBot.api.update_status(status=m, in_reply_to_status_id=id) 

#	replyText = "Laces out Dan!"
#	for tweet in api.search(q="Dolphin", count=1):
#		sn = tweet.user.screen_name
#		m = "@{0}, {1}".format(sn, replyText) 
#		print(replyText)
#		print(tweet.user.screen_name)
#		s = api.update_status(status=m, in_reply_to_status_id = tweet.id)
#	replyText = "I'm in psychoville, and Finkle's the mayor!"
#	for tweet in api.search(q="crazy", count=1):
#		sn = tweet.user.screen_name
#		m = "@{0}, {1}".format(sn, replyText) 
#		print(replyText)
#		print(tweet.user.screen_name)
#		s = api.update_status(status=m, in_reply_to_status_id = tweet.id)
	
if __name__ == "__main__": main() 