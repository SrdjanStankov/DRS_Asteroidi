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
import TournamentManager
import MultiplayerTwoPlayerScene as mtps
import MultiplayerThreePlayerScene as mthps
import MultiplayerFourPlayerScene as mfps


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
        self.multiplayerTwoPlayerScene = mtps.MultiplayerTwoPlayerScene(self.startTwoPlayerMethod, self.backFromMultiplayerPlayerMenu)
        self.multiplayerThreePlayerScene = mthps.MultiplayerThreePlayerScene(self.startThreePlayerMethod, self.backFromMultiplayerPlayerMenu)
        self.multiplayerFourPlayerScene = mfps.MultiplayerFourPlayerScene(self.startFourPlayerMethod, self.backFromMultiplayerPlayerMenu)
        self.multiplayerScene = ms.MultiplayerScene(self.changeSceneToMultiplayerTwoPlayers,
                                                    self.changeSceneToMultiplayerThreePlayers,
                                                    self.changeSceneToMultiplayerFourPlayers,
                                                    self.backFromMultiplayer,
                                                    self.changeSceneToTournamentFourPlayers)

        self.singleplayerScene = ss.SingleplayerScene()
        self.gm = None
        self.startView = sv.View(self.startScene)
        self.setCentralWidget(self.startView)
        self.levelItem = None
        self.remainingAsteriodsItem = None
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
        self.gm.isTournament = False
        self.levelItem = pli.PlayerLevelInformation(self.gm)
        self.remainingAsteriodsItem = pra.PlayerRemainingAsteroids(self.gm)
        mng.Managers.getInstance().scene.AddItem(self.levelItem)
        mng.Managers.getInstance().scene.AddItem(self.remainingAsteriodsItem)

    def changeSceneToMultiplayerTwoPlayers(self):
        multiplayerTwoPlayerView = sv.View(self.multiplayerTwoPlayerScene)
        self.changeViewMethod(multiplayerTwoPlayerView)

    def changeSceneToMultiplayerThreePlayers(self):
        multiplayerThreePlayerView = sv.View(self.multiplayerThreePlayerScene)
        self.changeViewMethod(multiplayerThreePlayerView)

    def changeSceneToMultiplayerFourPlayers(self):
        multiplayerFourPlayerView = sv.View(self.multiplayerFourPlayerScene)
        self.changeViewMethod(multiplayerFourPlayerView)


    def changeSceneToTournamentFourPlayers(self):
        self.view = QtWidgets.QGraphicsView(self.scene)
        self.view.setSceneRect(90, 90, 1250, 738)
        self.view.setViewportUpdateMode(QtWidgets.QGraphicsView.NoViewportUpdate)
        self.view.setInteractive(False)
        self.setCentralWidget(self.view)
        self.tm = TournamentManager.Tournament("Dejan", "Srdjan", "Nemanja", "Aleksandar")

    def backFromMultiplayer(self):
        if self.gm is not None:
            del self.gm
            self.gm = None
            self.removeItem(self.levelItem)
            self.removeItem(self.remainingAsteriodsItem)
            self.levelItem = None
            self.remainingAsteroidsItem = None
        startView = sv.View(self.startScene)
        self.changeViewMethod(startView)

    def backFromMultiplayerPlayerMenu(self):
        multiplayerView = sv.View(self.multiplayerScene)
        self.changeViewMethod(multiplayerView)


    def startTwoPlayerMethod(self):
        player1name = self.multiplayerTwoPlayerScene.textbox1.text()
        player2name = self.multiplayerTwoPlayerScene.textbox2.text()
        self.view = QtWidgets.QGraphicsView(self.scene)
        self.view.setSceneRect(90, 90, 1250, 738)
        self.view.setViewportUpdateMode(QtWidgets.QGraphicsView.NoViewportUpdate)
        self.view.setInteractive(False)
        self.setCentralWidget(self.view)
        self.gm = GameManager({PlayerType.player1: str(player1name), PlayerType.player2: str(player2name)})
        self.gm.isTournament = False
        self.levelItem = pli.PlayerLevelInformation(self.gm)
        self.remainingAsteriodsItem = pra.PlayerRemainingAsteroids(self.gm)
        mng.Managers.getInstance().scene.AddItem(self.levelItem)
        mng.Managers.getInstance().scene.AddItem(self.remainingAsteriodsItem)

    def startThreePlayerMethod(self):
        player1name = self.multiplayerThreePlayerScene.textbox1.text()
        player2name = self.multiplayerThreePlayerScene.textbox2.text()
        player3name = self.multiplayerThreePlayerScene.textbox3.text()
        self.view = QtWidgets.QGraphicsView(self.scene)
        self.view.setSceneRect(90, 90, 1250, 738)
        self.view.setViewportUpdateMode(QtWidgets.QGraphicsView.NoViewportUpdate)
        self.view.setInteractive(False)
        self.setCentralWidget(self.view)
        self.gm = GameManager({PlayerType.player1: player1name, PlayerType.player2: player2name, PlayerType.player3: player3name})
        self.gm.isTournament = False
        self.levelItem = pli.PlayerLevelInformation(self.gm)
        self.remainingAsteriodsItem = pra.PlayerRemainingAsteroids(self.gm)
        mng.Managers.getInstance().scene.AddItem(self.levelItem)
        mng.Managers.getInstance().scene.AddItem(self.remainingAsteriodsItem)

    def startFourPlayerMethod(self):
        player1name = self.multiplayerFourPlayerScene.textbox1.text()
        player2name = self.multiplayerFourPlayerScene.textbox2.text()
        player3name = self.multiplayerFourPlayerScene.textbox3.text()
        player4name = self.multiplayerFourPlayerScene.textbox4.text()
        self.view = QtWidgets.QGraphicsView(self.scene)
        self.view.setSceneRect(90, 90, 1250, 738)
        self.view.setViewportUpdateMode(QtWidgets.QGraphicsView.NoViewportUpdate)
        self.view.setInteractive(False)
        self.setCentralWidget(self.view)
        self.gm = GameManager({PlayerType.player1: player1name, PlayerType.player2: player2name, PlayerType.player3: player3name,
                               PlayerType.player4: player4name})
        self.gm.isTournament = False
        self.levelItem = pli.PlayerLevelInformation(self.gm)
        self.remainingAsteriodsItem = pra.PlayerRemainingAsteroids(self.gm)
        mng.Managers.getInstance().scene.AddItem(self.levelItem)
        mng.Managers.getInstance().scene.AddItem(self.remainingAsteriodsItem)

    def update(self):     
        for item in self.scene.items():
            if item.itemType == "Spaceship":
                item.rotateItem()
                item.moveItem()
            else:
                item.moveItem()
        self.scene.update()

    def AddItem(self,renderer):
        self.scene.addItem(renderer)

    def removeItem(self, renderer):
        self.scene.removeItem(renderer)