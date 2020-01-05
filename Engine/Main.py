# Here start up StartUI
from PyQt5.QtWidgets import QApplication
import sys
import StartMenuManager as smm


if __name__ == "__main__":
    print("This is main")
    
    #=====test==========

    app = QApplication(sys.argv)
    startMenuManager = smm.StartMenuManager(app)
    startMenuManager.resize(1300, 700)
    startMenuManager.show()

    sys.exit(app.exec_())


