import sys
from PyQt5.QtCore import pyqtSignal, QObject
from time import sleep
from Signal import Signal

class GameLoop(QObject):
    
    __instance = None
    _update_signal = Signal()

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

    def _connect(self, method):
        self._update_signal.connect(method)
        print("CONNECTED {}".format(method.__name__))

    def _loop(self):
        while True:
            self._update_signal.notify_all()
            print("LOOP")
            sleep(1/6)


if __name__ == '__main__':
    from GameObject import ConcreteObject

    gl = GameLoop.getInstance()
    go = ConcreteObject()
    go = ConcreteObject()
    go = ConcreteObject()

    gl._loop()
    
    sleep (3)
    print("BBBBB")