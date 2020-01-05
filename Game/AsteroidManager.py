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

    def createAsteroidSimple(self,type,x,y,rotation):
        temp = Asteroid(type,x,y,rotation,self.signalCollision,self.signalMapEnd)

    def createAsteroid(self,side : ScreenSide):
        if side is ScreenSide.left:
            y = randint(50,718)
            if y < 334:
                angle = randint(80,160)
            else:
                angle = randint(40,100)
            self.createAsteroidSimple(AsteroidType(randint(0,2)),-60,y,angle)
        elif side is ScreenSide.top:
            x = randint(50,1250)
            if x < 600:
                angle = randint(-300,-170)
            else:
                angle = randint(-190,-100)
            self.createAsteroidSimple(AsteroidType(randint(0,2)),x,-60,angle)
        elif side is ScreenSide.right:
            y = randint(50,718)
            if y < 334:
                angle = randint(-160,-80)
            else:
                angle = randint(-100,-40)
            self.createAsteroidSimple(AsteroidType(randint(0,2)),1360,y,angle)
        else:
            x = randint(50,1250)
            if x < 600:
                angle = randint(-10,80)
            else:
                angle = randint(-70,10)
            self.createAsteroidSimple(AsteroidType(randint(0,2)),x,858,angle)


    def update(self):
        pass

