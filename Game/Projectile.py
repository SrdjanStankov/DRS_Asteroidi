from GameObject import GameObject
import types
import Transform as transform
import Managers as mng

class Projectile():
    
    def __init__(self,shooter:GameObject):
        topLeft = shooter.Render.getTopLeft()
        topRight = shooter.Render.getTopRight()
        tempTransform = transform.Transform()
        tempTransform.x = (topLeft.x() + topRight.x()) / 2
        tempTransform.y = (topLeft.y() + topRight.y()) / 2
        tempTransform.rotation = shooter.transform.rotation
        tempTransform.speed = 6
        self.projectile = mng.Managers.getInstance().objects.Instantiate("Projectile",transform = tempTransform,name = shooter.name,callable = self.update)
        self.projectile.update = self.update

    def update(self):
        if self.projectile.transform.x >= 1280 or self.projectile.transform.y >= 680 :
            mng.Managers.getInstance().objects.Destroy(self.projectile.Id)
        else:
            self.projectile.transform.move(1)
