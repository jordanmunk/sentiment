from tkinter import *
from Stream import MyStreamer
from WordSearcher import Searcher
from Sentiment import SentimentChecker

if __name__ == '__main__':
    root = Tk()
    myLabel = Label(root, text="Anton's Bad Sentiment Analyzer (ABSA)")
    myLabel.pack(fill=X)

    topFrame = Frame(root)
    topFrame.pack()
    botFrame = Frame(root)
    botFrame.pack(side=BOTTOM)

    entry1 = Entry(topFrame)
    entry1.pack()

    button1 = Button(topFrame, text="Start Stream")
    button2 = Button(topFrame, text="Toon analyse")
    button3 = Button(botFrame, text="About")
    button1.pack(side=LEFT)
    button2.pack(side=LEFT)
    button3.pack()
    root.mainloop()


    #
    # choice = input("Wil je streamen of analyzeren?")
    # if choice.startswith("stream"):
    #     stream = MyStreamer()
    #     stream.start()
    # if choice.startswith("analyze"):
    #     sentimentChecker = SentimentChecker()
    #     sentimentChecker.analyse_file('tweets.txt')
