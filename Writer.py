#Used to write to file. Variable filename so it could be reused
class Writer:
    savefile = ''
    def __init__(self, filename):
        self.savefile = open(filename,'a', encoding='utf8')
        
    #Writes the tweet with the sentiment to a file.
    def write(self,tweet):
        self.savefile.write(tweet)

