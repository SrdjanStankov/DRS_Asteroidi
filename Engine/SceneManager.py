import math
import time
import typing
from PyQt5 import QtCore, QtGui, QtWidgets, QtOpenGL
from PyQt5.QtCore import QPointF, QThread, pyqtSignal, QObject
from PyQt5.QtGui import QBrush, QColor, QPen, QPainterPath, QPixmap
from PyQt5.Qt import Qt
from PyQt5.QtWidgets import QWidget, QStyleOptionGraphicsItem
import PyQt5.QtOpenGL as OpenGL
from time import sleep
import threading as th
import Renderer as renderer


class internalUpdate(QObject):
    update = pyqtSignal()

    def __init__(self):
        super(internalUpdate, self).__init__()
        self.t = th.Thread(target=self.loop)
        self.t.start()

    def loop(self):
        while True:
            self.update.emit()
            sleep(1 / 60)

class SceneManager(QtWidgets.QMainWindow):

    addSignal = pyqtSignal(renderer.Renderer)

    def __init__(self, parent=None):
        super(SceneManager, self).__init__(parent)
        self.scene = QtWidgets.QGraphicsScene(self)
        self.scene.setBackgroundBrush(QBrush(QColor('yellow')))
        self.scene.setSceneRect(0, 0, 1300, 700)
        self.view = QtWidgets.QGraphicsView()
        self.view.setViewport(OpenGL.QGLWidget(OpenGL.QGLFormat(OpenGL.QGL.SampleBuffers)))
        self.view.setSceneRect(70, 0, 1280, 680)
        self.view.setViewportUpdateMode(QtWidgets.QGraphicsView.FullViewportUpdate)
        self.view.setInteractive(False)
        self.view.setScene(self.scene)
        self.setCentralWidget(self.view)
        self.scene.setItemIndexMethod(QtWidgets.QGraphicsScene.NoIndex)
        self.noti = internalUpdate()
        self.noti.update.connect(self.update)
        self.addSignal.connect(self.AddItem)


    def update(self):     
        for item in self.scene.items():
            if item.itemType == "Spaceship":
                item.rotateItem()
                item.moveItem()
            else:
                item.beh.update()
        self.scene.update()  

    def AddItem(self,renderer):
        self.scene.addItem(renderer)    
    
