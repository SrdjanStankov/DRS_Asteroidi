import GameObject as gameObject
import SceneManager
import Renderer as renderer
import Transform as transform
from AsteroidAndPlayerTypes import AsteroidType, PlayerType
from PyQt5 import QtGui
from PyQt5.QtCore import QPointF, QRectF
from PyQt5.QtWidgets import QGraphicsItem

Types = ["Spaceship", "Asteroid", "Projectile", "SpeedUp"]    # ;)
class ObjectFactory:
    def __init__(self,SceneManager:SceneManager):
        self.SceneManager = SceneManager
        print("Factory on duty.")
        self.spaceshipWidth = 100
        self.spaceshipHeight = 120
        self.asteroidWidth = 50
        self.asteroidHeight = 50
        self.itemFactory = ItemFactory(largeAsteroidWidth = self.asteroidWidth, largeAsteroidHeight = self.asteroidHeight, player1Width = self.spaceshipWidth, player1Height = self.spaceshipHeight)

    def Create(self,type,**kwargs):
        if(type == Types[0]):
            return self._CreateSpaceShip(**kwargs)
        elif(type == Types[1]):
            return self._CreteAsteroid(**kwargs)
        elif(type == Types[2]):
            return self._CreateProjectile(**kwargs)
        elif(type == Types[3]):
            return self._CreateSpeedUp(**kwargs)

    def _CreateSpeedUp(self, **kwargs):
        go = gameObject.GameObject()
        go.Type = "SpeedUp"
        go.transform = transform.Transform()
        go.transform.x = kwargs["transform"].x
        go.transform.y = kwargs["transform"].y
        go.transform.speed = kwargs["transform"].speed
        go.transform.rotation = kwargs["transform"].rotation
        go.transform.rotationSpeed = kwargs["transform"].rotationSpeed
        go.Render = renderer.Renderer(50,50, transform=go.transform, type=go.Type, path=None, image=None)
        go.Render.setCacheMode(QGraphicsItem.DeviceCoordinateCache)

        self.SceneManager.scene.addItem(go.Render)

        return go

    # Here populate Asteroid with all his properties
    def _CreteAsteroid(self,**kwargs):
        go = gameObject.GameObject(kwargs["callable"])
        go.Type = "Asteroid"
        go.asteroidType = AsteroidType.large
        go.transform = transform.Transform()
        go.transform.x = kwargs["transform"].x
        go.transform.y = kwargs["transform"].y
        go.transform.speed = kwargs["transform"].speed
        go.transform.rotation = kwargs["transform"].rotation
        go.transform.rotationSpeed = kwargs["transform"].rotationSpeed
        image,path = self.itemFactory.getAsteroid(AsteroidType.large)
        go.Render = renderer.Renderer(self.asteroidWidth,self.asteroidHeight,path,go.transform,image,go.Type)
        go.Render.setCacheMode(QGraphicsItem.DeviceCoordinateCache)

        self.SceneManager.scene.addItem(go.Render)
        
        return go

    # Here populate Spaceship with all his properties
    def _CreateSpaceShip(self,**kwargs):
        self.go = gameObject.GameObject()
        self.go.Type = "Spaceship"
        self.go.transform = transform.Transform()
        self.go.name = kwargs["name"]
        image,path = self.itemFactory.getPlayer(PlayerType.player1)
        self.go.Render = renderer.Renderer(self.spaceshipWidth,self.spaceshipHeight,path,self.go.transform,image,self.go.Type)
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



class ItemFactory():
    def __init__(self,**kwargs):
        self.asteroidImages = {}
        self.asteroidPaths = {}
        self.playerImages = {}
        self.playerPaths = {}
        if "largeAsteroidWidth" in kwargs and "largeAsteroidHeight" in kwargs: 
            self.asteroidImages[AsteroidType.large], self.asteroidPaths[AsteroidType.large] = self.makeLargeAsteroid(kwargs["largeAsteroidWidth"],kwargs["largeAsteroidHeight"],'asteroid1.png')
        if "player1Height" in kwargs and "player1Width" in kwargs:
            self.playerImages[PlayerType.player1], self.playerPaths[PlayerType.player1] = self.makePlayerOne(kwargs["player1Width"],kwargs["player1Height"],'spaceship2.jpg')
  

    def getPlayer(self,playerType : PlayerType):
        if playerType == PlayerType.player1:
            return self.playerImages[playerType], self.playerPaths[playerType]
        else:
            return None, None

    def getAsteroid(self,asteroidType:AsteroidType):
        if asteroidType == AsteroidType.large:
            if asteroidType in self.asteroidImages:
                return self.asteroidImages[asteroidType], self.asteroidPaths[asteroidType]
            else:
                return None, None
        else:
            return None, None

    def makeLargeAsteroid(self,width,height,imageName):
        img3 = QtGui.QImage(imageName)
        img4 = img3.scaledToHeight(width)
        imageAsteroid = img4.scaledToWidth(height)
        imageAsteroid.convertToFormat(QtGui.QImage.Format_ARGB32)
        polygonAsteroid = QtGui.QPolygonF([QPointF(0, 0.3 * height),
                                   QPointF(0, 0.6 * height),
                                   QPointF(0.3 * width, height),
                                   QPointF(0.8 * width, height),
                                   QPointF(width, 0.6 * height),
                                   QPointF(width, 0.2 * height),
                                   QPointF(0.8 * width, 0),
                                   QPointF(0.2 * width, 0)])
        asteroidPath = QtGui.QPainterPath()
        asteroidPath.addPolygon(polygonAsteroid)
        asteroidPath.closeSubpath()
        return imageAsteroid, asteroidPath

    def makePlayerOne(self,width,height,image):
        img1 = QtGui.QImage(image)
        img2 = img1.scaledToHeight(width)
        imageSpaceship = img2.scaledToWidth(height)
        imageSpaceship.convertToFormat(QtGui.QImage.Format_ARGB32)
        x_move = 10
        y_move = -8
        polygonSpaceship = QtGui.QPolygonF([
        QPointF((width / 2) + x_move, 0 + y_move),
        QPointF(0 + x_move, height + y_move),
        QPointF(width + x_move, height + y_move),
        QPointF(width / 2 + x_move, 0 + y_move)
        ])
        spaceshipPath= QtGui.QPainterPath()
        spaceshipPath.addPolygon(polygonSpaceship)
        spaceshipPath.closeSubpath()
        return imageSpaceship, spaceshipPath