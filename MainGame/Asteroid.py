from GameObject import GameObject
import types
import Transform as transform
import Managers as mng

class Asteroid():
    
    def __init__(self,x,y,rotation):
        tempTransform = transform.Transform()
        tempTransform.x = x
        tempTransform.y = y
        tempTransform.rotation = rotation
        tempTransform.speed = 2
        self.asteroid = mng.Managers.getInstance().objects.Instantiate("Asteroid",transform = tempTransform,name = "",callable = self.update)
        self.asteroid.Render.rotateItem()


    def update(self):
        self.asteroid.transform.move(1)
