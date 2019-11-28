from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QPalette, QBrush
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QApplication
from ClickableLabel import ClickableQLabel
from PyQt5 import QtCore, QtWidgets

class MultiplayerMenuu(QMainWindow):

    def __init__(self, menuss):
        super().__init__()
        self.menus = menuss
        self.initUI()

    def initUI(self):
        twoPlayer = ClickableQLabel('2 PLAYER', self)
        threePlayer = ClickableQLabel('3 PLAYER', self)
        fourPlayer = ClickableQLabel('4 PLAYER', self)
        back = ClickableQLabel('BACK', self)

        screenWidth = 1366
        screenHeight = 786

        twoPlayer.setStyleSheet("color: white; font-size: 40px")
        threePlayer.setStyleSheet("color: white; font-size: 40px")
        fourPlayer.setStyleSheet("color: white; font-size: 40px")
        back.setStyleSheet("color: white; font-size: 40px")

        twoPlayer.setGeometry(QtCore.QRect(500, 300, 300, 40))  # (x, y, width, height)
        threePlayer.setGeometry(QtCore.QRect(500, 400, 300, 40))
        fourPlayer.setGeometry(QtCore.QRect(500, 500, 300, 40))
        back.setGeometry(QtCore.QRect(100, 100, 300, 40))

        oImage = QImage("asteroids.jpg")
        sImage = oImage.scaled(QSize(screenWidth, screenHeight))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)

        self.setFixedSize(screenWidth, screenHeight)
        self.setWindowTitle('Asteroids')

        back.connect(self.clickBack)
        twoPlayer.connect(self.click2Player)
        threePlayer.connect(self.click3Player)
        fourPlayer.connect(self.click4Player)

    def clickBack(self):
        self.hide()
        self.menus.ShowStartMenu()

    def click2Player(self):
        pass

    def click3Player(self):
        pass

    def click4Player(self):
        pass


