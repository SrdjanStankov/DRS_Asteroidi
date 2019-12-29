import GameObject as gameObject
import Managers as mng
import threading
import Transform as transform

class ProjectileBeh(gameObject.GameObject):
    def __init__(self,go):
        super().__init__()
        self.projectile = go

    def update(self):
        if self.projectile.transform.x >= 1280 or self.projectile.transform.y >= 680 :
            mng.Managers.getInstance().objects.Destroy(self.projectile.Id)
        else:
            self.projectile.transform.move(1)
            self.projectile.Render.moveItem()


class ProjectileManager(gameObject.GameObject):
    def __init__(self):
        super().__init__()
        print("ProjectileManager init--->{}".format(threading.currentThread()))

        self.projectiles = []

    def createProjectile(self,shooter:gameObject.GameObject):
        topLeft = shooter.Render.getTopLeft()
        topRight = shooter.Render.getTopRight()
        tempTransform = transform.Transform()
        tempTransform.x = (topLeft.x() + topRight.x()) / 2
        tempTransform.y = (topLeft.y() + topRight.y()) / 2
        tempTransform.rotation = shooter.transform.rotation
        tempTransform.speed = 6
        temp = mng.Managers.getInstance().objects.Instantiate("Projectile",transform = tempTransform,name = shooter.name)
        temp.projectileBehaviour = ProjectileBeh(temp)
        self.projectiles.append(temp)

    def update(self):
        pass
        