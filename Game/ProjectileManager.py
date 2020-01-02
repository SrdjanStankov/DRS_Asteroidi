import GameObject as gameObject
import Managers as mng
import threading
import Transform as transform
from Projectile import Projectile

class ProjectileBeh():
    def __init__(self,go):
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
        temp = Projectile(shooter)
        #self.projectiles.append(temp)

    def update(self):
        pass
        