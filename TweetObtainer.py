'''
Author: Anton Steenvoorden
Is verantwoordelijk voor het ophalen van de tweets, en het verwerken ervan.
Ontvangt een live view en een pie chart view en een woord waarop gezocht
moet worden. Maakt gebruik van tweepy, en haalt de twitter API sleutels op
uit mijn Tokens.py
'''
import tweepy
from Tokens import consumer_key, consumer_secret, \
    access_secret, access_token
from SentimentAnalyzer import SentimentAnalyzer
from Writer import Writer
from tweepy import Stream
from tweepy.streaming import StreamListener
import json
import time
'''
Erft over van Tweepy's StreamListener
'''
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

    def start(self):
        print("Setting up tweetobtainer")
        #TwitterAPI authorization
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_secret)
        self.stream = Stream(auth, self)
        self.stream.filter(track=[self.parameter], languages=['en'])

    '''
    Wordt elke keer als er een tweet binnenkomt aangeroepen
    Stuurt de opgehaalde tweet door naar de analyse en schrijft de
    analyse+tweet weg in een bestand als er minder dan 10.000 zijn
    opgehaald deze sessie. Slaapt voor 1 seconde zodat er genoeg tijd is om
    de tweet te verwerken.
    '''
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
            time.sleep(1)
        return True

    def on_error(self, status_code):
        print('Got an error with status code: ' + str(status_code))
        return True # To continue listening

    def on_timeout(self):
        print('Timeout...')
        return True # To continue listening

    def stop_stream(self):
        self.stream.disconnect()