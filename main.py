from Controller import Controller
from Screens import *

if __name__ == '__main__':
    mainController = Controller()
    mainView = HomeView(mainController)
    mainController.setView(mainView.get_about())
    mainView.mainloop()
