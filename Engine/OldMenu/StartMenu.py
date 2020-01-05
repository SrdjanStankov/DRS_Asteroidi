import sys

from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPixmap, QPalette, QImage, QBrush
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QApplication
from ClickableLabel import ClickableQLabel
from PyQt5 import QtCore, QtWidgets



class StartMenu(QMainWindow):

    def __init__(self, menuss):
        super().__init__()
        self.menus = menuss
        self.initUI()

    def initUI(self):
        singleplayer = ClickableQLabel('SINGLEPLAYER', self)
        multiplayer = ClickableQLabel('MULTIPLAYER', self)
        exit = ClickableQLabel('EXIT', self)
        asteroids = QLabel('ASTEROIDS', self)

        multiplayer.setStyleSheet("color: white; font-size: 40px")
        singleplayer.setStyleSheet("color: white; font-size: 40px")
        exit.setStyleSheet("color: white; font-size: 40px")
        asteroids.setStyleSheet("color: white; font-size: 75px")


        singleplayer.connect(self.MyClickSinglePlayer)
        multiplayer.connect(self.MyClickMultiPlayer)
        exit.connect(self.MyClickExit)

        singleplayer.setGeometry(QtCore.QRect(500, 300, 300, 40)) #(x, y, width, height)
        multiplayer.setGeometry(QtCore.QRect(500, 400, 300, 40))
        exit.setGeometry(QtCore.QRect(500, 500, 300, 40))
        asteroids.setGeometry(QtCore.QRect(450, 100, 500, 65))


        screenWidth = 1366
        screenHeight = 786

        oImage = QImage("asteroids.jpg")
        sImage = oImage.scaled(QSize(screenWidth, screenHeight))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)

        self.setFixedSize(screenWidth, screenHeight)
        self.setWindowTitle('Asteroids')


    def MyClickExit(self):
        sys.exit()

    def MyClickSinglePlayer(self):
        print('sp')

    def MyClickMultiPlayer(self):
        self.menus.ShowMultiplayerMenu()
        self.hide()
