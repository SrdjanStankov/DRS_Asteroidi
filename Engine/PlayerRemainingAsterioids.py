import typing
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtCore import QRectF, QPointF
from PyQt5.QtGui import QPen, QColor, QFont
from PyQt5.QtWidgets import QWidget, QStyleOptionGraphicsItem
import AsteroidAndPlayerTypes as aapt

class PlayerRemainingAsteroids(QtWidgets.QGraphicsTextItem):
    def __init__(self, gameManager , type="placeholder", parent=None):
        super(QtWidgets.QGraphicsTextItem, self).__init__(parent)
        self.width = 100
        self.height = 50
        self.itemType = type
        self.gameManager = gameManager
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable, False)
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable, False)
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsFocusable, False)
        self.setTransformOriginPoint(self.width / 2, self.height / 2)
        self.setZValue(1)

        self.color = QColor("Grey")
        self.font = QFont('Helvetica', 14)
        self.font.setBold(True)

        self.setPos(1170, 100)


    def paint(self, painter: QtGui.QPainter, option: 'QStyleOptionGraphicsItem',
              widget: typing.Optional[QWidget] = ...) -> None:

        painter.setPen(self.color)
        painter.setFont(self.font)
        painter.drawText(QPointF(50, 50), "Remaining : " + str(self.gameManager.asteroidsToDestroy))


    def moveItem(self):
        pass

    def rotateItem(self):
        pass

    def boundingRect(self) -> QtCore.QRectF:
        return QtCore.QRectF(0, 0, self.width, self.height)
