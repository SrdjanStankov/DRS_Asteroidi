from PyQt5.QtCore import QPointF, QRectF
from AsteroidAndPlayerTypes import AsteroidType, PlayerType
from PyQt5 import QtGui


class ItemFactory():
    def __init__(self,**kwargs):
        self.asteroidImages = {}
        self.asteroidPaths = {}
        self.playerImages = {}
        self.playerPaths = {}
        if "largeAsteroidWidth" in kwargs and "largeAsteroidHeight" in kwargs: 
            self.asteroidImages[AsteroidType.large], self.asteroidPaths[AsteroidType.large] = self.makeAsteroid(kwargs["largeAsteroidWidth"],kwargs["largeAsteroidHeight"],'asteroid1.png')
        if "player1Height" in kwargs and "player1Width" in kwargs:
            self.playerImages[PlayerType.player1], self.playerPaths[PlayerType.player1] = self.makePlayer(kwargs["player1Width"],kwargs["player1Height"],'spaceship2.jpg')
        if "mediumAsteroidWidth" in kwargs and "mediumAsteroidHeight" in kwargs: 
            self.asteroidImages[AsteroidType.medium], self.asteroidPaths[AsteroidType.medium] = self.makeAsteroid(kwargs["mediumAsteroidWidth"],kwargs["mediumAsteroidHeight"],'asteroid1.png')
        if "smallAsteroidWidth" in kwargs and "smallAsteroidHeight" in kwargs: 
            self.asteroidImages[AsteroidType.small], self.asteroidPaths[AsteroidType.small] = self.makeAsteroid(kwargs["smallAsteroidWidth"],kwargs["smallAsteroidHeight"],'asteroid1.png')
        

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

    def makeAsteroid(self,width,height,imageName):
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

    def makePlayer(self,width,height,image):
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
