from Writer import Writer
import nltk
class SentimentChecker:
    writer = Writer('sentiments.txt')
    pos_words = ['good','best','awesome','amazing','epic','nice','happy','love','<3','true','right']
    neg_words = ['bad','worst','terrible','can\'t','bad','not','fuck','mean','hate','sad','false','wrong']
    neut_words = ['okay']
    sentiment = ''
    tokens = []

    def analyse_file(self,filename):
        for line in open(filename, 'r'):
             sentiment = self.analyse(line)
             sentiment = self.sentiment(sentiment)
             self.writer.write(sentiment+' '+line)
             
    def analyse(self, text):
        score = 0
        for w in text:
            if w in self.pos_words:
                score += 0.5
            if w in self.neg_words:
                score -= 0.4
        return score

    def sentiment(self, value):
        if value <= -0.5:
            return 'neg'
        elif value >= 0.5:
            return 'pos'
        else:
            return 'neut'
