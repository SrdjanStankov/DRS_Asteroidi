import math
import time
import typing
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QPointF, QThread, pyqtSignal
from PyQt5.QtGui import QBrush, QColor, QPen, QPainterPath, QPixmap
from PyQt5.Qt import Qt
from PyQt5.QtWidgets import QWidget, QStyleOptionGraphicsItem
from Transform import Transform

class Renderer(QtWidgets.QGraphicsItem):
    def __init__(self, width, height,polygon:QtGui.QPolygonF,transform:Transform, parent=None):
        super(Renderer, self).__init__(parent)
        self.currentRotation = 0
        self.name = "Dejan"
        self.width = width
        self.height = height
        self.transform = transform
        self.transform.speed = 2
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable, True)
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable, True)
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsFocusable, True)
        self.polygon = polygon
        self.setTransformOriginPoint(self.width / 2, self.height / 2)

    def paint(self, painter: QtGui.QPainter, option: 'QStyleOptionGraphicsItem',
        widget: typing.Optional[QWidget]=...) -> None:
        painter.setPen(QPen(Qt.red, 4, Qt.SolidLine))

        painter.setBrush(Qt.cyan)
        painter.drawPolygon(self.polygon)

    def boundingRect(self) -> QtCore.QRectF:
        return QtCore.QRectF(0, 0, self.width, self.height)

    def moveItem(self):
        self.setPos(self.transform.position.x,self.transform.position.y)

    def rotateItem(self):
        self.setRotation(self.transform.rotation)


