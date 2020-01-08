from Transform import Transform
import Managers as mgr
from GameObject import GameObject
from time import time

class SpeedUp(GameObject):

    def __init__(self, x, y):
        super(SpeedUp,self).__init__()
        tempTransform = Transform(rotation=0, speed=0, rotationSpeed=0, x=x, y=y)
        self.obj = mgr.Managers.getInstance().objects.Instantiate("SpeedUp", transform=tempTransform)
        self.expirationTime = None
        self.shipThatCollected = None
        self.collected = False
        self.durationTime = 30
        self.speedMultiplier = 2
        self.rotationMultiplier = 1.5

    def update(self):
        if not self.collected:
            for x in self.obj.collisionsType:
                if x == "Spaceship":
                    objId = self.obj.collisions[self.obj.collisionsType.index(x)]
                    self.shipThatCollected = mgr.Managers.getInstance().objects.FindById(objId)
                    self.shipThatCollected.transform.speed *= self.speedMultiplier
                    self.shipThatCollected.transform.rotationSpeed *= self.rotationMultiplier
                    self.expirationTime = time() + self.durationTime
                    mgr.Managers.getInstance().objects.Destroy(self.obj.Id)
                    self.collected = True
                    print("colected")
        
        if self.collected and (time() >= self.expirationTime):
            try:
                self.shipThatCollected.transform.speed /= self.speedMultiplier
                self.shipThatCollected.transform.rotationSpeed /= self.rotationMultiplier
            except :
                pass
            self.destroy()