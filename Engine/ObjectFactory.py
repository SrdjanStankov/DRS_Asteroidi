import GameObject as gameObject
import SceneManager
import Renderer as renderer
import Transform as transform
from AsteroidAndPlayerTypes import AsteroidType, PlayerType
from PyQt5 import QtGui
from PyQt5.QtCore import QPointF, QRectF
from PyQt5.QtWidgets import QGraphicsItem
from ItemFactory import ItemFactory

Types = ["Spaceship", "Asteroid", "Projectile"]    # ;)
class ObjectFactory:
    def __init__(self,SceneManager:SceneManager):
        self.SceneManager = SceneManager
        print("Factory on duty.")
        self.itemFactory = ItemFactory(
            largeAsteroidWidth = 80, largeAsteroidHeight = 80,
            mediumAsteroidWidth = 50, mediumAsteroidHeight = 50,
            smallAsteroidWidth = 30, smallAsteroidHeight = 30,
            player1Width = 80, player1Height = 100)

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
        go.asteroidType = kwargs["asteroidType"]
        go.transform = transform.Transform()
        go.transform.x = kwargs["transform"].x
        go.transform.y = kwargs["transform"].y
        go.transform.speed = kwargs["transform"].speed
        go.transform.rotation = kwargs["transform"].rotation
        go.transform.rotationSpeed = kwargs["transform"].rotationSpeed
        image,path = self.itemFactory.getAsteroid(AsteroidType.large)
        if go.asteroidType is AsteroidType.large:
            go.Render = renderer.Renderer(80,80,path,go.transform,image,go.Type)
        elif go.asteroidType is AsteroidType.medium:
            go.Render = renderer.Renderer(50,50,path,go.transform,image,go.Type)
        else:
            go.Render = renderer.Renderer(30,30,path,go.transform,image,go.Type)
        go.Render.setCacheMode(QGraphicsItem.DeviceCoordinateCache)

        self.SceneManager.scene.addItem(go.Render)
        
        return go

    # Here populate Spaceship with all his properties
    def _CreateSpaceShip(self,**kwargs):
        self.go = gameObject.GameObject(kwargs["callable"])
        self.go.Type = "Spaceship"
        self.go.transform = transform.Transform()
        self.go.name = kwargs["name"]
        image,path = self.itemFactory.getPlayer(PlayerType.player1)
        self.go.Render = renderer.Renderer(80,100,path,self.go.transform,image,self.go.Type)
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
