from Controller import Controller
from Views import *

if __name__ == '__main__':
    mainController = Controller()
    mainView = HomeView(mainController)
    mainController.setView(mainView.get_about())
    mainView.mainloop()
