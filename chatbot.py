import tweepy
import schedule
import os
import time

def job():
    # Auth Variables
    CONSUMER_KEY = os.environ.get('CONSUMER_KEY')
    CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET')
    KEY = os.environ.get('KEY')
    SECRET = os.environ.get('SECRET')

    #Authenicaton
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(KEY,SECRET)
    api = tweepy.API(auth)
    #Make Post about event
    api.update_status("Hi! @Sebbiesuperior and @bpeppers1. Can y'all make it to D&D today? Its today at 7:00pm!")
    print("Request Sent")

#Time
schedule.every().friday.at("18:30").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)