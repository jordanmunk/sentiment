import tweepy
from Tokens import consumer_key, consumer_secret, \
    access_secret, access_token
from SentimentAnalyzer import SentimentAnalyzer
from Writer import Writer
from tweepy import Stream
from tweepy.streaming import StreamListener
import json

class TweetObtainer(StreamListener):
    writer = None
    sentimentAnalyzer = None
    tokens = ''
    parameter = ''
    liveView = None
    pieView = None
    currentNumber = 0
    stream = None

    def __init__(self, parameter, liveView, pieView):
        self.sentimentAnalyzer = SentimentAnalyzer()
        self.writer = Writer()
        self.parameter = parameter
        print('Creating token')
        self.liveView = liveView
        self.pieView = pieView

    def init_stream(self):
        self.writer.setSaveFile('StreamedTweets.txt')

    def init_search(self):
        self.writer.setSaveFile('SearchedTweets.txt')

    def start(self):
        print("Setting up tweetobtainer")
        #TwitterAPI authorization
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_secret)
        self.stream = Stream(auth, self)
        self.stream.filter(track=[self.parameter], languages=['en'])

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
            self.pieView.update()
        return True

    def on_error(self, status_code):
        print('Got an error with status code: ' + str(status_code))
        return True # To continue listening

    def on_timeout(self):
        print('Timeout...')
        return True # To continue listening

    def stop_stream(self):
        self.stream.disconnect()