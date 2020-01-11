from GameObject import GameObject
from PyQt5.QtCore import QObject
import types
import Transform as transform
import Managers as mng

class Asteroid(QObject):

    def __init__(self,type,x,y,rotation,speed,signalCollision):
        super(Asteroid,self).__init__()
        tempTransform = transform.Transform()
        tempTransform.x = x
        tempTransform.y = y
        tempTransform.rotation = rotation
        tempTransform.speed = speed
        self.asteroid = mng.Managers.getInstance().objects.Instantiate("Asteroid",asteroidType = type,transform = tempTransform,name = "",callable = self.update)
        self.asteroid.Render.rotateItem()
        self.signalCollision = signalCollision


    def update(self):
        try:
            self.asteroid.transform.move(1)
            for ind,item in enumerate(self.asteroid.collisionsType):
                if item == "Spaceship":
                    self.signalCollision.emit(self.asteroid.collisions[ind])
        except:
            pass
