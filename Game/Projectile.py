from GameObject import GameObject
from PyQt5.QtCore import QObject
import types
import Transform as transform
import Managers as mng

class Projectile(QObject):

    def __init__(self,shooter:GameObject,gameSignal):
        super(Projectile,self).__init__()
        tempTransform = transform.Transform()
        tempTransform.x, tempTransform.y = shooter.Render.getTopCenter()
        tempTransform.rotation = shooter.transform.rotation
        tempTransform.speed = 6
        self.projectile = mng.Managers.getInstance().objects.Instantiate("Projectile",transform = tempTransform,name = shooter.Id,callable = self.update,playerType = shooter.playerType)
        self.gameSignal = gameSignal

    def update(self):
        for ind, item in enumerate(self.projectile.collisionsType):
            if item == "Asteroid":
                #try:
                    self.gameSignal.emit(self.projectile.collisions[ind],self.projectile.name,self.projectile.Id)
                #except:
                #    pass
        self.projectile.transform.move(1)
        if self.projectile.transform.x < 100 or self.projectile.transform.y < 100:
            mng.Managers.getInstance().objects.Destroy(self.projectile.Id)
            