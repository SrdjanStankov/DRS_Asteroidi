from MultiplayerMenu import MultiplayerMenuu
from StartMenu import StartMenu

class Menus :
    __instance = None

    @staticmethod
    def getInstance():
        if Menus.__instance == None:
            Menus()
        return Menus.__instance

    def __init__(self):
        if Menus.__instance != None:
            raise Exception("This class is singleton!")
        else:
            Menus.__instance = self
            self.startMenu = StartMenu(self)
            self.multiplayerMenu = MultiplayerMenuu(self)

    def ShowStartMenu(self):
        self.startMenu.show()

    def ShowMultiplayerMenu(self):
        self.multiplayerMenu.show()

    def HideStartMenu(self):
        self.startMenu.hide()

    def HideMultiplayerMenu(self):
        self.multiplayerMenu.hide()

