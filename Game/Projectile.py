from GameObject import GameObject
from PyQt5.QtCore import QObject
import types
import Transform as transform
import Managers as mng

class Projectile(QObject):

    def __init__(self,shooter:GameObject,gameSignal):
        super(Projectile,self).__init__()
        topLeft = shooter.Render.getTopLeft()
        topRight = shooter.Render.getTopRight()
        tempTransform = transform.Transform()
        tempTransform.x = (topLeft.x() + topRight.x()) / 2
        tempTransform.y = (topLeft.y() + topRight.y()) / 2
        tempTransform.rotation = shooter.transform.rotation
        tempTransform.speed = 6
        self.projectile = mng.Managers.getInstance().objects.Instantiate("Projectile",transform = tempTransform,name = shooter.Id,callable = self.update)
        self.gameSignal = gameSignal

    def update(self):
        for ind, item in enumerate(self.projectile.collisionsType):
            if item == "Asteroid":
                #try:
                    self.gameSignal.emit(self.projectile.collisions[ind],self.projectile.name,self.projectile.Id)
                #except:
                #    pass
        if self.projectile.transform.x >= 1280 or self.projectile.transform.y >= 680 :
            mng.Managers.getInstance().objects.Destroy(self.projectile.Id)
        else:
            self.projectile.transform.move(1)