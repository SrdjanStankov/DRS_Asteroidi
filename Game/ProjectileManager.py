import GameObject as gameObject
import Managers as mng
import Transform as transform
from Projectile import Projectile


class ProjectileManager(gameObject.GameObject):
    def __init__(self,projectileSignal):
        super().__init__()
        self.projectileSignal = projectileSignal
        self.projectiles = []

    def createProjectile(self,shooter:gameObject.GameObject):
        temp = Projectile(shooter,self.projectileSignal)

    def update(self):
        pass
        