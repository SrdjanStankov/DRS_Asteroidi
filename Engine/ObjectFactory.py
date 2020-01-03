import GameObject as gameObject
import SceneManager
import Renderer as renderer
import Transform as transform

from PyQt5 import QtGui
from PyQt5.QtCore import QPointF, QRectF
from PyQt5.QtWidgets import QGraphicsItem

Types = ["Spaceship", "Asteroid", "Projectile"]    # ;)
class ObjectFactory:
    def __init__(self,SceneManager:SceneManager):
        self.SceneManager = SceneManager
        print("Factory on duty.")
        self.spaceshipWidth = 100
        self.spaceshipHeight = 120
        self.asteroidWidth = 50
        self.asteroidHeight = 50
        img1 = QtGui.QImage('spaceship2.jpg')
        img2 = img1.scaledToHeight(self.spaceshipWidth)
        self.imageSpaceship = img2.scaledToWidth(self.spaceshipHeight)
        self.imageSpaceship.convertToFormat(QtGui.QImage.Format_ARGB32)
        img3 = QtGui.QImage('asteroid1.png')
        img4 = img3.scaledToHeight(self.asteroidWidth)
        self.imageAsteroid = img4.scaledToWidth(self.asteroidHeight)
        self.imageAsteroid.convertToFormat(QtGui.QImage.Format_ARGB32)
        polygonAsteroid = QtGui.QPolygonF([QPointF(0, 0.3*self.asteroidHeight),
                                   QPointF(0, 0.6*self.asteroidHeight),
                                   QPointF(0.3*self.asteroidWidth, self.asteroidHeight),
                                   QPointF(0.8*self.asteroidWidth, self.asteroidHeight),
                                   QPointF(self.asteroidWidth, 0.6*self.asteroidHeight),
                                   QPointF(self.asteroidWidth, 0.2*self.asteroidHeight),
                                   QPointF(0.8*self.asteroidWidth, 0),
                                   QPointF(0.2*self.asteroidWidth, 0)])
        self.asteroidPath = QtGui.QPainterPath()
        self.asteroidPath.addPolygon(polygonAsteroid)
        self.asteroidPath.closeSubpath()
        x_move = 10
        y_move = -8
        polygonSpaceship = QtGui.QPolygonF([
            QPointF((self.spaceshipWidth / 2) + x_move, 0 + y_move),
            QPointF(0 + x_move, self.spaceshipHeight + y_move),
            QPointF(self.spaceshipWidth + x_move, self.spaceshipHeight + y_move),
            QPointF(self.spaceshipWidth / 2 + x_move, 0 + y_move)
                ])
        self.spaceshipPath= QtGui.QPainterPath()
        self.spaceshipPath.addPolygon(polygonSpaceship)
        self.spaceshipPath.closeSubpath()

    def Create(self,type,**kwargs):
        if(type == Types[0]):
            return self._CreateSpaceShip(**kwargs)
        elif(type == Types[1]):
            return self._CreteAsteroid(**kwargs)
        elif(type == Types[2]):
            return self._CreateProjectile(**kwargs)

    # Here populate Asteroid with all his properties
    def _CreteAsteroid(self,**kwargs):
        go = gameObject.GameObject(kwargs["callable"])
        go.Type = "Asteroid"
        go.transform = transform.Transform()
        go.transform.x = kwargs["transform"].x
        go.transform.y = kwargs["transform"].y
        go.transform.speed = kwargs["transform"].speed
        go.transform.rotation = kwargs["transform"].rotation
        go.transform.rotationSpeed = kwargs["transform"].rotationSpeed     
        go.Render = renderer.Renderer(self.asteroidWidth,self.asteroidHeight,self.asteroidPath,go.transform,self.imageAsteroid,go.Type)
        go.Render.setCacheMode(QGraphicsItem.DeviceCoordinateCache)

        self.SceneManager.scene.addItem(go.Render)
        
        return go

    # Here populate Spaceship with all his properties
    def _CreateSpaceShip(self,**kwargs):
        self.go = gameObject.GameObject()
        self.go.Type = "Spaceship"
        self.go.transform = transform.Transform()
        self.go.name = kwargs["name"]
        self.go.Render = renderer.Renderer(self.spaceshipWidth,self.spaceshipHeight,self.spaceshipPath,self.go.transform,self.imageSpaceship,self.go.Type)
        self.SceneManager.scene.addItem(self.go.Render)
        return self.go

    def _CreateProjectile(self,**kwargs):

        width = 4
        height = -12
        go = gameObject.GameObject(kwargs["callable"])
        go.Type = "Projectile"
        go.name = kwargs["name"]
        go.transform.x = kwargs["transform"].x
        go.transform.y = kwargs["transform"].y
        go.transform.rotation = kwargs["transform"].rotation
        go.transform.speed = kwargs["transform"].speed
        go.transform.rotationSpeed = kwargs["transform"].rotationSpeed
        go.Render =  renderer.Renderer(width,height,None,go.transform,None,go.Type) 
        self.SceneManager.scene.addItem(go.Render)
        go.Render.moveItem()
        go.Render.rotateItem()

        return go