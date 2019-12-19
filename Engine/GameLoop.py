from time import sleep
from Signal import Signal
import threading as tread

class GameLoop():
    
    """
    Primary Game Loop class
    
    DO NOT USE ATTRIBUTES ON YOUR OWN!
    USE METHODS INSTEAD!
    """

    __instance = None
    _update_signal = Signal()
    _cancelation_token = False

    @staticmethod
    def getInstance():
        """Gets instance of GameLoop class. GameLoop is a singleton."""
        if GameLoop.__instance==None:
            GameLoop()
        return GameLoop.__instance

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(GameLoop, cls).__new__(cls)
            cls.__instance._start_loop()
        return cls.__instance

    def connect_to_update(self, method):
        """Use this method to connect your method to primary game loop"""
        self._update_signal.connect(method)

    def _start_loop(self):
        """
        Starts the game loop.
        Not necessary to start it yourself.
        It starts automatically on class creation.
        """
        self.p = tread.Thread(target=self._loop)
        self.p.start()

    def cancel(self):
        """
        Stops Game Loop.
        After this is called you will need to manualy call the _start_loop() method to restart the Game Loop.
        """
        GameLoop.getInstance()._cancelation_token = True

    def _loop(self):
        """Do not call this method!"""
        while True:
            if GameLoop.getInstance()._cancelation_token==True:
                break
            self._update_signal.notify_all()
            sleep(1/100)
