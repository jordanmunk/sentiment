from Stream import MyStreamer
from Sentiment import SentimentChecker

if __name__ == '__main__':
    choice = input("Wil je streamen of analyzeren?")
    if choice.startswith("stream"):
        stream = MyStreamer()
        stream.start()
    if choice.startswith("analyze"):
        sentimentChecker = SentimentChecker()
        sentimentChecker.analyse_file('tweets.txt')
