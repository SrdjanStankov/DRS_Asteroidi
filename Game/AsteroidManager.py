import Transform as transform
import GameObject as gameObject

import Managers as mng

class AsteroidBeh():
    def __init__(self, go):
        self.asteroid = go
        self.asteroid.Render.rotateItem()
    
    def update(self):
        #if self.asteroid.active == False:
        #    return
        self.asteroid.transform.speed=5
        self.asteroid.transform.move(1)
        self.asteroid.Render.moveItem()

class AsteroidManager(gameObject.GameObject):
    def __init__(self):
        super().__init__()
      #  print("AsteroidManager init--->{}".format(threading.currentThread()))

        self.count = 0
        self.asteroids = []

    def createAsteroid(self,x,y,rotation):
        tempTransform = transform.Transform()
        tempTransform.x = x
        tempTransform.y = y
        tempTransform.rotation = rotation
        tempTransform.speed = 2
        temp = mng.Managers.getInstance().objects.Instantiate("Asteroid",transform = tempTransform,name = "")
        temp.Render.beh = AsteroidBeh(temp)
        self.asteroids.append(temp)

    def update(self):
        pass