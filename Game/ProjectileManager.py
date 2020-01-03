import GameObject as gameObject
import Managers as mng
import Transform as transform
from Projectile import Projectile


class ProjectileManager(gameObject.GameObject):
    def __init__(self):
        super().__init__()

        self.projectiles = []

    def createProjectile(self,shooter:gameObject.GameObject):
        temp = Projectile(shooter)

    def update(self):
        pass
        