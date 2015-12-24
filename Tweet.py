import re

class TweetPreprocessor:
    text = 'No text..'
    split_text = []
    def __init__(self, text):
        self.text = text

    def parse_json(self):
        self.text = self.text['text']
        self.text.encode('utf8','ignore')

# process the tweets
    def preprocess(self):
        tweet = self.text
        #Convert to lower case
        tweet = tweet.lower()
        #Convert www.* or http:// or https?://* to URL
        tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+)|(http://[^\s]+))','URL',tweet)
        #Convert @* to AT_USER
        tweet = re.sub('@[^\s]+','AT_USER',tweet)
        #Remove additional white spaces
        tweet = re.sub('[\s]+', ' ', tweet)
        #Replace #word with word
        tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
        #Remove smileys
        #tweet = re.sub('(\u[^\s]+)','Smiley',tweet)
        #trim
        tweet = tweet.strip('\'"')
        self.text = tweet
        return self.text

    def get_split_text(self):
        return self.split_text

    def get_text(self):
        return self.text
