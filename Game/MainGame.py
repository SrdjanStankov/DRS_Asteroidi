import sys
from Player import Player
from SpeedUp import SpeedUp
from PyQt5 import QtWidgets
from GameLoop import GameLoop as gl
from AsteroidAndPlayerTypes import AsteroidType
import Managers as mgr
import AsteroidManager as AsteroidManager
import ProjectileManager as ProjectileManager
from CollisionDetection import CollisionDetection
from GameManager import GameManager
from socket_send import SocketSend
from socket_listen import SocketListen
import multiprocessing as mp
from CommandMapper import CommandMapper
from time import sleep

            
# method for canceling game loop thread
def cancel():
    gl.getInstance().cancel()

class Worker(mp.Process):
    def __init__(self, pipe):
        super().__init__(target=self.worker, args=[pipe])


    def worker(self,pipe):
        while True:
            pipe.send("He he")
            sleep(1 / 60)


class Printer(mp.Process):
    def __init__(self,pipe):
        super().__init__(target=self.printer, args=[pipe])


    def printer(self,pipe):
        while True:
            print(pipe.recv())
            sleep(1 / 60)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    
    # connect app exit signal to thread stop of game loop
    app.aboutToQuit.connect(cancel)

    input = mgr.Managers.getInstance().input
    sceneManager = mgr.Managers.getInstance().scene
    sceneManager.resize(1300, 768)
    sceneManager.show()
    objectManager = mgr.Managers.getInstance().objects
    projectileManager = ProjectileManager.ProjectileManager()
    go = Player("Dejan",projectileManager)
    asteroidManager = AsteroidManager.AsteroidManager()
    collisionManager = CollisionDetection(objectManager)
    gm = GameManager(asteroidManager,projectileManager)
    projectileManager.gameSignal = gm.asteroidDestroyed
    asteroidManager.signalCollision = gm.spaceshipDestroyed
    asteroidManager.signalMapEnd = gm.asteroidEnd


    cl_in,cl_out = mp.Pipe()
    sr_in,sr_out = mp.Pipe()

    input.SetPipes(cl_in,sr_out)
    
    sender = SocketSend(cl_out).start()
    listener = SocketListen(sr_in).start()


    sys.exit(app.exec_())

