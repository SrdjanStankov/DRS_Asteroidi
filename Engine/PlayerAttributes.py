
import typing
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtCore import QRectF, QPointF
from PyQt5.QtGui import QPen, QColor, QFont
from PyQt5.QtWidgets import QWidget, QStyleOptionGraphicsItem
import AsteroidAndPlayerTypes as aapt

class PlayerAttributes(QtWidgets.QGraphicsTextItem):
    def __init__(self, player, type="placeholder", parent=None):
        super(QtWidgets.QGraphicsTextItem, self).__init__(parent)
        self.width = 100
        self.height = 50
        self.itemType = type
        self.player = player
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable, False)
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable, False)
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsFocusable, False)
        self.setTransformOriginPoint(self.width / 2, self.height / 2)
        self.setZValue(1)
        self.pen = QPen(QtCore.Qt.red, 1, QtCore.Qt.SolidLine)
        self.font = QFont('Helvetica', 14)
        self.font.setBold(True)
        self.x_step = 250  #promeniti kada bude bilo potrebno

        if self.player.playerType is aapt.PlayerType.player1:
            self.x_pos = 0
            self.color = QColor("Grey")
        elif self.player.playerType is aapt.PlayerType.player2:
            self.x_pos = self.x_step
            self.color = QColor("Red")
        elif self.player.playerType is aapt.PlayerType.player3:
            self.x_pos = self.x_step * 2
            self.color = QColor("Yellow")
        else:
            self.x_pos = self.x_step * 3
            self.color = QColor("Green")

        self.setPos(self.x_pos, 70)


    def paint(self, painter: QtGui.QPainter, option: 'QStyleOptionGraphicsItem',
              widget: typing.Optional[QWidget] = ...) -> None:

        painter.setPen(self.color)
        painter.setFont(self.font)
        painter.drawText(QPointF(50, 50), self.player.name + " : " + str(self.player.points) + "\n Lives : " + str(self.player.lives))


    def moveItem(self):
        pass

    def rotateItem(self):
        pass

    def boundingRect(self) -> QtCore.QRectF:
        return QtCore.QRectF(0, 0, self.width, self.height)
