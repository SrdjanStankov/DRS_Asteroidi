import math
import time
import typing
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QPointF, QThread, pyqtSignal
from PyQt5.QtGui import QBrush, QColor, QPen, QPainterPath, QPixmap
from PyQt5.Qt import Qt
from PyQt5.QtWidgets import QWidget, QStyleOptionGraphicsItem
from GameLoop import GameLoop as gl
from time import sleep


class SceneManager(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(SceneManager, self).__init__(parent)
        self.scene = QtWidgets.QGraphicsScene(self)
        self.scene.setBackgroundBrush(QBrush(QColor('yellow')))
        self.scene.setSceneRect(0, 0, 1300, 700)
        self.view = QtWidgets.QGraphicsView(self.scene)
        self.view.setSceneRect(100, 100, 200, 200)
        self.setCentralWidget(self.view)