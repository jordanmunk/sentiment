import tweepy
from Tokens import consumer_key, consumer_secret, access_secret, access_token
from SentimentAnalyzer import SentimentAnalyzer
from Writer import Writer
from tweepy import Stream
from tweepy.streaming import StreamListener
from Screens import *
import json

class TweetObtainer(StreamListener):
    writer = ''
    sentimentAnalyzer = ''
    tokens = ''
    parameter = ''
    liveView = ''
    currentNumber = 0

    def __init__(self, parameter, liveView):
        self.sentimentAnalyzer = SentimentAnalyzer()
        self.writer = Writer()
        self.parameter = parameter
        print('Creating token')
        self.liveView = liveView

    def init_stream(self):
        self.writer.setSaveFile('StreamedTweets.txt')

    def init_search(self):
        self.writer.setSaveFile('SearchedTweets.txt')

    def start(self):
        print("Setting up tweetobtainer")
        #TwitterAPI authorization
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_secret)
        stream = Stream(auth, self)
        stream.filter(track=[self.parameter], languages=['en'])

    #Gets called everytime data is streamed through the Twitter API
    def on_data(self, data):
        text = json.loads(data)

        #Use only the text field of obtained JSON String
        if 'text' in text:
            text = text['text']
            tweet = self.sentimentAnalyzer.preprocess(text)
            print(tweet)
            sentiment = self.sentimentAnalyzer.analyse(tweet)
            if self.currentNumber <= 10000:
                self.writer.write(sentiment + text)
                self.currentNumber += 1
            self.liveView.update(sentiment)
        return True

    def on_error(self, status_code):
        print('Got an error with status code: ' + str(status_code))
        return True # To continue listening

    def on_timeout(self):
        print('Timeout...')
        return True # To continue listening