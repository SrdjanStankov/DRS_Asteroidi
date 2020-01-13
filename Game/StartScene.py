from PyQt5.QtCore import QSize, QRect
from PyQt5.QtGui import QBrush, QColor, QImage, QPixmap
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsPixmapItem, QLabel

from ClickableLabel import ClickableQLabel


class StartScene(QGraphicsScene):
    def __init__(self, singlepalyerMethod, multiplayerMethod, exitMethod, parent=None):
        super(StartScene, self).__init__(parent)

        screenWidth = 1370
        screenHeight = 730
        oImage = QPixmap("asteroids.jpg")
        sImage = oImage.scaled(QSize(screenWidth, screenHeight))  # resize Image to widgets size

        self.graphicsPixmapItem = QGraphicsPixmapItem(sImage)
        self.addItem(self.graphicsPixmapItem)
        self.setSceneRect(0, 0, screenWidth, screenHeight)

        singleplayer = ClickableQLabel('SINGLEPLAYER')
        multiplayer = ClickableQLabel('MULTIPLAYER')
        exit = ClickableQLabel('EXIT')
        asteroids = QLabel('ASTEROIDS')

        multiplayer.setStyleSheet("color: white; font-size: 40px; background-color: rgba(0,0,0,0%)")
        singleplayer.setStyleSheet("color: white; font-size: 40px; background-color: rgba(0,0,0,0%)")
        exit.setStyleSheet("color: white; font-size: 40px; background-color: rgba(0,0,0,0%)")
        asteroids.setStyleSheet("color: white; font-size: 75px; background-color: rgba(0,0,0,0%)")

        singleplayer.setGeometry(QRect(500, 300, 300, 40))  # (x, y, width, height)
        multiplayer.setGeometry(QRect(500, 400, 300, 40))
        exit.setGeometry(QRect(500, 500, 300, 40))
        asteroids.setGeometry(QRect(450, 100, 500, 65))

        singleplayer.connect(singlepalyerMethod)
        multiplayer.connect(multiplayerMethod)
        exit.connect(exitMethod)

        self.addWidget(singleplayer)
        self.addWidget(multiplayer)
        self.addWidget(exit)
        self.addWidget(asteroids)