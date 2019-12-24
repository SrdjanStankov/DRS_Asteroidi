import sys
from Asteroid import Asteroid
from Player import Player
import math
import time
import typing
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QPointF, QThread, pyqtSignal
from PyQt5.QtGui import QBrush, QColor, QPen, QPainterPath, QPixmap
from PyQt5.Qt import Qt
from PyQt5.QtWidgets import QWidget, QStyleOptionGraphicsItem
from GameLoop import GameLoop as gl
from time import sleep

import InputManager as inputManager
import ObjectManager as objMan
import SceneManager as scene
import InputCommandType as inputCommand
import GameObject as gameObject


# Example
class SimpleGO(gameObject.GameObject):
    def __init__(self):
        super().__init__()
        self.go1 = ObjectManager.Instantiate("Spaceship")
    def update(self):
        if Input.GetCommand() == inputCommand.InputCommandType.left:
            print("Destroy")
            ObjectManager.Destroy(self.go1.Id)





if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    
    loop = gl.getInstance()
    Input = inputManager.InputManager()
    SceneManager = scene.SceneManager()
    SceneManager.resize(1300, 700)
    SceneManager.show()
    ObjectManager = objMan.ObjectManager(SceneManager)
    
    go = SimpleGO()
    #loop.cancel()
    sys.exit(app.exec_())