import ObjectFactory as factory
import SceneManager
import threading as th
from PyQt5.QtCore import pyqtSignal, QObject
# Responsible for creating , accessing and destroying objects
class ObjectManager(QObject):

    instansiateSignal = pyqtSignal(object)
    instantiatedObjects = []

    Pool = []
    def __init__(self,SceneManager: SceneManager):
        super(ObjectManager, self).__init__()
        
        self.id = 0
        self.SceneManager = SceneManager
        self.factory = factory.ObjectFactory(SceneManager)
        self.instansiateSignal.connect(self.Instantiate)


    def Instantiate(self, type,**kwargs):
        
        #print("Instantiate")
        go = self.factory.Create(type,**kwargs)
        go.Id = self.id
        self.id += 1 
        self.Pool.append(go)
        self.instantiatedObjects.append(go)
        return go

    def GetInstantiatedObject(self):
        try:
            return self.instantiatedObjects[0]
        except:
            pass

    # Always check is returned value different from NonType
    def FindById(self, id):
        #print("FindById")
        for i in self.Pool:
            if i.Id == id:
                return i

    # Always check is returned value different from NoneType
    def FindObjectsOfType(self, type):
        #print("Find by name")
        self.result = []
        for i in self.Pool:
            if i.Type == type:
                self.result.append(i)

        return self.result

    def Destroy(self,id):
        temp = self.FindById(id)
        if temp != None:
            self.SceneManager.scene.removeItem(temp.Render) 
            self.Pool.remove(temp)
        else:
            pass
            #print(f"Object with id {self.id} not found.")