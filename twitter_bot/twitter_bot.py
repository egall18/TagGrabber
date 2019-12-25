import tweepy
import time

consumer_key = 'bFl2WTFT9ZOk662iiyWo5qwHF'
consumer_secret = 'BLfjyxm8NXN83wjySiRFMVovi3KwbiUkyGrN9SdNEOufojZQOg'

key = '1183867130405507073-bsDFukh76MC1eq2C7Mj6uU2Jyk5YuJ'
secret = 'BaT8RHjfx7M11t0pOoc8NCvTg0QLwkC13lGDcNYp2uxkQ'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)#authentacation code to pass in the consumer key and consumer secret as parameters.
auth.set_access_token(key, secret)
api = tweepy.API(auth) #api is an aboject that will be used for other things such as like, comment, etc. This is a great way to read and write data from api.

# tweets = api.mentions_timeline() #Returns the 20 most recent mentions, including retweets.

FILE_NAME = 'last_seen.txt' #assign FILE_NAME to the text for easy reading purposes.

def read_last_seen(FILE_NAME): #funciton to read last seen text.
    file_read = open(FILE_NAME, 'r') #read the file info by opening it with the funciton open(filename, 'r'), r is for reading. Reading it into a string.
    last_seen_id = int(file_read.read().strip()) #strips any space.
    file_read.close() #closes the file being read which in this case is last_seen.txt
    return last_seen_id #return the last seen id info.

# id = read_last_seen(FILE_NAME) #testing purposes to check if last seen id does print
# print(id)
def store_last_seen(FILE_NAME, last_seen_id): #function that stores last seen id.
    file_write = open(FILE_NAME, 'w') #open file. File is being written to by using "w" which means write. file_write is an instance.
    file_write.write(str(last_seen_id)) #pass last_seen_id in the form of a string.
    file_write.close() #closes the file
    return #return nothing

def reply():
    tweets = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode = 'extended') #Returns the 20 most recent mentions, including retweets. If I pass in a particular id then I will only get the ids that are after that particular id.("1183996893572976645").
# store_last_seen_id(FILE_NAME, "1183996893572976666") #pass in the file and the id number.
    for tweet in reversed(tweets): #have access to each tweet individually
        if "#randomtweet" in tweet.full_text.lower(): #if this text is found in the text then it will print out the comment below and also the id and full text.
            # print("New Tweet Found!")
            print("Replied To ID - " + str(tweet.id)) #convert tweet id from int to string
            api.update_status("@" + tweet.user.screen_name + " Goodluck Kire Cruz! #randomtweet", tweet.id) #able to reply back to that particular tweet by using update_status
            api.create_favorite(tweet.id) #Favorites the status specified in the ID parameter as the authenticating user.
            api.retweet(tweet.id) #retweets the tweet of that particular id.
            store_last_seen(FILE_NAME, tweet.id) #able to store id and fetch last id

while True: #run infinitely as long as its true
    reply() #run the funciton reply which is going to get all tweets and reply to those tweets
    time.sleep(15) # wait for 2 seconds then the funciton will run again.

# print(tweets[0]) #able to grab first tweet since the type tweets is a list. 
# print(type(tweets)) #list type ResultSet

# api.update_status = ('Hey From Twitter Bot - Second Tweet!')
# print("Status Updated!")
