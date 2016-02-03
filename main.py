'''
Author: Anton Steenvoorden
Hier begint de applicatie. Er wordt een controller aangemaakt en een
container voor de views (HomeView) vervolgens roepen we op de controller de
setview functie aan en geven we de live view en de pie chart view mee.
'''
from Controller import Controller
from Views import *

if __name__ == '__main__':
    mainController = Controller()
    mainView = HomeView(mainController)
    mainController.setView(mainView.get_live(), mainView.get_pie())
    mainView.mainloop()
