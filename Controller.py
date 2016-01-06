from TweetObtainer import TweetObtainer
import threading

class Controller():
    mainView =''
    tweetObtainer = None

    def __init__(self):
        print("Controller created")

    def setView(self,view):
        self.mainView = view

    def start_stream(self, parameter):
        self.tweetObtainer = TweetObtainer(parameter, self.mainView)
        self.tweetObtainer.init_stream()
        self.thread = threading.Thread(target = lambda : self.tweetObtainer.start())
        self.thread.daemon = True
        self.thread.start()

    def stop_stream(self):
        self.tweetObtainer.stop_stream()



