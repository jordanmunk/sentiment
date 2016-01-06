import re

def read_words(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = file.read().split("\n")
        print(data)
        return data


class SentimentAnalyzer():
    #local variables
    pos_words = []
    neg_words = []
    neut_words = []
    sentiment_score = ''
    def __init__(self):
        self.pos_words = read_words("PositiveWords.txt")
        self.neg_words = read_words("NegativeWords.txt")
        self.pos_words = read_words("NeutralWords.txt")

    def preprocess(self, text):
        #Encode to prevent writing issues..
        #text = text.encode('utf8','ignore')

        #Convert to lower case
        text = text.lower()
        #Convert www.* or http:// or https?://* to URL
        text = re.sub('((www\.[^\s]+)|(https?://[^\s]+)|(http://[^\s]+))','URL',text)
        #Convert @* to AT_USER
        text = re.sub('@[^\s]+','AT_USER',text)
        #Remove additional white spaces
        text = re.sub('[\s]+', ' ', text)
        #Replace #word with word
        text = re.sub(r'#([^\s]+)', r'\1', text)

        #trim
        text = text.strip('\'"')
        text = text.split()

        return text

    def analyse(self, processedText):
        score = 0
        #Compare words from the array of the tweet to the words used to identify the sentiment
        for w in processedText:
            if w in self.pos_words:
                score += 0.5
            if w in self.neg_words:
                score -= 0.4
        #Determine the sentiment
        if score <= -0.5:
            return 'neg'
        elif score >= 0.5:
            return 'pos'
        else:
            return 'neut'