from Transform import Transform
import Managers as mgr
from GameObject import GameObject

class ExtraLife(GameObject):

    def __init__(self, x, y):
        super(ExtraLife,self).__init__()
        tempTransform = Transform(rotation=0, speed=0, rotationSpeed=0, x=x, y=y)
        self.obj = mgr.Managers.getInstance().objects.Instantiate("ExtraLife", transform=tempTransform)
        self.shipThatCollected = None

    def update(self):
        for x in self.obj.collisionsType:
            if x == "Spaceship":
                objId = self.obj.collisions[self.obj.collisionsType.index(x)]
                self.shipThatCollected = mgr.Managers.getInstance().objects.FindById(objId)
                self.shipThatCollected.lives += 1
                mgr.Managers.getInstance().objects.Destroy(self.obj.Id)
                self.destroy()