from PyQt5.QtCore import QSize, QRect
from PyQt5.QtGui import QBrush, QColor, QImage, QPixmap
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsPixmapItem, QLabel

from ClickableLabel import ClickableQLabel


class MultiplayerScene(QGraphicsScene):
    def __init__(self,twoPlayersMethod,threePlayersMethod,fourPlayersMethod, backMethod, parent=None):
        super(MultiplayerScene, self).__init__(parent)

        screenWidth = 1300
        screenHeight = 700

        oImage = QPixmap("asteroids.jpg")
        sImage = oImage.scaled(QSize(screenWidth, screenHeight))  # resize Image to widgets size

        self.graphicsPixmapItem = QGraphicsPixmapItem(sImage)
        self.addItem(self.graphicsPixmapItem)
        self.setSceneRect(0, 0, screenWidth, screenHeight)

        twoPlayer = ClickableQLabel('2 PLAYER')
        threePlayer = ClickableQLabel('3 PLAYER')
        fourPlayer = ClickableQLabel('4 PLAYER')
        back = ClickableQLabel('BACK')

        twoPlayer.setStyleSheet("color: white; font-size: 40px; background-color: rgba(0,0,0,0%)")
        threePlayer.setStyleSheet("color: white; font-size: 40px; background-color: rgba(0,0,0,0%)")
        fourPlayer.setStyleSheet("color: white; font-size: 40px; background-color: rgba(0,0,0,0%)")
        back.setStyleSheet("color: white; font-size: 40px; background-color: rgba(0,0,0,0%)")

        twoPlayer.setGeometry(QRect(500, 300, 300, 40))  # (x, y, width, height)
        threePlayer.setGeometry(QRect(500, 400, 300, 40))
        fourPlayer.setGeometry(QRect(500, 500, 300, 40))
        back.setGeometry(QRect(100, 100, 300, 40))

        #connect
        back.connect(backMethod)
        twoPlayer.connect(twoPlayersMethod)
        threePlayer.connect(threePlayersMethod)
        fourPlayer.connect(fourPlayersMethod)

        self.addWidget(twoPlayer)
        self.addWidget(threePlayer)
        self.addWidget(fourPlayer)
        self.addWidget(back)