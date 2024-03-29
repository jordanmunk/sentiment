'''
Author: Anton Steenvoorden
Creeert de tweetobtainer en geeft de live en pie view hieraan mee zodat de
update functie kan worden geroepen. Zet de tweetobtainer in een aparte
thread dmv een lambda expressie. Dit zodat er geen conflict is met de GUI
thread
'''
from TweetObtainer import TweetObtainer
import threading

class Controller():
    mainView = None
    pieView = None
    tweetObtainer = None

    def __init__(self):
        print("Controller created")

    def setView(self,view, pie):
        self.mainView = view
        self.pieView = pie

    def start_stream(self, parameter):
        self.tweetObtainer = TweetObtainer(parameter, self.mainView, self.pieView)
        self.tweetObtainer.init_stream()
        self.thread = threading.Thread(target = lambda : self.tweetObtainer.start())
        self.thread.daemon = True
        self.thread.start()

    def stop_stream(self):
        self.tweetObtainer.stop_stream()



