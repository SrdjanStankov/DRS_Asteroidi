import Transform as transform
import GameObject as gameObject
import Managers as mng
from Asteroid import Asteroid

class AsteroidBeh():
    def __init__(self, go):
        self.asteroid = go
        self.asteroid.Render.rotateItem()
    
    def update(self):
        self.asteroid.transform.speed=5
        self.asteroid.transform.move(1)
        self.asteroid.Render.moveItem()
        for item in self.asteroid.collisionsType:
            if item == "Projectile":
                try:
                    mng.Managers.getInstance().objects.Destroy(self.asteroid.Id)
                except:
                    pass

class AsteroidManager(gameObject.GameObject):
    def __init__(self):
        super().__init__()

        self.count = 0
        self.asteroids = []

    def createAsteroid(self,x,y,rotation):
        temp = Asteroid(x,y,rotation)

    def update(self):
        pass

