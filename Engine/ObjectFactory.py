import GameObject as gameObject
import SceneManager
import Renderer as renderer
import Transform as transform
import Managers as mgr
import threading


import math
import time
import typing
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QPointF, QThread, pyqtSignal, QRectF, QSize
from PyQt5.QtGui import QBrush, QColor, QPen, QPainterPath, QPixmap
from PyQt5.Qt import Qt
from PyQt5.QtWidgets import QWidget, QStyleOptionGraphicsItem, QGraphicsItem


Types = ["Spaceship", "Asteroid", "Projectile"]    # ;)
class ObjectFactory:
    def __init__(self,SceneManager:SceneManager):
        self.SceneManager = SceneManager
        print("Factory on duty.")

    def Create(self,type,**kwargs):
        if(type == Types[0]):
            return self._CreateSpaceShip()
        elif(type == Types[1]):
            return self._CreteAsteroid(**kwargs)
        elif(type == Types[2]):
            return self._CreateProjectile(**kwargs)

    # Here populate Asteroid with all his properties
    def _CreteAsteroid(self,**kwargs):
        #print("Asteroid")
        print("Asteroid--->{}".format(threading.currentThread()))
        width = 50
        height = 50
        go = gameObject.GameObject()
        go.Type = "Asteroid"
        go.transform = transform.Transform()
        go.transform.x = kwargs["transform"].x
        go.transform.y = kwargs["transform"].y
        go.transform.speed = kwargs["transform"].speed
        go.transform.rotation = kwargs["transform"].rotation
        go.transform.rotationSpeed = kwargs["transform"].rotationSpeed

        polygon = QtGui.QPolygonF([QPointF(0, 0.3*height),
                                   QPointF(0, 0.6*height),
                                   QPointF(0.3*width, height),
                                   QPointF(0.8*width, height),
                                   QPointF(width, 0.6*height),
                                   QPointF(width, 0.2*height),
                                   QPointF(0.8*width, 0),
                                   QPointF(0.2*width, 0)])

        image = QtGui.QImage('asteroid1.png')
        image1 = image.scaledToHeight(width)
        image2 = image1.scaledToWidth(height)
        image2.convertToFormat(QtGui.QImage.Format_ARGB32)

        go.Render = renderer.Renderer(width,height,polygon,go.transform,image2,go.Type)
        #go.Render.setCacheMode(QGraphicsItem.DeviceCoordinateCache) 
        self.SceneManager.scene.addItem(go.Render)
        
        return go

    # Here populate Spaceship with all his properties
    def _CreateSpaceShip(self):
        print("Spaceship--->{}".format(threading.currentThread()))
        width = 100
        height = 120
        self.go = gameObject.GameObject()
        self.go.Type = "Spaceship"
        self.go.transform = transform.Transform()
        self.go.name = "Dejan"

        x_move = 10
        y_move = -8
        polygon = QtGui.QPolygonF([QPointF((width / 2) + x_move, 0 + y_move),
            QPointF(0 + x_move, height + y_move),
            #QPointF(width / 2, height * 0.85),
            QPointF(width + x_move, height + y_move),
            QPointF(width / 2 + x_move, 0 + y_move)])


        #polygon = QtGui.QPolygonF([QPointF(width/2, height), QPointF(0, height), QPointF(width, height)])

        image = QtGui.QImage('spaceship2.jpg')
        image1 = image.scaledToHeight(width)
        image2 = image1.scaledToWidth(height)
        image2.convertToFormat(QtGui.QImage.Format_ARGB32)

        self.go.Render = renderer.Renderer(width, height, polygon, self.go.transform, image2, self.go.Type)
        self.SceneManager.scene.addItem(self.go.Render)
        return self.go

    def _CreateProjectile(self, **kwargs):
        print("Projectile--->{}".format(threading.currentThread()))
        width = 4
        height = -7
        go = gameObject.GameObject()
        go.Type = "Projectile"
        go.name = kwargs["name"]
        go.transform.x = kwargs["transform"].x
        go.transform.y = kwargs["transform"].y
        go.transform.rotation = kwargs["transform"].rotation
        go.transform.speed = kwargs["transform"].speed
        go.transform.rotationSpeed = kwargs["transform"].rotationSpeed
        polygon = QtGui.QPolygonF(QRectF(0,0,width,height))

        go.Render = renderer.Renderer(width,height,polygon,go.transform,None,go.Type)
        #go.Render.setCacheMode(QGraphicsItem.DeviceCoordinateCache) 
        self.SceneManager.scene.addItem(go.Render)
        go.Render.moveItem()
        go.Render.rotateItem()

        return go