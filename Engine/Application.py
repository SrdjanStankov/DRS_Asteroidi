import GameLoop as loop
import multiprocessing as mp
from time import sleep
import GameObject as gameobject

class Application():

    gl = loop.GameLoop.getInstance()

    def __init__(self, *args, **kwargs):
        self.p = mp.Process(target=self._start_game_loop, daemon = True)
        print("APP INITIALIZE")

    def start(self):
        self.p.start()
        print("STARTED")

    def stop(self):
        self._stop_game_loop()
        print("STOPED")


    def _start_game_loop(self):
        self.gl._loop()
        print("GAMELOOP STARTED")

    def _stop_game_loop(self):
        self.p.terminate()
        print("GAMELOOP STOPED")

if __name__ == '__main__':

    app = Application()
    app.start();
    
    o = gameobject.ConcreteObject()
    
    print("BEFORE SLEEP")
    sleep(3)
    print("AFTER SLEEP")

    app.stop()