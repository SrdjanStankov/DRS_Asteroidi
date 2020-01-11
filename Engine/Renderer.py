import typing
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPen
from PyQt5.QtWidgets import QWidget, QStyleOptionGraphicsItem
from Transform import Transform

class Renderer(QtWidgets.QGraphicsItem):
    def __init__(self, width, height,path:QtGui.QPainterPath,transform:Transform,image,type, parent=None):
        super(Renderer, self).__init__(parent)
        self.width = width
        self.height = height
        self.itemType = type
        self.transform = transform
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable, True)
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable, True)
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsFocusable, True)
        self.setTransformOriginPoint(self.width / 2, self.height / 2)
        if image is not None:
            self.image = image
            self.path = path
            self.draw = self.drawImageFunction
        else:
            self.pen = QPen(QtCore.Qt.red, 1, QtCore.Qt.SolidLine)
            self.draw = self.drawRectFunction

    def paint(self, painter: QtGui.QPainter, option: 'QStyleOptionGraphicsItem',
        widget: typing.Optional[QWidget]=...) -> None:
        self.draw(painter)

    def boundingRect(self) -> QtCore.QRectF:
        return QtCore.QRectF(0, 0, self.width, self.height)

    def drawImageFunction(self,painter: QtGui.QPainter):
        painter.setClipPath(self.path)
        painter.drawImage(QtCore.QPoint(), self.image)

    def drawRectFunction(self,painter: QtGui.QPainter):
        painter.setPen(self.pen)
        painter.setBrush(QtCore.Qt.red)
        painter.drawRect(0,0,self.width,self.height)

    def moveItem(self):
        self.setPos(self.transform.x,self.transform.y)

    def rotateItem(self):
        self.setRotation(self.transform.rotation)

    def getTopCenter(self):
        topLeft = self.mapToScene(self.boundingRect().topLeft())
        topRight = self.mapToScene(self.boundingRect().topRight())
        return (topLeft.x() + topRight.x()) / 2, (topLeft.y() + topRight.y()) / 2

    def getBottomCenter(self):
        botLeft = self.mapToScene(self.boundingRect().bottomLeft())
        botRight = self.mapToScene(self.boundingRect().bottomRight())
        return (botLeft.x() + botRight.x()) / 2, (botLeft.y() + botRight.y()) / 2