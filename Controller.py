from TweetObtainer import TweetObtainer
import threading
class Controller():
    mainView =''

    def __init__(self):
        print("Controller created")

    def setView(self,view):
        self.mainView = view

    def start_stream(self, parameter):
        tweetObtainer = TweetObtainer(parameter, self.mainView)
        tweetObtainer.init_stream()
        t2 = threading.Thread(target=tweetObtainer.start())
        t2.daemon = True
        t2.start()



