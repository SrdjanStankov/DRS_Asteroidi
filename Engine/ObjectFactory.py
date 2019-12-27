import GameObject as gameObject
import SceneManager
import SceneManager
import Renderer as renderer

import math
import time
import typing
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QPointF, QThread, pyqtSignal
from PyQt5.QtGui import QBrush, QColor, QPen, QPainterPath, QPixmap
from PyQt5.Qt import Qt
from PyQt5.QtWidgets import QWidget, QStyleOptionGraphicsItem


Types = ["Spaceship", "Asteroid"]    # ;)
class ObjectFactory:
    def __init__(self,SceneManager:SceneManager):
        self.SceneManager = SceneManager
        print("Factory on duty.")

    def Create(self,type):
        if(type == Types[0]):
            return self._CreateSpaceShip()
        elif(type == Types[1]):
            return self._CreteAsteroid()

    # Here populate Asteroid with all his properties
    def _CreteAsteroid(self):
        #print("Asteroid")
        self.go = gameObject.GameObject()
        self.go.Type = "Asteroid"
        return self.go

    # Here populate Spaceship with all his properties
    def _CreateSpaceShip(self):
        #print("Spaceship")
        width = 50
        height = 50
        self.go = gameObject.GameObject()
        self.go.Type = "Spaceship"
        polygon = QtGui.QPolygonF([QPointF(width / 2, 0),
            QPointF(0, height),
            QPointF(width / 2, height * 0.75),
            QPointF(width, height),
            QPointF(width / 2, 0)])

        self.go.Render = renderer.Renderer(50,50,polygon,self.go.transform)
        self.SceneManager.scene.addItem(self.go.Render)
        return self.go