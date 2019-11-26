import sys
from PyQt5.QtCore import pyqtSignal, QObject
from time import sleep

class GameLoop(QObject):
    
    __instance = None
    _update = pyqtSignal()

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

    def _connect(self, obj):
        self._update.connect(obj.update)
        print("CONNECTED {}".format(obj.__class__.__name__))

    def _emit(self):
        self._update.emit()
        print("EMITED")

    def _loop(self):
        while True:
            self._update.emit()
            print("LOOP")
            sleep(1/6)


if __name__ == '__main__':
    import Application
    app = Application()
    
    print("AAAAA")
    
    sleep (3)
    print("BBBBB")

    app.stop_game_loop()