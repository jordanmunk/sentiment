import tweepy
from Tokens import Token
from SentimentAnalyzer import SentimentAnalyzer
from Writer import Writer
from Plotter import Plotter
from tweepy import Stream
from tweepy.streaming import StreamListener

class TweetObtainer(StreamListener):
    writer = ''
    sentimentAnalyzer = ''
    plot = ''
    tokens = ''

    def __init__(self, parameter):
        self.sentimentAnalyzer = SentimentAnalyzer()
        self.writer = Writer()
        self.plot = Plotter()
        print('Creating token')
        self.tokens = Token()

        #TwitterAPI authorization
        auth = tweepy.OAuthHandler(self.tokens.consumer_key, self.tokens.consumer_secret)
        auth.set_access_token(self.tokens.access_token, self.tokens.access_secret)
        stream = Stream(auth, self)
        stream.filter(track=[parameter], languages=['en'])

    def init_stream(self):
        self.writer.setSaveFile('StreamedTweets')

    def init_search(self):
        self.writer.setSaveFile('SearchedTweets')

    #Gets called everytime data is streamed through the Twitter API
    def on_data(self, data):
        tweet = self.sentimentAnalyzer.preprocess(data)
        print(tweet)
        sentiment = self.sentimentAnalyzer.analyse(tweet)
        self.writer.write(sentiment + tweet )
#       self.plotter.update()
    def on_error(self, status_code):
        print('Got an error with status code: ' + str(status_code))
        return True # To continue listening

    def on_timeout(self):
        print('Timeout...')
        return True # To continue listening