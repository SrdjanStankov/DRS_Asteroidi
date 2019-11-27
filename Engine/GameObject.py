from GameLoop import GameLoopManager
import multiprocessing as mp


class GameObject():

    def __init__(self, *args, **kwargs):
        #GameLoopManager.getInstance().q.put(self.update)
        print("GO: ", args[0])
        print("GAME OBJECT INITIALIZED")

    def update(self):
        print("GAME OBJECT UPDATE")
        print("GameObject update: ", mp.current_process().name)
        

class ConcreteObject(GameObject):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print("CONCRETE OBJECT INITIALIZED")

    def update(self):
        print("CONCRETE OBJECT UPDATE")
        print("ConcreteObject update: ", mp.current_process().name)
