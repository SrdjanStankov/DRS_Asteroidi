import sys
from Asteroid import Asteroid
from Player import Player
from PyQt5 import QtWidgets
from GameLoop import GameLoop as gl

import InputCommandType as inputCommand
import GameObject as gameObject

import Managers as mgr
import AsteroidManager as AsteroidManager
import Vector as vector
import Transform as transform
from AsteroidManager import AsteroidBeh
# Example
class SimpleGO(gameObject.GameObject):
    def __init__(self):
        super().__init__()
        self.go1 = mgr.Managers.getInstance().objects.Instantiate("Spaceship")
        self.go1.transform.speed=2
        #self.go1.transform = transform.Transform()
        #self.go1.transform.position = vector.Vector(60,0)
        #self.asteroid = mgr.Managers.getInstance().objects.Instantiate("Asteroid")
        #self.asteroid.transform.position = vector.Vector(60,0)
        #self.asteroid.asteroidBeh = AsteroidBeh(self.asteroid)


        #self.asteroid = mgr.Managers.getInstance().objects.Instantiate("Asteroid")
        #self.asteroid.transform.position = vector.Vector(160,0)
        #self.asteroid.asteroidBeh = AsteroidBeh(self.asteroid)
        
    def update(self):
        if mgr.Managers.getInstance().input.GetCommand() == inputCommand.InputCommandType.left:
            self.go1.transform.rotate(1)
        if mgr.Managers.getInstance().input.GetCommand() == inputCommand.InputCommandType.right:
            self.go1.transform.rotate(-1)
        self.go1.transform.move(1)


# method for canceling game loop thread
def cancel():
    gl.getInstance().cancel()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    
    # connect app exit signal to thread stop of game loop
    app.aboutToQuit.connect(cancel)

    Input = mgr.Managers.getInstance().input
    SceneManager = mgr.Managers.getInstance().scene
    SceneManager.resize(1300, 700)
    SceneManager.show()
    ObjectManager = mgr.Managers.getInstance().objects
    
    go = SimpleGO()
    asteroidManager = AsteroidManager.AsteroidManager()
    sys.exit(app.exec_())