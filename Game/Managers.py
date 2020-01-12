import sys
from PyQt5 import QtWidgets
import InputManager as inputManager
import ObjectManager as objMan
import SceneManager as scene
import CollisionDetection as collision

class Managers():
    
    __instance = None

    @staticmethod
    def getInstance():
        if Managers.__instance==None:
            Managers()
        return Managers.__instance

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(Managers, cls).__new__(cls)
            cls.__instance.app = QtWidgets.QApplication(sys.argv)
            cls.__instance.input = inputManager.InputManager();
            cls.__instance.scene = scene.SceneManager();
            cls.__instance.scene.resize(1550, 1000)
            cls.__instance.objects = objMan.ObjectManager(cls.__instance.scene);
            cls.__instance.collisionDetection = collision.CollisionDetection(cls.__instance.objects)
        return cls.__instance

