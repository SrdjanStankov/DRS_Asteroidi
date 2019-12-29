import sys
from Asteroid import Asteroid
from Player import Player
from PyQt5 import QtWidgets
from GameLoop import GameLoop as gl

import InputCommandType as inputCommand
import GameObject as gameObject

import Managers as mgr
import Vector as vector
import threading

class AsteroidBeh(gameObject.GameObject):
    def __init__(self, go):
        super().__init__()
        self.asteroid = go
        self.destroyCounter = 0

    def update(self):
        pass
       #self.asteroid.transform.speed=1
       #self.asteroid.transform.rotate(1)
       #self.asteroid.transform.move(1)
       #try:
       #     self.destroyCounter += 1
       #     if(self.destroyCounter % 420):
       #             mgr.Managers.getInstance().objects.Destroy(self.asteroid)
       #except:
       #     print("Property destroyCounter not found in AsteroidBeh.")

class AsteroidManager(gameObject.GameObject):
    def __init__(self):
        super().__init__()
        print("AsteroidManager init--->{}".format(threading.currentThread()))

        self.count = 0
        self.asteroids = []

    def update(self):
        pass
        #self.count += 1
        #if(self.count % 60 == 0):
        #    mgr.Managers.getInstance().objects.instansiateSignal.emit("Asteroid")
        #    a = mgr.Managers.getInstance().objects.GetInstantiatedObject()
        #    a.transform.position=vector.Vector(self.count,0)
        #    a.asteroidBeh = AsteroidBeh(a)
        #    self.asteroids.append(a)
