import GameLoop as gameLoop
from AsteroidAndPlayerTypes import AsteroidType
import Managers as mng
import time
from random import seed,randint
from PyQt5.QtCore import QPointF, QThread, pyqtSignal, QObject
from ScreenSides import ScreenSide




class GameManager(QObject):
    asteroidDestroyed = pyqtSignal(int,int,int)
    spaceshipDestroyed = pyqtSignal(int)
    asteroidEnd = pyqtSignal()
    def __init__(self,asteroidManager,projectileManager):
        super(GameManager,self).__init__()
        self.asteroidManager = asteroidManager
        self.projectileManager = projectileManager
        self.asteroidDestroyed.connect(self.asteroidAction)
        self.spaceshipDestroyed.connect(self.spaceshipAction)
        self.asteroidEnd.connect(self.asteroidEndAction)

    def asteroidAction(self,asteroidId,playerId,projectileId):
        player = mng.Managers.getInstance().objects.FindById(playerId)
        asteroid = mng.Managers.getInstance().objects.FindById(asteroidId)
        if player is not None and asteroid is not None:
            mng.Managers.getInstance().objects.Destroy(projectileId)
            x = asteroid.transform.x
            y = asteroid.transform.y
            type = asteroid.asteroidType
            mng.Managers.getInstance().objects.Destroy(asteroidId)
            if type is AsteroidType.large:
                player.points += 100
                self.createSmallerAsteroids(x,y,AsteroidType.medium)
            elif type is AsteroidType.medium:
                player.points += 150
                self.createSmallerAsteroids(x,y,AsteroidType.small)
            else:
                player.points += 200


    def createSmallerAsteroids(self,x,y,type: AsteroidType):
        asteroidX = x
        asteroidY = y
        self.asteroidManager.createAsteroidSimple(type,asteroidX,asteroidY,randint(1,180))
        self.asteroidManager.createAsteroidSimple(type,asteroidX,asteroidY,randint(-180,0))


    def spaceshipAction(self,playerId):
        player = mng.Managers.getInstance().objects.FindById(playerId)
        if player is not None:
            if time.time() > player.nextAliveTime:
                player.nextAliveTime = time.time() + player.invulnerableTime
                if player.lives > 1:
                    player.transform.x = 1000
                    player.transform.y = 450
                    player.lives -= 1
                else:
                    mng.Managers.getInstance().objects.Destroy(playerId)

    def asteroidEndAction(self):
        self.asteroidManager.createAsteroid(ScreenSide(randint(0,3)))



        
