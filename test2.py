import math
import time
import typing
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QPointF, QThread, pyqtSignal, QRectF
from PyQt5.QtGui import QBrush, QColor, QPen, QPainterPath, QPixmap
from PyQt5.Qt import Qt
from PyQt5.QtWidgets import QWidget, QStyleOptionGraphicsItem, QGraphicsEllipseItem, QGraphicsRectItem
from numpy import arctan2, arccos


class RectItem(QtWidgets.QGraphicsRectItem):
    def __init__(self, parent=None):
        super(RectItem, self).__init__(parent)
        self.currentRotation = 0
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable, True)
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable, True)
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsFocusable, True)

    def paint(self, painter, option, widget=None):
        super(RectItem, self).paint(painter, option, widget)
        painter.save()
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        painter.setBrush(QtCore.Qt.red)
        painter.drawEllipse(option.rect)
        painter.restore()


class Player(QtWidgets.QGraphicsItem):
    def __init__(self, width, height, parent=None):
        super(Player, self).__init__(parent)
        self.currentRotation = 0
        self.name = "Dejan"
        temp = self.getPosition()
        self.currentX = temp[0]
        self.currentY = temp[1]
        self.width = width
        self.height = height
        self.projectileX = 0
        self.projectileY = 0
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable, True)
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable, True)
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsFocusable, True)
        self.polygon = QtGui.QPolygonF([
            QPointF(width / 2, 0),
            QPointF(0, height),
            QPointF(width / 2, height * 0.75),
            QPointF(width, height),
            QPointF(width / 2, 0)
        ]
        )

    def paint(self, painter: QtGui.QPainter, option: 'QStyleOptionGraphicsItem',
              widget: typing.Optional[QWidget] = ...) -> None:
        painter.setPen(QPen(Qt.red, 4, Qt.SolidLine))

        painter.setBrush(Qt.cyan)
        painter.drawPolygon(self.polygon)

    def boundingRect(self) -> QtCore.QRectF:
        return QtCore.QRectF(0, 0, self.width, self.height)

    def shape(self) -> QtGui.QPainterPath:
        path = QPainterPath()
        path.addPolygon(self.polygon)
        return path

    def getPosition(self):
        pos = self.scenePos()
        return pos.x(), pos.y()

    def moveUp(self, amount=1):
        self.currentX += math.sin(math.radians(self.currentRotation)) * amount
        self.currentY -= math.cos(math.radians(self.currentRotation)) * amount
        #self.moveBy(dx - x, y - dy)
        self.setPos(self.currentX, self.currentY)

    def moveDown(self, amount=1):
        x, y = self.getPosition()
        dx = x - math.sin(math.radians(self.currentRotation)) * amount
        dy = y - math.cos(math.radians(self.currentRotation)) * amount
        self.moveBy(dx - x, y - dy)

    def rotateLeft(self):
        self.currentRotation -= 5
        self.setRotation(self.currentRotation)

    def rotateRight(self):
        self.currentRotation += 5
        self.setRotation(self.currentRotation)

    def centerRotation(self):
        self.setTransformOriginPoint(self.boundingRect().center().x(),
                                     self.boundingRect().center().y())
    def getCenterSpot(self):
        temp1 = self.mapToScene(self.boundingRect().topLeft())
        x1 = temp1.x()
        y1 = temp1.y()
        temp2 = self.mapToScene(self.boundingRect().topRight())
        x2 = temp2.x()
        y2 = temp2.y()
        Cx = (x1 + x2)/2
        Cy = (y1 + y2)/2

        item = Projectile(Cx,Cy,10,-20,self.currentRotation)
        item.setMyRotation()
        return item


class Projectile(QtWidgets.QGraphicsItem):
    def __init__(self, x,y,width, height, rotation, parent=None):
        super(Projectile, self).__init__(parent)
        self.currentRotation = rotation
        self.currentX = x
        self.currentY = y
        self.width = width
        self.height = height
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable, True)
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable, True)
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsFocusable, True)
        self.rect = QRectF(0, 0, self.width, self.height)

    def paint(self, painter: QtGui.QPainter, option: 'QStyleOptionGraphicsItem',
              widget: typing.Optional[QWidget] = ...) -> None:
        painter.setPen(QPen(Qt.red, 4, Qt.SolidLine))
        painter.setBrush(Qt.cyan)
        painter.drawRect(self.rect)

    def boundingRect(self) -> QtCore.QRectF:
        return self.rect

    def getPosition(self):
        pos = self.scenePos()
        return pos.x(), pos.y()

    def moveUp(self, amount=1):
        self.currentX += math.sin(math.radians(self.currentRotation)) * amount
        self.currentY -= math.cos(math.radians(self.currentRotation)) * amount
        # self.moveBy(dx - x, y - dy)
        self.setPos(self.currentX, self.currentY)

    def moveDown(self, amount=1):
        self.currentX -= math.sin(math.radians(self.currentRotation)) * amount
        self.currentY += math.cos(math.radians(self.currentRotation)) * amount
        # self.moveBy(dx - x, y - dy)
        self.setPos(self.currentX, self.currentY)

    def setMyRotation(self):
        self.setRotation(self.currentRotation)


class MoveThread(QThread):
    s = pyqtSignal()

    def __init__(self):
        super().__init__()

    def run(self):
        for i in range(1, 1000000):
            time.sleep(1)
            self.s.emit()


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.projectiles = []
        self.scene = QtWidgets.QGraphicsScene(self)
        self.scene.setBackgroundBrush(QBrush(QColor('yellow')))
        self.scene.setSceneRect(0, 0, 500, 500)
        view = QtWidgets.QGraphicsView(self.scene)
        view.setSceneRect(100, 100, 200, 200)
        self.setCentralWidget(view)
        self.player = Player(50, 50)
        self.scene.addItem(self.player)
        self.player.setPos(self.scene.sceneRect().center())
        self.player.centerRotation()
        self.rect = self.scene.addRect(100, 100, 50, 50)
        self.th = MoveThread()
        self.th.s.connect(self.func)
        self.th.start()

    def keyPressEvent(self, a0: QtGui.QKeyEvent):
        if a0.key() == Qt.Key_A:
            self.player.rotateLeft()
        elif a0.key() == Qt.Key_D:
            self.player.rotateRight()
        elif a0.key() == Qt.Key_W:
            self.player.moveUp(5)
        elif a0.key() == Qt.Key_S:
            a = self.player.getCenterSpot()
            a.setPos(a.currentX, a.currentY)
            self.scene.addItem(a)
            self.projectiles.append(a)
            self.scene.update()

    def func(self):
        for a in self.projectiles:
            a.moveUp(20)
            if a.currentY < 0 or a.currentX < 0:
                self.scene.removeItem(a)
        self.scene.update()
        
        if self.player.collidesWithItem(self.rect):
            self.player.hide()


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.resize(640, 480)
    w.show()
    sys.exit(app.exec_())
