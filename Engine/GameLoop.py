from time import sleep
from Signal import Signal
import threading as tread

class GameLoop():
    
    __instance = None
    _update_signal = Signal()
    _cancelation_token = False

    @staticmethod
    def getInstance():
        if GameLoop.__instance==None:
            GameLoop()
        return GameLoop.__instance

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(GameLoop, cls).__new__(cls)
            cls.__instance.start_loop()
        return cls.__instance

    def connect_to_update(self, method):
        self._update_signal.connect(method)

    def start_loop(self):
        self.p = tread.Thread(target=self._loop)
        self.p.start()

    def cancel(self):
        GameLoop.getInstance()._cancelation_token = True

    def _loop(self):
        while True:
            if GameLoop.getInstance()._cancelation_token==True:
                break
            self._update_signal.notify_all()
            sleep(1/6)