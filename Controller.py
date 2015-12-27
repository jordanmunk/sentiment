from TweetObtainer import TweetObtainer
from LiveView import LiveView
import threading

class Controller():
    def __init__(self):
        print("Controller created")

    def start_stream(self, parameter):
        liveView = LiveView()
        tweetObtainer = TweetObtainer(parameter, liveView)
        tweetObtainer.init_stream()
        t1 = threading.Thread(target=tweetObtainer.start())
        t1.start()
