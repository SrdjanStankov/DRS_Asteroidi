import sys
from Player import Player
from PyQt5 import QtWidgets
from GameLoop import GameLoop as gl

import Managers as mgr
import AsteroidManager as AsteroidManager
import ProjectileManager as ProjectileManager
from CollisionDetection import CollisionDetection
            
# method for canceling game loop thread
def cancel():
    gl.getInstance().cancel()
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
    go = Player("Dejan",projectileManager)
    asteroidManager = AsteroidManager.AsteroidManager()
    collisionManager = CollisionDetection(objectManager)
    for i in range(1,10):
        asteroidManager.createAsteroid(100 + 50*i,0,5)
    sys.exit(app.exec_())