import tweepy
import json
import time
from Tokens import Token
from Sentiment import SentimentChecker
from Tweet import TweetPreprocessor
from Writer import Writer

#Class used to receive the stream from twitter API
class Searcher():
    #My file writer
    writer = Writer('twots.txt')

    #My sentiment checker
    sentiment_checker = SentimentChecker()

    def search(self, api,  keyword, language, amount):
        results = api.search(q=keyword, lang=language, count = int(amount) )
        return results

    def write_results(self, results):
        for result in results:
            new_tweet = TweetPreprocessor(result.text)
            processed_tweet = new_tweet.preprocess()
            print(processed_tweet)
            self.writer.write(processed_tweet)


    def start(self):
        print('Creating token')
        token = Token()

        #Stream listener
        print("Creating listener . . .")
        searcher = Searcher()

        #TwitterAPI authorization
        auth = tweepy.OAuthHandler(token.consumer_key, token.consumer_secret)
        auth.set_access_token(token.access_token, token.access_secret)
        api = tweepy.API(auth)

        keyword = input("What word do you want to search for?")
        language = input("In what language do you want to search ?")
        amount = input("How many results do you want ?")
        print("Starting search")
        results = searcher.search(api, keyword,language, amount)
        searcher.write_results(results)
