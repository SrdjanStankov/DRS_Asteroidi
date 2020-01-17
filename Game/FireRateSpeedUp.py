from Transform import Transform
import Managers as mgr
from GameObject import GameObject
from time import time

class FireRateSpeedUp(GameObject):

    def __init__(self, x, y):
        super(FireRateSpeedUp,self).__init__()
        tempTransform = Transform(rotation=0, speed=0, rotationSpeed=0, x=x, y=y)
        self.obj = mgr.Managers.getInstance().objects.Instantiate("FireRateSpeedUp", transform=tempTransform)
        self.expirationTime = None
        self.shipThatCollected = None
        self.collected = False
        self.durationTime = 30
        self.fireRateMultiplier = 2

    def update(self):
        if not self.collected:
            for x in self.obj.collisionsType:
                if x == "Spaceship":
                    objId = self.obj.collisions[self.obj.collisionsType.index(x)]
                    self.obj.sound.play()
                    self.shipThatCollected = mgr.Managers.getInstance().objects.FindById(objId)
                    self.shipThatCollected.shootInterval /= self.fireRateMultiplier
                    self.expirationTime = time() + self.durationTime
                    mgr.Managers.getInstance().objects.Destroy(self.obj.Id)
                    self.collected = True
                    
        
        if self.collected and (time() >= self.expirationTime):
            try:
                self.shipThatCollected.shootInterval *= self.fireRateMultiplier
            except :
                pass
            self.destroy()