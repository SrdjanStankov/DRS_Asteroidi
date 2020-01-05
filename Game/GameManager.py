import GameLoop as gameLoop
from AsteroidAndPlayerTypes import AsteroidType
import Managers as mng
import time
import threading as th
from random import seed,randint
from PyQt5.QtCore import QPointF, QThread, pyqtSignal, QObject
from ScreenSides import ScreenSide

class gameStateUpdate(QObject):

    update = pyqtSignal()

    def __init__(self):
        super(gameStateUpdate, self).__init__()
        self.t = th.Thread(target=self.loop)
        self.t.start()

    def loop(self):
        while True:
            self.update.emit()
            time.sleep(1 / 150)



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
        self.currentAsteroidSpeed = 1.8
        self.asteroidsToDestroy = 0
        self.currentLevel = 0
        self.noti = gameStateUpdate()
        self.noti.update.connect(self.update)

    def asteroidAction(self,asteroidId,playerId,projectileId):
        player = mng.Managers.getInstance().objects.FindById(playerId)
        asteroid = mng.Managers.getInstance().objects.FindById(asteroidId)
        if player is not None and asteroid is not None:
            self.asteroidsToDestroy -= 1
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
        self.asteroidManager.createAsteroidSimple(type,asteroidX,asteroidY,self.currentAsteroidSpeed,randint(1,180))
        self.asteroidManager.createAsteroidSimple(type,asteroidX,asteroidY,self.currentAsteroidSpeed,randint(-180,0))


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
        self.asteroidManager.createAsteroid(ScreenSide(randint(0,3)),self.currentAsteroidSpeed)

    def startLevel(self):
        print(f"Starting level {self.currentLevel + 1}")
        self.currentLevel += 1
        self.asteroidsToDestroy = 2 * self.currentLevel + 1
        self.currentAsteroidSpeed += 0.2
        if self.currentLevel % 4 == 0:
            for item  in mng.Managers.getInstance().objects.FindObjectsOfType("Spaceship"):
                item.transform.speed += 0.2

        for _ in range(1,2 + 2 * self.currentLevel):
            self.asteroidManager.createAsteroid(ScreenSide(randint(0,3)),self.currentAsteroidSpeed)

    def update(self):
        if self.asteroidsToDestroy <= 0:
            self.startLevel()
