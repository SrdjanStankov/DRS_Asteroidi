import sys
from Player import Player
from PyQt5 import QtWidgets
from GameLoop import GameLoop as gl

import Managers as mgr
import AsteroidManager as AsteroidManager
import ProjectileManager as ProjectileManager
import socket_send
import socket_listen
import multiprocessing

# method for canceling game loop thread
def cancel():
    gl.getInstance().cancel()

def socketListen():
    socket_listen.SocketListen().Listen()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    
    # connect app exit signal to thread stop of game loop
    app.aboutToQuit.connect(cancel)

    input = mgr.Managers.getInstance().input
    sceneManager = mgr.Managers.getInstance().scene
    sceneManager.resize(1300, 700)
    sceneManager.show()
    objectManager = mgr.Managers.getInstance().objects
    projectileManager = ProjectileManager.ProjectileManager()
    go = Player(projectileManager)
    asteroidManager = AsteroidManager.AsteroidManager()
    for i in range(1,30):
        asteroidManager.createAsteroid(100 + 50 * i,0,5)

    multiprocessing.Process(target=socketListen).start()
    socket_send.SocketSend().Send('Hello world š đ č ć ž Здраво Свете')

    sys.exit(app.exec_())