import Transform as transform
import GameObject as gameObject
import Managers as mng
from Asteroid import Asteroid


class AsteroidManager(gameObject.GameObject):
    def __init__(self):
        super().__init__()

        self.count = 0
        self.asteroids = []

    def createAsteroid(self,x,y,rotation):
        temp = Asteroid(x,y,rotation,self.gameSignal)

    def update(self):
        pass

