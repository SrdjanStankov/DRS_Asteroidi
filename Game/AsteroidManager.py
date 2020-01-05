import Transform as transform
import GameObject as gameObject
import Managers as mng
from Asteroid import Asteroid
from ScreenSides import ScreenSide
from random import seed,randint
from AsteroidAndPlayerTypes import AsteroidType


class AsteroidManager(gameObject.GameObject):
    def __init__(self):
        super().__init__()

        self.count = 0
        self.asteroids = []

    def createAsteroidSimple(self,type,x,y,speed,rotation):
        temp = Asteroid(type,x,y,rotation,speed,self.signalCollision,self.signalMapEnd)

    def createAsteroid(self,side : ScreenSide,speed):
        if side is ScreenSide.left:
            y = randint(50,718)
            if y < 334:
                angle = randint(80,160)
            else:
                angle = randint(40,100)
            self.createAsteroidSimple(AsteroidType(randint(0,2)),-100,y,speed,angle)
        elif side is ScreenSide.top:
            x = randint(50,1250)
            if x < 600:
                angle = randint(-300,-170)
            else:
                angle = randint(-190,-100)
            self.createAsteroidSimple(AsteroidType(randint(0,2)),x,-100,speed,angle)
        elif side is ScreenSide.right:
            y = randint(50,718)
            if y < 334:
                angle = randint(-160,-80)
            else:
                angle = randint(-100,-40)
            self.createAsteroidSimple(AsteroidType(randint(0,2)),1400,y,speed,angle)
        else:
            x = randint(50,1250)
            if x < 600:
                angle = randint(-10,80)
            else:
                angle = randint(-70,10)
            self.createAsteroidSimple(AsteroidType(randint(0,2)),x,868,speed,angle)


    def update(self):
        pass

