import sys
from Player import Player
import Managers as mgr
import AsteroidManager as AsteroidManager
import ProjectileManager as ProjectileManager
from CollisionDetection import CollisionDetection
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal, QObject
import GameLoop as gl
import Renderer as renderer
import View as sv
import StartScene as sc
import MultiplayerScene as ms
import SingleplayerScene as ss


class StartMenuManager(QtWidgets.QMainWindow):

    addSignal = pyqtSignal(renderer.Renderer)

    def __init__(self, app ,parent=None):
        super(StartMenuManager, self).__init__(parent)
        self.app = app

        self.startScene = sc.StartScene(self.changeSceneToSingleplayer, self.changeSceneToMultiplayer, self.applicationExitMethod)
        self.multiplayerScene = ms.MultiplayerScene(self.backFromMultiplayer)
        self.singleplayerScene = ss.SingleplayerScene()

        self.startView = sv.View(self.startScene)
        self.setCentralWidget(self.startView)

    def changeViewMethod(self, view):
        self.setCentralWidget(view)

    def applicationExitMethod(self):
        sys.exit(self.app.exec_())

    def changeSceneToMultiplayer(self):
        multiplayerView = sv.View(self.multiplayerScene)
        self.changeViewMethod(multiplayerView)

    def changeSceneToSingleplayer(self):

        self.hide()
        input = mgr.Managers.getInstance().input
        sceneManager = mgr.Managers.getInstance().scene
        sceneManager.resize(1300, 700)
        sceneManager.show()
        objectManager = mgr.Managers.getInstance().objects
        projectileManager = ProjectileManager.ProjectileManager()
        go = Player("Dejan", projectileManager)
        asteroidManager = AsteroidManager.AsteroidManager()
        collisionManager = CollisionDetection(objectManager)
        for i in range(1, 10):
            asteroidManager.createAsteroid(100 + 50 * i, 0, 5)


    def backFromMultiplayer(self):
        startView = sv.View(self.startScene)
        self.changeViewMethod(startView)