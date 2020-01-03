import math
import time
import typing
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QPointF, QThread, pyqtSignal
from PyQt5.QtGui import QBrush, QColor, QPen, QPainterPath, QPixmap
from PyQt5.Qt import Qt
from PyQt5.QtWidgets import QWidget, QStyleOptionGraphicsItem
from Transform import Transform
import GameLoop as loop

class Renderer(QtWidgets.QGraphicsItem):
    def __init__(self, width, height,polygon:QtGui.QPolygonF,transform:Transform,image:QtGui.QImage,type, parent=None):
        super(Renderer, self).__init__(parent)
        self.width = width
        self.height = height
        self.itemType = type
        self.transform = transform
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable, True)
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable, True)
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsFocusable, True)
        self.polygon = polygon
        self.setTransformOriginPoint(self.width / 2, self.height / 2)
        self.image = image


    def paint(self, painter: QtGui.QPainter, option: 'QStyleOptionGraphicsItem', widget: typing.Optional[QWidget]=...) -> None:
        if self.image is not None:
            output = QtGui.QImage(self.image.size(), QtGui.QImage.Format_ARGB32)
            output.fill(QtCore.Qt.transparent)
            painter.begin(output)
            path = QtGui.QPainterPath()
            path.addPolygon(self.polygon)
            painter.setClipPath(path)
            painter.drawImage(QtCore.QPoint(), output)
            painter.drawImage(QtCore.QPoint(), self.image)
        else:
            painter.setClipRect(option.exposedRect)
            painter.setPen(QPen(Qt.red, 4, Qt.SolidLine))
            painter.setBrush(Qt.cyan)
            painter.drawPolygon(self.polygon)


    def boundingRect(self) -> QtCore.QRectF:
        return QtCore.QRectF(0, 0, self.width, self.height)

    def moveItem(self):
        self.setPos(self.transform.x,self.transform.y)

    def rotateItem(self):
        self.setRotation(self.transform.rotation)

    def getTopLeft(self):
        return self.mapToScene(self.boundingRect().topLeft())

    def getTopRight(self):
        return self.mapToScene(self.boundingRect().topRight())




