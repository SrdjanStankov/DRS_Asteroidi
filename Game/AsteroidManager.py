import sys
from Asteroid import Asteroid
from Player import Player
from PyQt5 import QtWidgets
from GameLoop import GameLoop as gl

import InputCommandType as inputCommand
import GameObject as gameObject

import Managers as mgr
import Vector as vector

class AsteroidBeh(gameObject.GameObject):
    def __init__(self, go):
        super().__init__()
        self.asteroid = go
        self.destroyCounter = 0

    def update(self):
       pass
       self.asteroid.transform.rotate(1)
        #self.transform.move(1)
#try:
        #    self.destroyCounter += 1
        #    if(self.destroyCounter % 420):
        #        mgr.Managers.getInstance().objects.Destroy(self.asteroid)
        #except:
        #    print("Property destroyCounter not found in AsteroidBeh.")

class AsteroidManager(gameObject.GameObject):
     def __init__(self):
        super().__init__()
        self.count = 0
        self.asteroid = []
     def update(self):
         self.count += 1
         if(self.count % 60 == 0):
            self.asteroid = mgr.Managers.getInstance().objects.Instantiate("Asteroid")
            self.asteroid.transform.position=vector.Vector(self.count,0)
            self.asteroid.asteroidBeh = AsteroidBeh(self.asteroid)
