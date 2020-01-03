import sys
from Asteroid import Asteroid
from Player import Player
from PyQt5 import QtWidgets
from GameLoop import GameLoop as gl
from CollisionDetection import CollisionDetection

import InputCommandType as inputCommand
import GameObject as gameObject

import Managers as mgr
import AsteroidManager as AsteroidManager
import Vector as vector
import Transform as transform
import ProjectileManager as ProjectileManager
from AsteroidManager import AsteroidBeh
# Example
class SimpleGO(gameObject.GameObject):
    def __init__(self,projectileManager):
        super().__init__()
        self.go1 = mgr.Managers.getInstance().objects.Instantiate("Spaceship")
        self.go1.transform.speed = 2
        self.go1.transform.x = 1000
        self.go1.transform.y = 450
        self.shootCounter = 0
        self.projectiles = []
        self.projectileManager = projectileManager
        
        #self.go1.transform = transform.Transform()
        #self.go1.transform.position = vector.Vector(60,0)
        #self.asteroid =
        #mgr.Managers.getInstance().objects.Instantiate("Asteroid")
        #self.asteroid.transform.position = vector.Vector(60,0)
        #self.asteroid.asteroidBeh = AsteroidBeh(self.asteroid)


        #self.asteroid =
        #mgr.Managers.getInstance().objects.Instantiate("Asteroid")
        #self.asteroid.transform.position = vector.Vector(160,0)
        #self.asteroid.asteroidBeh = AsteroidBeh(self.asteroid)
        
    def update(self):
        self.shootCounter = (self.shootCounter + 1) % 60
        for cmd in mgr.Managers.getInstance().input.GetCommand():
            if cmd == inputCommand.InputCommandType.left:
                self.go1.transform.rotate(-1)
            if cmd == inputCommand.InputCommandType.right:
                self.go1.transform.rotate(1)
            if cmd == inputCommand.InputCommandType.up:
                 self.go1.transform.move(1)
            if cmd == inputCommand.InputCommandType.down:
                  self.go1.transform.move(-1)
            if cmd == inputCommand.InputCommandType.shoot:
                  if self.shootCounter != 0:
                    self.projectileManager.createProjectile(self.go1)
           
            


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
    go = SimpleGO(projectileManager)
    asteroidManager = AsteroidManager.AsteroidManager()
    collisions = CollisionDetection(mgr.Managers.getInstance().objects)
    for i in range(1,30):
        asteroidManager.createAsteroid(100 + 50 * i,0,5)
    sys.exit(app.exec_())