import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

class LiveView():
    fig = ''
    ax1 = ''

    def __init__(self):
        print("init called")
        style.use("ggplot")
        self.fig = plt.figure()
        self.ax1 = self.fig.add_subplot(1,1,1)

        self.xar = []
        self.yar = []

        self.x = 0
        self.y = 0
        plt.show()

#Gets called each time data is obtained by TweetObtainer
    def update(self,text):
        self.x += 1
        if text.startswith("pos"):
            self.y += 1
        elif text.startswith("neg"):
            self.y -= 1

        self.xar.append(self.x)
        self.yar.append(self.y)

        self.ax1.clear()
        self.ax1.plot(self.xar,self.yar)

