
class Writer:
    savefile = ''
    def setSaveFile(self, filename):
        #set it to encoding utf8 to prevent problems with special characters
        self.savefile = open(filename,'a', encoding='utf8')
        
    #Writes the tweet with the sentiment to a file, gets called each time data is obtained.
    def write(self,tweet):
        self.savefile.write(tweet + '\n')

