import tweepy
import json
import time
from Tokens import Token
from Sentiment import SentimentChecker
from Tweet import TweetPreprocessor
from Writer import Writer
from tweepy import Stream
from tweepy.streaming import StreamListener

#Class used to receive the stream from twitter API
class StdOutListener(StreamListener):
    my_sentiment_checker = SentimentChecker()
    writer = Writer('tweets.txt')
    def __init__(self, sentiment_checker):
        self.sentiment_checker = sentiment_checker
    
    #Gets called everytime data is streamed through the Twitter API
    def on_data(self, data):
        new_tweet = TweetPreprocessor(json.loads(data))
        new_tweet.parse_json()
        processed_tweet = new_tweet.preprocess()
        print(processed_tweet)
        self.writer.write(processed_tweet+'\n')
        self.my_sentiment_checker.analyse(processed_tweet)

    def on_error(self, status_code):
        print('Got an error with status code: ' + str(status_code))
        return True # To continue listening

    def on_timeout(self):
        print('Timeout...')
        return True # To continue listening

class MyStreamer():
#Main class, starts the app
    def start(self):
        print('Creating token')
        token = Token()

        #TwitterAPI authorization
        auth = tweepy.OAuthHandler(token.consumer_key, token.consumer_secret)
        auth.set_access_token(token.access_token, token.access_secret)
        api = tweepy.API(auth)

        #My sentiment checker
        my_sentiment_checker = SentimentChecker()

        #Stream listener
        print("Creating listener . . .")
        listener = StdOutListener(my_sentiment_checker)
        word = input("What do you want to stream for ? ")
        print("Starting stream . . .")
        stream = Stream(auth, listener)
        stream.filter(track=[word], languages=['en'])


