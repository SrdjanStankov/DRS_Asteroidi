import GameLoop as gameLoop
from AsteroidAndPlayerTypes import AsteroidType
import Managers as mng
from random import seed,randint
from PyQt5.QtCore import QPointF, QThread, pyqtSignal, QObject


class GameManager(QObject):
    asteroidDestroyed = pyqtSignal(int,int,int)
    spaceshipDestroyed = pyqtSignal(int)

    def __init__(self,asteroidManager,projectileManager):
        super(GameManager,self).__init__()
        self.asteroidManager = asteroidManager
        self.projectileManager = projectileManager
        self.asteroidDestroyed.connect(self.asteroidAction)
        self.spaceshipDestroyed.connect(self.spaceshipAction)

    def asteroidAction(self,asteroidId,playerId,projectileId):
        player = mng.Managers.getInstance().objects.FindById(playerId)
        asteroid = mng.Managers.getInstance().objects.FindById(asteroidId)
        if player is not None and asteroid is not None:
            mng.Managers.getInstance().objects.Destroy(projectileId)
            if asteroid.asteroidType is AsteroidType.large:
                player.points += 50
            elif asteroid.asteroidType is AsteroidType.medium:
                player.points += 75
            else:
                player.points += 100
            asteroidX = asteroid.transform.x
            asteroidY = asteroid.transform.y
            mng.Managers.getInstance().objects.Destroy(asteroidId)
            seed(1)
            self.asteroidManager.createAsteroid(asteroidX,asteroidY,randint(1,180))
            self.asteroidManager.createAsteroid(asteroidX,asteroidY,randint(-180,0))

    def spaceshipAction(self,playerId):
        player = mng.Managers.getInstance().objects.FindById(playerId)
        if player is not None:
            if player.lives > 1:
                player.transform.x = 1000
                player.transform.y = 450
                player.lives -= 1
            else:
                mng.Managers.getInstance().objects.Destroy(playerId)



        
