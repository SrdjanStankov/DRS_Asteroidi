import GameObject as gameObject
import SceneManager
import Renderer as renderer
import pygame
import Transform as transform
from AsteroidAndPlayerTypes import AsteroidType, PlayerType
from PyQt5 import QtGui
from PyQt5.QtCore import QPointF, QRectF, Qt
from PyQt5.QtWidgets import QGraphicsItem
from ItemFactory import ItemFactory

Types = ["Spaceship", "Asteroid", "Projectile", "SpeedUp", "FireRateSpeedUp", "ExtraLife"]    # ;)
class ObjectFactory:
    def __init__(self,SceneManager:SceneManager):
        self.SceneManager = SceneManager
        print("Factory on duty.")
   
        self.shootSound1 = pygame.mixer.Sound("shotPlayer1.wav")
        self.shootSound2 = pygame.mixer.Sound("shotPlayer2.wav")
        self.shootSound3 = pygame.mixer.Sound("shotPlayer3.wav")
        self.shootSound4 = pygame.mixer.Sound("shotPlayer4.wav")
        self.mediumAsteroidExplosionSound = pygame.mixer.Sound("mediumAsteroid.wav")
        self.smallAsteroidExplosionSound = pygame.mixer.Sound("smallAsteroid.wav")
        self.bigAsteroidExplosionSound = pygame.mixer.Sound("largeAsteroid.wav")
        self.spaceshipExplosionSound = pygame.mixer.Sound("spaceshipDestroy.wav")
        self.speedUpSound = pygame.mixer.Sound("speedUp.wav")
        self.lifeUpSound = pygame.mixer.Sound("lifeUp.wav")
        self.fireRateUpSound = pygame.mixer.Sound("fireSpeedUp.wav")
        self.itemFactory = ItemFactory(
            largeAsteroidWidth=80, largeAsteroidHeight=80,
            mediumAsteroidWidth=50, mediumAsteroidHeight=50,
            smallAsteroidWidth=30, smallAsteroidHeight=30,
            player1Width=80, player1Height=100,
            player2Width=80, player2Height=100,
            player3Width=80, player3Height=100,
            player4Width=80, player4Height=100,
            speedUpWidth=40, speedUpHeight=110,
            fireRateSpeedUpWidth=40, fireRateSpeedUpHeight=80,
            extraLifeWidth=50, extraLifeHeight=50)

    def Create(self,type,**kwargs):
        if(type == Types[0]):
            return self._CreateSpaceShip(**kwargs)
        elif(type == Types[1]):
            return self._CreteAsteroid(**kwargs)
        elif(type == Types[2]):
            return self._CreateProjectile(**kwargs)
        elif(type == Types[3]):
            return self._CreateSpeedUp(**kwargs)
        elif(type == Types[4]):
            return self._CreateFireRateSpeedUp(**kwargs)
        elif(type == Types[5]):
            return self._CreateExtraLife(**kwargs)

    def _CreateExtraLife(self, **kwargs):
        go = gameObject.GameObject()
        go.Type = "ExtraLife"
        go.transform = transform.Transform()
        go.transform.x = kwargs["transform"].x
        go.transform.y = kwargs["transform"].y
        go.transform.speed = kwargs["transform"].speed
        go.transform.rotation = kwargs["transform"].rotation
        go.transform.rotationSpeed = kwargs["transform"].rotationSpeed
        go.sound = self.lifeUpSound
        image, path = self.itemFactory.getExtraLife()
        go.Render = renderer.Renderer(50,50, transform=go.transform, type=go.Type, path=path, image=image, color = None)
        go.Render.setCacheMode(QGraphicsItem.DeviceCoordinateCache)

        self.SceneManager.scene.addItem(go.Render)

        return go
        
    def _CreateFireRateSpeedUp(self, **kwargs):
        go = gameObject.GameObject()
        go.Type = "FireRateSpeedUp"
        go.transform = transform.Transform()
        go.transform.x = kwargs["transform"].x
        go.transform.y = kwargs["transform"].y
        go.transform.speed = kwargs["transform"].speed
        go.transform.rotation = kwargs["transform"].rotation
        go.transform.rotationSpeed = kwargs["transform"].rotationSpeed
        go.sound = self.fireRateUpSound
        image, path = self.itemFactory.getFireRateSpeedUp()
        go.Render = renderer.Renderer(50,50, transform=go.transform, type=go.Type, path=path, image=image, color = None)
        go.Render.setCacheMode(QGraphicsItem.DeviceCoordinateCache)

        self.SceneManager.scene.addItem(go.Render)

        return go
        
    def _CreateSpeedUp(self, **kwargs):
        go = gameObject.GameObject()
        go.Type = "SpeedUp"
        go.transform = transform.Transform()
        go.transform.x = kwargs["transform"].x
        go.transform.y = kwargs["transform"].y
        go.transform.speed = kwargs["transform"].speed
        go.transform.rotation = kwargs["transform"].rotation
        go.transform.rotationSpeed = kwargs["transform"].rotationSpeed
        go.sound = self.speedUpSound
        image, path = self.itemFactory.getSpeedUp()
        go.Render = renderer.Renderer(50,50, transform=go.transform, type=go.Type, path=path, image=image, color = None)
        go.Render.setCacheMode(QGraphicsItem.DeviceCoordinateCache)

        self.SceneManager.scene.addItem(go.Render)

        return go

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
        
        if go.asteroidType is AsteroidType.large:
            go.sound = self.bigAsteroidExplosionSound
            go.radius = 40
            image,path = self.itemFactory.getAsteroid(AsteroidType.large)
            go.Render = renderer.Renderer(80,80,path,go.transform,image,None,go.Type)
        elif go.asteroidType is AsteroidType.medium:
            go.sound = self.mediumAsteroidExplosionSound
            go.radius = 25
            go.transform.speed += 0.2
            image,path = self.itemFactory.getAsteroid(AsteroidType.medium)
            go.Render = renderer.Renderer(50,50,path,go.transform,image,None,go.Type)
        else:
            go.sound = self.smallAsteroidExplosionSound
            go.transform.speed += 0.4
            go.radius = 15
            image,path = self.itemFactory.getAsteroid(AsteroidType.small)
            go.Render = renderer.Renderer(30,30,path,go.transform,image,None,go.Type)
        go.Render.setCacheMode(QGraphicsItem.DeviceCoordinateCache)

        self.SceneManager.scene.addItem(go.Render)
        return go

    # Here populate Spaceship with all his properties
    def _CreateSpaceShip(self,**kwargs):
        go = gameObject.GameObject(kwargs["callable"])
        go.Type = "Spaceship"
        go.transform = transform.Transform()
        go.name = kwargs["name"]
        go.playerType = kwargs["playerType"]
        if go.playerType is PlayerType.player1:
            go.shootSound = self.shootSound1
        elif go.playerType is PlayerType.player2:
            go.shootSound = self.shootSound2
        elif go.playerType is PlayerType.player3:
            go.shootSound = self.shootSound3
        else:
            go.shootSound = self.shootSound4
        go.destroySound = self.spaceshipExplosionSound
        image,path = self.itemFactory.getPlayer(kwargs["playerType"])
        go.Render = renderer.Renderer(80,100,path,go.transform,image,None,go.Type)
        self.SceneManager.scene.addItem(go.Render)
        
        return go

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
        if kwargs["playerType"] is PlayerType.player1:
            go.Render =  renderer.Renderer(width,height,None,go.transform,None,Qt.gray,go.Type) 
        if kwargs["playerType"] is PlayerType.player2:
            go.Render =  renderer.Renderer(width,height,None,go.transform,None,Qt.red,go.Type) 
        if kwargs["playerType"] is PlayerType.player3:
            go.Render =  renderer.Renderer(width,height,None,go.transform,None,Qt.green,go.Type) 
        if kwargs["playerType"] is PlayerType.player4:
            go.Render =  renderer.Renderer(width,height,None,go.transform,None,Qt.yellow,go.Type) 
        self.SceneManager.scene.addItem(go.Render)
        go.Render.moveItem()
        go.Render.rotateItem()

        return go
