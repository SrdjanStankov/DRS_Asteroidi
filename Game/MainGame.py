import sys
from Asteroid import Asteroid
from Player import Player
from PyQt5 import QtWidgets
from GameLoop import GameLoop as gl

import InputCommandType as inputCommand
import GameObject as gameObject

import Managers as mgr

# Example
class SimpleGO(gameObject.GameObject):
    def __init__(self):
        super().__init__()
        self.go1 = mgr.Managers.getInstance().object.Instantiate("Spaceship")
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
    ObjectManager = mgr.Managers.getInstance().object
    
    go = SimpleGO()
    sys.exit(app.exec_())