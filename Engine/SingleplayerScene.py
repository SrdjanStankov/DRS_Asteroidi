from PyQt5.QtCore import QSize, QRect
from PyQt5.QtGui import QBrush, QColor, QImage, QPixmap
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsPixmapItem, QLabel, QGraphicsView

from ClickableLabel import ClickableQLabel

class SingleplayerScene(QGraphicsScene):
    def __init__(self, parent=None):
        super(SingleplayerScene, self).__init__(parent)

        screenWidth = 1300
        screenHeight = 700

        self.setBackgroundBrush(QBrush(QColor('black')))
        self.setSceneRect(0, 0, screenWidth, screenHeight)
        self.setItemIndexMethod(QGraphicsScene.NoIndex)


