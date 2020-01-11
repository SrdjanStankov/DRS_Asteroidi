import Transform as transform
import GameObject as gameObject
import Managers as mng
from Asteroid import Asteroid
from ScreenSides import ScreenSide
from random import seed,randint
from AsteroidAndPlayerTypes import AsteroidType


class AsteroidManager(gameObject.GameObject):
    def __init__(self,asteroidSignal):
        super().__init__()
        self.asteroidSignal = asteroidSignal
        self.count = 0
        self.asteroids = []

    def createAsteroidSimple(self,type,x,y,speed,rotation):
        temp = Asteroid(type,x,y,rotation,speed,self.asteroidSignal)

    def createAsteroid(self,side : ScreenSide,speed):
        typeInt = randint(1,10)
        if typeInt < 2:
            type = AsteroidType.small
        elif typeInt < 5:
            type = AsteroidType.medium
        else:
            type = AsteroidType.large
        if side is ScreenSide.left:
            y = randint(165,818)
            if y < 321:
                angle = randint(80,160)
            else:
                angle = randint(40,100)
            self.createAsteroidSimple(type,0,y,speed,angle)
        elif side is ScreenSide.top:
            x = randint(160,1340)
            if x < 587:
                angle = randint(-300,-170)
            else:
                angle = randint(-190,-100)
            self.createAsteroidSimple(type,x,0,speed,angle)
        elif side is ScreenSide.right:
            y = randint(165,808)
            if y < 321:
                angle = randint(-160,-80)
            else:
                angle = randint(-100,-40)
            self.createAsteroidSimple(type,1420,y,speed,angle)
        else:
            x = randint(165,1340)
            if x < 587:
                angle = randint(-10,80)
            else:
                angle = randint(-70,10)
            self.createAsteroidSimple(type,x,880,speed,angle)


    def update(self):
        pass

