import Transform as transform
import GameObject as gameObject
from Asteroid import Asteroid
import Managers as mng

class AsteroidBeh():
    def __init__(self, go):
        self.asteroid = go
        self.asteroid.Render.rotateItem()
    
    def update(self):
        #if self.asteroid.active == False:
        #    return
        self.asteroid.transform.speed=5
        self.asteroid.transform.move(1)

class AsteroidManager(gameObject.GameObject):
    def __init__(self):
        super().__init__()
      #  print("AsteroidManager init--->{}".format(threading.currentThread()))

        self.count = 0
        self.asteroids = []

    def createAsteroid(self,x,y,rotation):
        temp = Asteroid(x,y,rotation)
        #self.asteroids.append(temp)

    def update(self):
        pass