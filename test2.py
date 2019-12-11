import time
import typing
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QPointF, QThread, pyqtSignal
from PyQt5.QtGui import QBrush, QColor, QPen, QPainterPath, QPixmap
from PyQt5.Qt import Qt
from PyQt5.QtWidgets import QWidget, QStyleOptionGraphicsItem


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
        return QtCore.QRectF(0, 0, 100, 100)

    def shape(self) -> QtGui.QPainterPath:
        path = QPainterPath()
        path.addPolygon(self.polygon)
        return path

    def rotateLeft(self):
        self.currentRotation -= 10
        self.setRotation(self.currentRotation)

    def rotateRight(self):
        self.currentRotation += 10
        self.setRotation(self.currentRotation)

    def centerRotation(self):
        self.setTransformOriginPoint(self.boundingRect().center().x(),
                                     self.boundingRect().center().y())


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
        scene = QtWidgets.QGraphicsScene(self)
        scene.setBackgroundBrush(QBrush(QColor('yellow')))
        scene.setSceneRect(0, 0, 200, 200)
        view = QtWidgets.QGraphicsView(scene)
        view.setSceneRect(20, 20, 100, 100)
        self.setCentralWidget(view)
        self.player = Player(100, 100)
        scene.addItem(self.player)
        self.player.centerRotation()
        self.rect = scene.addRect(0, -100, 50, 50)
        self.th = MoveThread()
        self.th.s.connect(self.func)
        self.th.start()

    def keyPressEvent(self, a0: QtGui.QKeyEvent):
        if a0.key() == Qt.Key_A:
            self.player.rotateLeft()
        elif a0.key() == Qt.Key_D:
            self.player.rotateRight()
        elif a0.key() == Qt.Key_W:
            self.player.moveBy(0, -10)
        elif a0.key() == Qt.Key_S:
            self.player.moveBy(0, 10)

    def func(self):
        if self.player.collidesWithItem(self.rect):
            self.player.hide()




if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.resize(640, 480)
    w.show()
    sys.exit(app.exec_())
