from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtGui import QBrush, QColor
from time import sleep
import threading as th
import Renderer as renderer
import GameLoop as gameLoop

class internalUpdate(QObject):
    update = pyqtSignal()
    def __init__(self):
        super(internalUpdate, self).__init__()
        self.t = th.Thread(target=self.loop)
        self.t.start()
    def loop(self):
        while True:
            if gameLoop.GameLoop.getInstance()._cancelation_token==True:
                break
            self.update.emit()
            sleep(1 / 60)

class SceneManager(QtWidgets.QMainWindow):

    addSignal = pyqtSignal(renderer.Renderer)

    def __init__(self, parent=None):
        super(SceneManager, self).__init__(parent)
        self.scene = QtWidgets.QGraphicsScene(self)
        self.scene.setBackgroundBrush(QBrush(QColor('black')))
        self.scene.setSceneRect(0, 0, 1500, 980)
        self.view = QtWidgets.QGraphicsView(self.scene)
        self.view.setSceneRect(90,90, 1250, 738)
        self.view.setViewportUpdateMode(QtWidgets.QGraphicsView.NoViewportUpdate)
        self.view.setInteractive(False)
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
                item.moveItem()
        self.scene.update()

    def AddItem(self,renderer):
        self.scene.addItem(renderer)    