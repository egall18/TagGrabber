import tweepy
import time

consumer_key = 'bFl2WTFT9ZOk662iiyWo5qwHF'
consumer_secret = 'BLfjyxm8NXN83wjySiRFMVovi3KwbiUkyGrN9SdNEOufojZQOg'

key = '1183867130405507073-bsDFukh76MC1eq2C7Mj6uU2Jyk5YuJ'
secret = 'BaT8RHjfx7M11t0pOoc8NCvTg0QLwkC13lGDcNYp2uxkQ'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)#authentacation code to pass in the consumer key and consumer secret as parameters.
auth.set_access_token(key, secret)
api = tweepy.API(auth) #api is an aboject that will be used for other things such as like, comment, etc. This is a great way to read and write data from api.

hashtag = ("RandomTweet", "python") #combination of hashtag to use (tuple)
tweetNumber = 10 #number of tweets we need to retweet and like

tweets = tweepy.Cursor(api.search, hashtag).items(tweetNumber) #Looks for anything with a #christmas and how many tweets I nedd to fetch of that hashtag.
#instead of items.(tweetNumber) and we use pages.(tweetNumber) then we would be retweeting 200 tweets for 10 pages.

def searchbot(): #funciton used to retweet that particular hashtag. 
    for tweet in tweets:
        try: #try and except error is a great way to avoid errors while trying to run the function.
            tweet.retweet() #this will run the function retweet to retweet the comment of the hashtag.
            print("Retweet Done!")
            time.sleep(2) #wait for 2 seconds and then the function will run again
        except tweepy.TweepError as e: #if already retweeted then this will run.
            print(e.reason)
            time.sleep(2)

searchbot() #calling the function to run
