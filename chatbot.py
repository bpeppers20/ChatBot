import tweepy
#Authenicaton
consumer_key = '4ky21bmQvioRcpu7kBgXe54ew'
consumer_secret = 'C7aAUqeO2I1qb25aNK9CgZ245bvJcTrP5DaWUZFpz2gC6VxSPP'

key = '1286112733340020738-Vxj95fv3ji9wQ5iKwvdsNED98xEm8k'
secret = 'NEfkgdzvxBtrGTDScvSOv0xCUu6sr7Gvmx6H1YiO56Ofi'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key,secret)

api = tweepy.API(auth)
#Authenicaton
api.update_status("Boop")
