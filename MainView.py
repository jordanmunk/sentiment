from tkinter import *
import threading

class MainView():
    mainController = ''
    def __init__(self, controller):
        self.mainController = controller
        self.setup_gui()


    def setup_gui(self):
        print("Setup gui")
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
        button1.config(command = lambda: self.mainController.start_stream(entry1.get()) )
        button2 = Button(topFrame, text="Toon analyse")
        button3 = Button(botFrame, text="About")
        button1.pack(side=LEFT)
        button2.pack(side=LEFT)
        button3.pack()
        root.mainloop()

    def printbby(self):
        print("bby")