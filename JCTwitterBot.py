# Team Cupcake - Brad McManus, Chad Hilke, and Ryan Barby

import tweepy, time, sys
from TwitterBotKeys import keys
from datetime import datetime, timedelta
import random
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
		auth.secure = True
		auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
		self.api = tweepy.API(auth)
		user = self.api.me()
		print("Name: " + user.name)
		print("Location: " + user.location)
		print("Friends: " + str(user.friends_count))
		print("-----------------------------------")
			
	def updateStatusGIF(self, quotes):
		quote = random.choice(quotes)
		if len(quote) > 140:
			quote = "Alrighty then!"
		print(quote)
		mypath = ".\gifs"
		onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
		pick = random.choice(onlyfiles)
		print(pick)
		relpath = mypath + "\\" + pick
		statusGIF = os.path.abspath(relpath)
		size = os.path.getsize(statusGIF)
		if int((size/1000)) > 3072:
			statusGIF = r"C:\\Users\chilke\Documents\Git\Jimcarreybot\gifs\Ace2.gif"
		self.api.update_with_media(filename=statusGIF, status=quote)

	def retweet(self):
		JCBot = Twitbot(keys)		
		for tweet in JCBot.api.search(q="prize retweet", count=1):
			self.api.retweet(id=(tweet.id))
			id = str(tweet.id)
			print(id)
			
	def trollUser(self, query, replyText):
		for tweet in self.api.search(q=query, count=1):
			sn = tweet.user.screen_name
			m = "@{0}, {1}".format(sn, replyText) 
			id = str(tweet.id)
			print(replyText)
			print(tweet.user.screen_name)
			print(id)
			troll = self.api.update_status(status=m, in_reply_to_status_id=id)

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
	while True:
		JCBot = Twitbot(keys)
		quotes = getLines("liners.txt")		
		JCBot.updateStatusGIF(quotes) #update our status
		TimeToSleep = randint(120,360) 
		time.sleep(TimeToSleep) #wait 2-4 minutes to troll first user
		JCBot.retweet()
		TimeToSleep = randint(120,360) 
		time.sleep(TimeToSleep) #wait 2-4 minutes to troll first user
		replyText = "Ace is on the case!"
		query = "lost pet"
		JCBot.trollUser(query, replyText)
		TimeToSleep = randint(120,360)
		time.sleep(TimeToSleep) #wait 2-4 minutes to troll next user
		replyText = "Laces out Dan!"
		query = "Dolphin"
		JCBot.trollUser(query, replyText)
		TimeToSleep = randint(120,360)
		time.sleep(TimeToSleep) #wait 2-4 minutes to troll next user
		replyText = "I'm in psychoville, and Finkle's the mayor!"
		query = "crazy"
		JCBot.trollUser(query, replyText)
		TimeToSleep = randint(900,1200) 
		time.sleep(TimeToSleep) #wait 10-20 minutes, then update status again
	
if __name__ == "__main__": main() 
