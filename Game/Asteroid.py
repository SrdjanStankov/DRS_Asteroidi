from GameObject import GameObject
from PyQt5.QtCore import QObject
import types
import Transform as transform
import Managers as mng

class Asteroid():

    def __init__(self,x,y,rotation,gameSignal):
        super(Asteroid,self).__init__()
        tempTransform = transform.Transform()
        tempTransform.x = x
        tempTransform.y = y
        tempTransform.rotation = rotation
        tempTransform.speed = 2
        self.asteroid = mng.Managers.getInstance().objects.Instantiate("Asteroid",transform = tempTransform,name = "",callable = self.update)
        self.asteroid.Render.rotateItem()
        self.gameSignal = gameSignal


    def update(self):
        self.asteroid.transform.move(1)
        for ind,item in enumerate(self.asteroid.collisionsType):
            if item == "Spaceship":
                #try:
                    self.gameSignal.emit(self.asteroid.collisions[ind])
                #except:
                #    pass