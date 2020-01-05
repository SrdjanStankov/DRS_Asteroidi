from Transform import Transform
import Managers as mgr
from GameObject import GameObject

class SpeedUp(GameObject):

    def __init__(self, x, y):
        super(SpeedUp,self).__init__()
        tempTransform = Transform(rotation=0, speed=0, rotationSpeed=0, x=x, y=y)
        self.obj = mgr.Managers.getInstance().objects.Instantiate("SpeedUp", transform=tempTransform)

    def update(self):
        for x in self.obj.collisionsType:
            if x == "Spaceship":
                objId = self.obj.collisions[self.obj.collisionsType.index(x)]
                ship = mgr.Managers.getInstance().objects.FindById(objId)
                ship.transform.speed *= 2
                ship.transform.rotationSpeed *= 1.5
                mgr.Managers.getInstance().objects.Destroy(self.obj.Id)
                self.destroy()