from PyQt5.QtCore import QPointF, QRectF
from AsteroidAndPlayerTypes import AsteroidType, PlayerType
from PyQt5 import QtGui


class ItemFactory():
    def __init__(self,**kwargs):
        self.asteroidImages = {}
        self.asteroidPaths = {}
        self.playerImages = {}
        self.playerPaths = {}
        self.speedUpImage = None
        self.speedUpPath = None
        self.fireRateSpeedUpImage = None
        self.fireRateSpeedUpPath = None
        self.extraLifeImage = None
        self.extraLifePath = None

        if "largeAsteroidWidth" in kwargs and "largeAsteroidHeight" in kwargs: 
            self.asteroidImages[AsteroidType.large], self.asteroidPaths[AsteroidType.large] = self.makeAsteroid(kwargs["largeAsteroidWidth"],kwargs["largeAsteroidHeight"],'asteroid1.png')
        if "player1Height" in kwargs and "player1Width" in kwargs:
            self.playerImages[PlayerType.player1], self.playerPaths[PlayerType.player1] = self.makePlayer(kwargs["player1Width"],kwargs["player1Height"], 'spaceship2.jpg')
        if "player2Height" in kwargs and "player2Width" in kwargs:
            self.playerImages[PlayerType.player2], self.playerPaths[PlayerType.player2] = self.makePlayer(kwargs["player2Width"],kwargs["player2Height"], 'spaceshipRed.jpg')
        if "player3Height" in kwargs and "player3Width" in kwargs:
            self.playerImages[PlayerType.player3], self.playerPaths[PlayerType.player3] = self.makePlayer(kwargs["player3Width"],kwargs["player3Height"], 'spaceshipYellow.jpg')
        if "player4Height" in kwargs and "player4Width" in kwargs:
            self.playerImages[PlayerType.player4], self.playerPaths[PlayerType.player4] = self.makePlayer(kwargs["player4Width"],kwargs["player4Height"], 'spaceshipGreen.jpg')
        if "mediumAsteroidWidth" in kwargs and "mediumAsteroidHeight" in kwargs: 
            self.asteroidImages[AsteroidType.medium], self.asteroidPaths[AsteroidType.medium] = self.makeAsteroid(kwargs["mediumAsteroidWidth"],kwargs["mediumAsteroidHeight"],'asteroid1.png')
        if "smallAsteroidWidth" in kwargs and "smallAsteroidHeight" in kwargs: 
            self.asteroidImages[AsteroidType.small], self.asteroidPaths[AsteroidType.small] = self.makeAsteroid(kwargs["smallAsteroidWidth"],kwargs["smallAsteroidHeight"],'asteroid1.png')
        if "speedUpWidth" in kwargs and "speedUpHeight" in kwargs:
            self.speedUpImage, self.speedUpPath = self.make_SpeedUp_FireRateSpeedUp_ExtraLife(kwargs["speedUpWidth"], kwargs["speedUpHeight"], 'flash.png')
        if "fireRateSpeedUpWidth" in kwargs and "fireRateSpeedUpHeight" in kwargs:
            self.fireRateSpeedUpImage, self.fireRateSpeedUpPath = self.make_SpeedUp_FireRateSpeedUp_ExtraLife(kwargs["fireRateSpeedUpWidth"], kwargs["fireRateSpeedUpHeight"], 'fire.png')
        if "extraLifeWidth" in kwargs and "extraLifeHeight" in kwargs:
            self.extraLifeImage, self.extraLifePath = self.make_SpeedUp_FireRateSpeedUp_ExtraLife(kwargs["extraLifeWidth"], kwargs["extraLifeHeight"], 'hart.jpg')


    def getPlayer(self,playerType : PlayerType):
        if playerType in self.playerImages and playerType in self.playerPaths:
            return self.playerImages[playerType], self.playerPaths[playerType]
        else:
            return None,None

    def getAsteroid(self,asteroidType:AsteroidType):
        if asteroidType in self.asteroidImages and asteroidType in self.asteroidPaths:
            return self.asteroidImages[asteroidType], self.asteroidPaths[asteroidType]
        else:
            return None, None

    def getSpeedUp(self):
        if self.speedUpImage is not None and self.speedUpPath is not None:
            return self.speedUpImage, self.speedUpPath

    def getFireRateSpeedUp(self):
        if self.fireRateSpeedUpImage is not None and self.fireRateSpeedUpPath is not None:
            return self.fireRateSpeedUpImage, self.fireRateSpeedUpPath

    def getExtraLife(self):
        if self.extraLifeImage is not None and self.extraLifePath is not None:
            return self.extraLifeImage, self.extraLifePath

    def makeAsteroid(self,width,height,imageName):
        img3 = QtGui.QImage(imageName)
        img4 = img3.scaledToHeight(height)
        imageAsteroid = img4.scaledToWidth(width)
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

    def make_SpeedUp_FireRateSpeedUp_ExtraLife(self, width, height, image):
        img1 = QtGui.QImage(image)
        img2 = img1.scaledToHeight(height)
        imagee = img2.scaledToWidth(width)
        imagee.convertToFormat(QtGui.QImage.Format_ARGB32)
        polygon = QtGui.QPolygonF([
            QPointF(0, 0),
            QPointF(0, height),
            QPointF(width, height),
            QPointF(width, 0)
        ])
        path = QtGui.QPainterPath()
        path.addPolygon(polygon)
        path.closeSubpath()

        return imagee, path