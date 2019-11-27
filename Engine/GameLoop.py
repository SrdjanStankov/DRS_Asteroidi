from time import sleep
from Signal import Signal
import multiprocessing as mp
import queue

class GameLoop():
    
    __instance = None
    _update_signal = Signal()
    q = mp.Queue()

    @staticmethod
    def getInstance():
        if GameLoop.__instance == None:
            GameLoop()
        return GameLoop.__instance

    def __init__():
        pass

    def __init__(self):
      if GameLoop.__instance != None:
         raise Exception("This class is a singleton!")
      else:
         super().__init__()
         GameLoop.__instance = self
         #print("GameLoop: ", mp.current_process().name)

    def _connect(self):
        method = self.q.get(block = True)
        self._update_signal.connect(method)
        print("CONNECTED {}".format(method.__name__))

    def _start_loop(self):
        self.p = mp.Process(target=self._loop)
        self.p.start()

    def _loop(self, que):
        print("lop:", que)
        i = 0
        while i < 10:
            try:
                method = que.get(block = True)
                self._update_signal.connect(method)
            except queue.Empty:
                print("Except Empty")
            self._update_signal.notify_all()
            print("LOOP")
            print("GameLoop _loop: ", mp.current_process().name)
            sleep(1 / 6)
            i += 1


class GameLoopManager():

    __instance = None
    #q = mp.Queue()

    @staticmethod
    def getInstance():
        if GameLoopManager.__instance == None:
            GameLoopManager()
        return GameLoopManager.__instance

    def __init__():
        pass

    def __init__(self):
        if GameLoopManager.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            GameLoopManager.__instance = self

    def aaa(self, que):
        print("Manager aaa: ", mp.current_process().name)
        print("aaa:", que)
        self.p = mp.Process(target = self.bbb, args=[que])
        self.p.start()

    def bbb(self, que):
        sleep(1)
        print("bbb:", que)
        #print("Manager bbb:", mp.current_process().name)
        self.gl = GameLoop.getInstance()
        self.gl._loop(que)

    def connect(self, mtd):
        self.gl._connect(mtd)


if __name__ == '__main__':
    from GameObject import ConcreteObject
    q = mp.Queue()

    gm = GameLoopManager.getInstance()
    gm.aaa(q)
    sleep(2)
    #gl = GameLoop.getInstance()

    go = ConcreteObject(q)
    #go = ConcreteObject()
    #go = ConcreteObject()

    #gl._start_loop()
    
    sleep(3)
    print("End")