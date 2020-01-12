import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal, QObject
import View as sv
import StartScene as sc
import MultiplayerScene as ms
import SingleplayerScene as ss
import Managers as mgr
from GameManager import GameManager


class StartMenuManager(QtWidgets.QMainWindow):


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
        sceneManager = mgr.Managers.getInstance().scene
        sceneManager.resize(1550, 1000)
        sceneManager.show()
        GameManager()

    def backFromMultiplayer(self):
        startView = sv.View(self.startScene)
        self.changeViewMethod(startView)