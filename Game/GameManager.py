import GameLoop as gameLoop
from AsteroidAndPlayerTypes import AsteroidType
import Managers as mng
import time
import threading as th
from Player import Player
from random import seed,randint
from PyQt5.QtCore import QPointF, QThread, pyqtSignal, QObject
from ScreenSides import ScreenSide
from AsteroidManager import AsteroidManager
from ProjectileManager import ProjectileManager

class gameStateUpdate(QObject):

    update = pyqtSignal()

    def __init__(self):
        super(gameStateUpdate, self).__init__()
        self.t = th.Thread(target=self.loop)
        self.t.start()

    def loop(self):
        while True:
            if gameLoop.GameLoop.getInstance()._cancelation_token==True:
                break
            self.update.emit()
            time.sleep(4)



class GameManager(QObject):
    asteroidDestroyed = pyqtSignal(int,int,int)
    spaceshipDestroyed = pyqtSignal(int)
    def __init__(self):
        super(GameManager,self).__init__()
        self.asteroidManager = AsteroidManager(self.spaceshipDestroyed)
        self.projectileManager = ProjectileManager(self.asteroidDestroyed)
        self.player = Player("Dejan",self.projectileManager)
        self.asteroidDestroyed.connect(self.asteroidAction)
        self.spaceshipDestroyed.connect(self.spaceshipAction)
        self.currentAsteroidSpeed = 1.8
        self.asteroidsToDestroy = 0
        self.currentLevel = 0
        self.noti = gameStateUpdate()
        self.noti.update.connect(self.update)
        self.lock = th.Lock()

    def asteroidAction(self,asteroidId,playerId,projectileId):
        player = mng.Managers.getInstance().objects.FindById(playerId)
        asteroid = mng.Managers.getInstance().objects.FindById(asteroidId)
        if player is not None and asteroid is not None:
            self.lock.acquire()
            self.asteroidsToDestroy -= 1
            self.lock.release()
            mng.Managers.getInstance().objects.Destroy(projectileId)
            x = asteroid.transform.x
            y = asteroid.transform.y
            type = asteroid.asteroidType
            mng.Managers.getInstance().objects.Destroy(asteroidId)
            if type is AsteroidType.large:
                player.points += 100
                self.createSmallerAsteroids(x,y,AsteroidType.medium)
                self.lock.acquire()
                self.asteroidsToDestroy += 2
                self.lock.release()
            elif type is AsteroidType.medium:
                player.points += 150
                self.createSmallerAsteroids(x,y,AsteroidType.small)
                self.lock.acquire()
                self.asteroidsToDestroy += 2
                self.lock.release()
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
                    player.transform.x = 750
                    player.transform.y = 500
                    player.lives -= 1
                else:
                    mng.Managers.getInstance().objects.Destroy(playerId)

    def startLevel(self):
        print(f"Starting level {self.currentLevel + 1}")
        self.lock.acquire()
        self.currentLevel += 1
        self.asteroidsToDestroy = 2 * self.currentLevel + 1
        self.currentAsteroidSpeed += 0.2
        self.lock.release()
        if self.currentLevel % 4 == 0:
            for item  in mng.Managers.getInstance().objects.FindObjectsOfType("Spaceship"):
                item.transform.speed += 0.2

        for _ in range(1,2 + 2 * self.currentLevel):
            self.asteroidManager.createAsteroid(ScreenSide(randint(0,3)),self.currentAsteroidSpeed)

    def update(self):
        if len(mng.Managers.getInstance().objects.FindObjectsOfType("Spaceship")) > 0:
            if self.asteroidsToDestroy <= 0:
                self.startLevel()
        else:
            pass # game over logika
