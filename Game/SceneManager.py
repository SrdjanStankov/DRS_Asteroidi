from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtGui import QBrush, QColor
from time import sleep
import threading as th
import Renderer as renderer
import GameLoop as gameLoop
import View as sv
import StartScene as sc
import MultiplayerScene as ms
from PyQt5.QtMultimedia import QSound
import sys
import SingleplayerScene as ss
from GameManager import GameManager
import Managers as mgr
from AsteroidAndPlayerTypes import PlayerType
import PlayerLevelInformation as pli
import PlayerRemainingAsterioids as pra
import Managers as mng


class internalUpdate(QObject):
    update = pyqtSignal()
    def __init__(self):
        super(internalUpdate, self).__init__()
        self.t = th.Thread(target=self.loop)
        self.t.start()
    def loop(self):
        while True:
            if gameLoop.GameLoop.getInstance()._cancelation_token==True:
                break
            self.update.emit()
            sleep(1 / 60)

class SceneManager(QtWidgets.QMainWindow):

    addSignal = pyqtSignal(renderer.Renderer)

    def __init__(self, parent=None):
        super(SceneManager, self).__init__(parent)
        self.startScene = sc.StartScene(self.changeSceneToSingleplayer, self.changeSceneToMultiplayer, self.applicationExitMethod)
        self.multiplayerScene = ms.MultiplayerScene(self.changeSceneToMultiplayerTwoPlayers,self.changeSceneToMultiplayerThreePlayers,self.changeSceneToMultiplayerFourPlayers,self.backFromMultiplayer)
        self.singleplayerScene = ss.SingleplayerScene()

        self.startView = sv.View(self.startScene)
        self.setCentralWidget(self.startView)

        self.scene = QtWidgets.QGraphicsScene(self)
        self.scene.setBackgroundBrush(QBrush(QColor('black')))
        self.scene.setSceneRect(0, 0, 1500, 980)
        self.scene.setItemIndexMethod(QtWidgets.QGraphicsScene.NoIndex)
        self.noti = internalUpdate()
        self.noti.update.connect(self.update)
        self.addSignal.connect(self.AddItem)

    def changeViewMethod(self, view):
        self.setCentralWidget(view)

    def applicationExitMethod(self):
        mgr.Managers.getInstance().app.exit()

    def changeSceneToMultiplayer(self):
        multiplayerView = sv.View(self.multiplayerScene)
        self.changeViewMethod(multiplayerView)

    def changeSceneToSingleplayer(self):      
        self.view = QtWidgets.QGraphicsView(self.scene)
        self.view.setSceneRect(90,90, 1250, 738)
        self.view.setViewportUpdateMode(QtWidgets.QGraphicsView.NoViewportUpdate)
        self.view.setInteractive(False)
        self.setCentralWidget(self.view)
        self.gm = GameManager({PlayerType.player1:"Dejan"})
        levelItem = pli.PlayerLevelInformation(self.gm)
        remainingAsteriodsItem = pra.PlayerRemainingAsteroids(self.gm)
        mng.Managers.getInstance().scene.AddItem(levelItem)
        mng.Managers.getInstance().scene.AddItem(remainingAsteriodsItem)


    def changeSceneToMultiplayerTwoPlayers(self):
        self.view = QtWidgets.QGraphicsView(self.scene)
        self.view.setSceneRect(90,90, 1250, 738)
        self.view.setViewportUpdateMode(QtWidgets.QGraphicsView.NoViewportUpdate)
        self.view.setInteractive(False)
        self.setCentralWidget(self.view)
        self.gm = GameManager({PlayerType.player1:"Dejan",PlayerType.player2:"Srdjan"})

    def changeSceneToMultiplayerThreePlayers(self):
        self.view = QtWidgets.QGraphicsView(self.scene)
        self.view.setSceneRect(90,90, 1250, 738)
        self.view.setViewportUpdateMode(QtWidgets.QGraphicsView.NoViewportUpdate)
        self.view.setInteractive(False)
        self.setCentralWidget(self.view)
        self.gm = GameManager({PlayerType.player1:"Dejan",PlayerType.player2:"Srdjan",PlayerType.player3:"Nemanja"})

    def changeSceneToMultiplayerFourPlayers(self):
        self.view = QtWidgets.QGraphicsView(self.scene)
        self.view.setSceneRect(90,90, 1250, 738)
        self.view.setViewportUpdateMode(QtWidgets.QGraphicsView.NoViewportUpdate)
        self.view.setInteractive(False)
        self.setCentralWidget(self.view)
        self.gm = GameManager({PlayerType.player1:"Dejan",PlayerType.player2:"Srdjan",PlayerType.player3:"Nemanja",PlayerType.player4:"Aleksandar"})

    def backFromMultiplayer(self):
        startView = sv.View(self.startScene)
        self.changeViewMethod(startView)

    def update(self):     
        for item in self.scene.items():
            if item.itemType == "Spaceship":
                item.rotateItem()
                item.moveItem()
                for i in item.pendingSounds:
                    i.play()
                item.pendingSounds.clear()
            else:
                item.moveItem()
        self.scene.update()

    def AddItem(self,renderer):
        self.scene.addItem(renderer)    