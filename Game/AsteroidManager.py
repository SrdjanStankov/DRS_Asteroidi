import sys
from Asteroid import Asteroid
from Player import Player
from PyQt5 import QtWidgets
from GameLoop import GameLoop as gl
import Transform as transform
import InputCommandType as inputCommand
import GameObject as gameObject

import Managers as mng
import Vector as vector
import threading

class AsteroidBeh(gameObject.GameObject):
    def __init__(self, go):
        super().__init__()
        self.asteroid = go

    def update(self):
       self.asteroid.transform.speed=5
       self.asteroid.transform.move(-1)
       self.asteroid.Render.moveItem()

class AsteroidManager(gameObject.GameObject):
    def __init__(self):
        super().__init__()
        print("AsteroidManager init--->{}".format(threading.currentThread()))

        self.count = 0
        self.asteroids = []

    def createAsteroid(self):
        tempTransform = transform.Transform()
        tempTransform.x = 100
        tempTransform.y = 0
        tempTransform.rotation = 0
        tempTransform.speed = 2
        temp = mng.Managers.getInstance().objects.Instantiate("Asteroid",transform = tempTransform,name = "")
        temp.asteroidBehBehaviour = AsteroidBeh(temp)
        self.asteroids.append(temp)

    def update(self):
        pass
        #self.count += 1
        #if(self.count % 60 == 0):
        #    mgr.Managers.getInstance().objects.instansiateSignal.emit("Asteroid")
        #    a = mgr.Managers.getInstance().objects.GetInstantiatedObject()
        #    a.transform.x = self.count
        #    a.transform.y = -50
        #    a.asteroidBeh = AsteroidBeh(a)
        #    self.asteroids.append(a)
