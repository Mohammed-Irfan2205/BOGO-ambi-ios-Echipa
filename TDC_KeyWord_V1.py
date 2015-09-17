#!/usr/bin/env python

"""

Use Twitter API to grab user information from list of organizations; 
export text file

Uses Twython module to access Twitter API

"""

import sys
import string
import simplejson
from twython import Twython
import time

# Library to use Mongo DB
import pymongo
from pymongo import MongoClient

#WE WILL USE THE VARIABLES DAY, MONTH, AND YEAR FOR OUR OUTPUT FILE NAME
import datetime
now = datetime.datetime.now()
day=int(now.day)
month=int(now.month)
year=int(now.year)


#FOR OAUTH AUTHENTICATION -- NEEDED TO ACCESS THE TWITTER API
t = Twython(app_key='Aj75DDCB608ERaHyMiWj8xV7t', #REPLACE 'APP_KEY' WITH YOUR APP KEY, ETC., IN THE NEXT 4 LINES
    app_secret='pT4w1VJPORy0RlEVx45AWvc8RNmwOsJnIYyzDFPGIysKcRer40',
    oauth_token='1687216410-lLpY8pQjialj94OL3Hsm9h7hXpl16IdmLhsOOGc',
    oauth_token_secret='WXWCt23WpgM8quShFLPL35lBMteu4uxj4k1ogYEcimbOh')
	
#Connecting to Mongo DB
client = MongoClient('localhost',27017)
db = client['NEWSdata']
Tweets = db.TKD
   
#REPLACE WITH YOUR LIST OF TWITTER KEYWORDS
	
keywordList= ["@BJP4India","@Bihar_BJP","@NitishForBihar","#BiharPolls","Bihar BJP","Bihar Polls","#BiharElections","#Bihar Elections","Nitish","#NitishKumar","#BJP","#Congress","#LJP","#RJD","LJP","RJD","Bihar","Bharatiya Jan Congress","Bihar People's Party","Bihar Vikas Party","Kisan Vikas Party","Krantikari Samyavadi Party","Rashtrawadi Kisan Sanghatan","Rashtriya Janata Dal (Democratic)","Samajwadi Krantikari Sena","Sampurna Vikas Dal","#bihar","#bihar assembly elections 2015","#congress","#JD(U)","ModiInsultsIndia","#ModiFailsTest"]# List of keywords for which twitter data has to be collected.
j = 1
for i in range(0,120):
	print i
	for id in keywordList:
		try:
			data = t.search(q=id,count=100,result_type='recent',lang='en',max_id=None)
			for elements in data:
				#search_metadata = data['search_metadata'] # Metadata is not required as of now.
				statuses = data["statuses"]
				try:
					j = j + 1
					for item in statuses:
						Tweets.insert(item)
				except:
					print "Duplicate Number = %i" % (j)
					j = j + 1
					continue
		except:
			time.sleep(900)
			continue