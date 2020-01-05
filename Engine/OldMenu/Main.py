from PyQt5.QtWidgets import QApplication
from MenusFacade import Menus
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    menus = Menus.getInstance()
    menus.ShowStartMenu()
    sys.exit(app.exec_())