import ObjectFactory as factory
import SceneManager
# Responsible for creating , accessing and destroying objects
class ObjectManager:

    Pool = []
    def __init__(self,SceneManager: SceneManager):
        self.id = 0
        self.SceneManager = SceneManager
        self.factory = factory.ObjectFactory(SceneManager)


    def Instantiate(self, type):
        #print("Instantiate")
        go = self.factory.Create(type)
        go.Id = self.id
        self.id += 1 
        self.Pool.append(go)
        return go

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
            print(f"Object with if {id} not found.")