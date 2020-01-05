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
from ScreenSides import ScreenSide  
from random import seed,randint
            
# method for canceling game loop thread
def cancel():
    gl.getInstance().cancel()
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
    for i in range(1,10):
        asteroidManager.createAsteroid(ScreenSide(randint(0,3)))
    SpeedUp(1000, 350)
    sys.exit(app.exec_())