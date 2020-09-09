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
    api.update_status("This is a demo of the schedular :)")
    print("Request Sent")

#Time
schedule.every().friday.at("18:30").do(job)
schedule.every().wednesday.at("18:30").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)