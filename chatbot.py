import tweepy
import os

# Auth Variables
CONSUMER_KEY = os.environ.get('CONSUMER_KEY')
CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET')
KEY = os.environ.get('KEY')
SECRET = os.environ.get('SECRET')


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(KEY,SECRET)
api = tweepy.API(auth)
#Authenicaton
api.update_status("Hello Twitter Septeber 2020 Test 3!")
print("Request Submitted")