import sys
from PyQt5 import QtWidgets
from GameLoop import GameLoop as gl
import Managers as mgr
from GameManager import GameManager
from StartMenuManager import StartMenuManager
            
# method for canceling game loop thread
def cancel():
    gl.getInstance().cancel()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    
    # connect app exit signal to thread stop of game loop
    app.aboutToQuit.connect(cancel)
    input = mgr.Managers.getInstance().input

    menu = StartMenuManager(app)

    #sceneManager = mgr.Managers.getInstance().scene
    #sceneManager.resize(1550, 1000)
    #sceneManager.show()
    #objectManager = mgr.Managers.getInstance().objects
    #collisionManager = CollisionDetection(objectManager)
    #gm = GameManager()

    sys.exit(app.exec_())

