import re

class SentimentAnalyzer():
    #local variables
    pos_words = ['good','best','awesome','amazing','epic','nice','happy','love','<3','true','right']
    neg_words = ['bad','worst','terrible','can\'t','bad','not','fuck','mean','hate','sad','false','wrong']
    neut_words = ['okay']
    sentiment_score = ''


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