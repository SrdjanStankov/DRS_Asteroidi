from AsteroidAndPlayerTypes import PlayerType
from MutiplayerTournamentMenuScene import MutiplayerTournamentMenuScene


class TournamentMenuMappper():
    def __init__(self):
        pass

    def map(self, scene: MutiplayerTournamentMenuScene):
        tempPlayers = []
        tempPlayers.append((scene.mpti1.textbox.text(), scene.mpti1.buttonGroup.checkedId()))
        tempPlayers.append((scene.mpti2.textbox.text(), scene.mpti2.buttonGroup.checkedId()))
        tempPlayers.append((scene.mpti3.textbox.text(), scene.mpti3.buttonGroup.checkedId()))
        tempPlayers.append((scene.mpti4.textbox.text(), scene.mpti4.buttonGroup.checkedId()))
        tempPlayers.append((scene.mpti5.textbox.text(), scene.mpti5.buttonGroup.checkedId()))
        tempPlayers.append((scene.mpti6.textbox.text(), scene.mpti6.buttonGroup.checkedId()))
        tempPlayers.append((scene.mpti7.textbox.text(), scene.mpti7.buttonGroup.checkedId()))
        tempPlayers.append((scene.mpti8.textbox.text(), scene.mpti8.buttonGroup.checkedId()))
        tempPlayers.append((scene.mpti9.textbox.text(), scene.mpti9.buttonGroup.checkedId()))
        tempPlayers.append((scene.mpti10.textbox.text(), scene.mpti10.buttonGroup.checkedId()))

        players = []
        limit = int(scene.comboBox.currentText())
        for i in range(0, limit):
            id = tempPlayers[i][1]
            player = self.__mapIdToPlayer(id)
            players.append((tempPlayers[i][0], player))


        for i in range(0, limit):
            for j in range(i, limit):
                if i is j:
                    continue
                if players[i][0] == players[j][0] or players[i][0] == '':
                    return None

        return players


    def mapOnlyNames(self, scene: MutiplayerTournamentMenuScene):
        tempPlayers = []
        tempPlayers.append(scene.mpti1.textbox.text())
        tempPlayers.append(scene.mpti2.textbox.text())
        tempPlayers.append(scene.mpti3.textbox.text())
        tempPlayers.append(scene.mpti4.textbox.text())
        tempPlayers.append(scene.mpti5.textbox.text())
        tempPlayers.append(scene.mpti6.textbox.text())
        tempPlayers.append(scene.mpti7.textbox.text())
        tempPlayers.append(scene.mpti8.textbox.text())
        tempPlayers.append(scene.mpti9.textbox.text())
        tempPlayers.append(scene.mpti10.textbox.text())

        players = []
        limit = int(scene.comboBox.currentText())
        for i in range(0, limit):
            name = tempPlayers[i]
            if name == '':
                return None
            players.append((tempPlayers[i]))

        for i in range(0, limit):
            for j in range(i, limit):
                if i is j:
                    continue
                if players[i] == players[j]:
                    return None

        return players


    def __mapIdToPlayer(self, id: int):
        if id is 1:
            ret = PlayerType.player1
        elif id is 2:
            ret = PlayerType.player2
        elif id is 3:
            ret = PlayerType.player3
        else:
            ret = PlayerType.player4

        return ret

