from TweetObtainer import TweetObtainer
from Plotter import Plotter
import threading
class Controller():
    def __init__(self):
        print("Controller created")

    def start_stream(self, parameter):
        tweetObtainer = TweetObtainer(parameter)
        tweetObtainer.init_stream()
        t1 = threading.Thread(target=tweetObtainer.start())
        t1.start()
        t2 = threading.Thread(target=Plotter.animate())
        t2.start()