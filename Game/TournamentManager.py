import random as rnd
from GameManager import GameManager
from AsteroidAndPlayerTypes import PlayerType
import Managers as mng
from PyQt5.QtCore import pyqtSignal, QObject
import Player

class Tournament(QObject):
    signal = pyqtSignal()
    def __init__(self, *playerNames):
        super(Tournament, self).__init__()
        self.playerNum = len(playerNames)
        self.playerNames = [x for x in playerNames]
        self.brackets = []
        self.bracketsWinners = []
        self.setupBrackets()
        self.signal.connect(self.spawnBracket)
        self.signal.emit()

    def setupBrackets(self):
        while len(self.playerNames) > 0:
            self.brackets.append((self._getPlayer(), self._getPlayer()))

    def _getPlayer(self):
        index = rnd.randint(0, len(self.playerNames) - 1)
        player = self.playerNames[index]
        self.playerNames.remove(player)
        return player

    def spawnBracket(self):
        if len(self.bracketsWinners) >= 2:
            self.brackets.append((self.bracketsWinners[0], self.bracketsWinners[1]))
            self.bracketsWinners.remove(self.bracketsWinners[0])
            self.bracketsWinners.remove(self.bracketsWinners[0])
        
        if len(self.brackets) > 0:
            self.gm = GameManager({PlayerType.player1:self.brackets[0][0],PlayerType.player2:self.brackets[0][1]})
            self.gm.noti.update.connect(self.update)

        if len(self.bracketsWinners) == 1 and len(self.brackets) <= 0:
            # ovde logika za kraj turnira pobednik se nalazi u self.bracketsWinners[0]
            print('Winner {}'.format(self.bracketsWinners[0]))

    def update(self):
        #spaceships = mng.Managers.getInstance().objects.FindObjectsOfType("Spaceship")
        if self.gm.winner is not None:
        #if len(spaceships) != 2:
            # next game
            winnerName = self.gm.winner[0]
            print('bracket winner is ' + winnerName)
            self.bracketsWinners.append(winnerName)
            self.gm.noti.update.disconnect(self.update)
            self.brackets.remove(self.brackets[0])
            mng.Managers.getInstance().input.stopListening()
            for x in self.gm.destroyedShipAttribute:
                mng.Managers.getInstance().scene.removeItem(x)
            for x in range(0, mng.Managers.getInstance().objects.id + 1):
                p = mng.Managers.getInstance().objects.FindById(x)
                if p is not None:
                    if p.Type == 'Spaceship':
                        #mng.Managers.getInstance().scene.removeItem(self.gm.destroyedShipAttribute)
                        mng.Managers.getInstance().scene.removeItem(p.attributesItem)
                mng.Managers.getInstance().objects.Destroy(x)
            del self.gm
            self.signal.emit()

    def _findPlayer(self, playerName):
        playerIndex = -1
        for x in self.brackets:
            if x.count(playerName) > 0:
                playerIndex = self.brackets.index(x)
                return playerIndex
        return playerIndex