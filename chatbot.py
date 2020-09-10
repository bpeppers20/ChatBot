import tweepy
import schedule
import os
import time


#Send Status Post to twitter dev account
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
    api.update_status("This is a demo of the scheduler :)")
    print("Request Sent")


#Functions to run on select day and time for that day
def selectSunday():
    schedule.every().sunday.at(timer).do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)

def selectMonday():
    schedule.every().monday.at(timer).do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)


def selectTuesday():
    schedule.every().tuesday.at(timer).do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)

def selectWednesday():
    schedule.every().wednesday.at(timer).do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)

def selectThursday():
    schedule.every().thursday.at(timer).do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)

def selectFriday():
    schedule.every().friday.at(timer).do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)

def selectSaturday():
    schedule.every().saturday.at(timer).do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)

def startSchedule(case):
    switch = {
        0: selectSunday,
        1: selectMonday,
        2: selectTuesday,
        3: selectWednesday,
        4: selectThursday,
        5: selectFriday,
        6: selectSaturday
    }
    func = switch.get(case, lambda : 'Day not valid or format')
    return func() #return the function of the selected day

day = int(input("Enter the day you wish the post to be released. 0 = sun, 1 = mon, 2 = tues, etc...\n"))

timer = str(input("Enter the time you want the post to be released. Needs to be in military time\n")) #Should be string for day function a("")

startSchedule(day)