import ObjectFactory as factory
import SceneManager
<<<<<<< HEAD
import threading as th
import GameLoop as gl
=======
#import Transform
>>>>>>> 3780d3175f76cb3788ed53f1e3c3dab9e30ad68f
from PyQt5.QtCore import pyqtSignal, QObject
# Responsible for creating , accessing and destroying objects
class ObjectManager(QObject):

    #instansiateSignal = pyqtSignal(object)

    #SpaceshipPool = []
    #AsteroidsPool = []
    #ProjectilesPool = []
    Pool = []
    def __init__(self,SceneManager: SceneManager):
        super(ObjectManager, self).__init__()
        
        self.id = 0
        self.SceneManager = SceneManager
        self.factory = factory.ObjectFactory(SceneManager)

        #for _ in range(100):
        #    self._internalInstantiate("Asteroid", transform = Transform.Transform(x = -100, y = -100), name = "")
        #for _ in range(200):
        #    self._internalInstantiate("Projectile", transform = Transform.Transform(x = -100, y = -100), name = "")
        #for _ in range(1):
        #    self._internalInstantiate("Spaceship", transform = Transform.Transform(x = -100, y = -100), name = "")

    #def _internalInstantiate(self, type, **kwargs):
    #    #print("Instantiate")
    #    go = self.factory.Create(type,**kwargs)
    #    go.Id = self.id
    #    go.active = False
    #    #go.Render.beh = AsteroidBeh(go)
    #    self.id += 1 
    #    if type == "Asteroid":
    #        self.AsteroidsPool.append(go)
    #    elif type == "Projectile":
    #        self.ProjectilesPool.append(go)
    #    else:
    #        self.SpaceshipPool.append(go)
    #    #self.instantiatedObjects.append(go)
    #    return go

    def Instantiate(self, type,**kwargs):
        go = self.factory.Create(type, **kwargs)
        go.Id = self.id
        self.id += 1
        self.Pool.append(go)
        return go
        # nadji neaktivan objekat iz odgovarajuceg poola
        #go = self.FindByActive(type)
        ## postavi ga da bude aktivan
        #go.active = True
        ## postavi mu odgovarajuca polja
        #try:
        #    go.name = kwargs["name"]
        #except :
        #    pass
        #try:
        #    go.transform = kwargs["transform"]
        #except:
        #    pass
        ## vrat taj objekat
        #return go

    #def FindByActive(self, type):
    #    if type == "Asteroid":
    #        for g in self.AsteroidsPool:
    #            if g.active == False:
    #                return g
    #    elif type == "Projectile":
    #        for g in self.ProjectilesPool:
    #            if g.active == False:
    #                return g
    #    else:
    #        for g in self.SpaceshipPool:
    #            if g.active == False:
    #                return g

    # Always check is returned value different from NonType
    def FindById(self, id):
        #print("FindById")
        for i in self.Pool:
            if i.Id == id:
                return i
        #for i in self.AsteroidsPool:
        #    if i.Id == id:
        #        return i
        #for i in self.ProjectilesPool:
        #    if i.Id == id:
        #        return i
        #for i in self.SpaceshipPool:
        #    if i.Id == id:
        #        return i

    # Always check is returned value different from NoneType
    def FindObjectsOfType(self, type):
        #print("Find by name")
        self.result = []
        for i in self.Pool:
            if i.Type == type:
                self.result.append(i)

        return self.result
        #if type == "Asteroid":
        #    return self.AsteroidsPool
        #elif type == "Projectile":
        #    return self.ProjectilesPool
        #else:
        #    return self.SpaceshipPool

    #def _intarnalDestroy(self,id):
    #    temp = self.FindById(id)
    #    if temp != None:
    #        self.SceneManager.scene.removeItem(temp.Render) 
    #        if temp.Type == "Asteroid":
    #            self.AsteroidsPool.remove(temp)
    #        elif temp.Type == "Projectile":
    #            self.ProjectilesPool.remove(temp)
    #        else:
    #            self.SpaceshipPool.remove(temp)
    #    else:
    #        print(f"Object with id {self.id} not found.")
    
    def Destroy(self,id):
        temp = self.FindById(id)
<<<<<<< HEAD
        if temp is not None:
            self.SceneManager.scene.removeItem(temp.Render) 
            gl.GameLoop.getInstance().disconnect_from_update(temp.callable)
=======
        if temp != None:
            self.SceneManager.scene.removeItem(temp.Render)
>>>>>>> 3780d3175f76cb3788ed53f1e3c3dab9e30ad68f
            self.Pool.remove(temp)
            #temp.active = False
            #temp.transform = Transform.Transform(x = -100, y = -100)
            #print("")
        else:
            print(f"Object with id {self.id} not found.")
