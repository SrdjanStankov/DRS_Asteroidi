import GameLoop as loop
import keyboard
import InputCommandType
from AsteroidAndPlayerTypes import PlayerType

#Set desired input for commands
left = "left"
right = "right"
up = "up"
down = "down"
shoot = "ctrl"

playerOne = {"left":"left","right":"right","up":"up","down":"down","shoot": "ctrl"}
playerTwo = {"left":"a","right":"d","up":"w","down":"s","shoot":"shift"}
playerThree = {"left":"j","right":"l","up":"i","down":"k","shoot":"n"}
playerFour = {"left":52,"right":54,"up":56,"down":53,"shoot":48}

# Should be instantiated first to get priority in update cycles
class InputManager:
    def __init__(self):
        self.gl = loop.GameLoop.getInstance()
        self.gl.connect_to_update(self.GetInput)
        self.commands = {PlayerType.player1:[], PlayerType.player2:[], PlayerType.player3:[], PlayerType.player4:[]}
    
    def GetCommands(self,player:PlayerType):
       return self.commands[player]

    def GetInput(self):
        self.commands[PlayerType.player1] = self.checkCommands(playerOne)
        self.commands[PlayerType.player2] = self.checkCommands(playerTwo)
        self.commands[PlayerType.player3] = self.checkCommands(playerThree)
        #self.commands[PlayerType.player4] = self.checkCommands(playerFour)

    def checkCommands(self,commandScheme):
        commands = []

        if keyboard.is_pressed(commandScheme["shoot"]):
            commands.append(InputCommandType.InputCommandType.shoot)

        if keyboard.is_pressed(commandScheme["left"]):
            commands.append(InputCommandType.InputCommandType.left)

        if keyboard.is_pressed(commandScheme["right"]):
            commands.append(InputCommandType.InputCommandType.right)

        if keyboard.is_pressed(commandScheme["up"]):
            commands.append(InputCommandType.InputCommandType.up)
        
        if keyboard.is_pressed(commandScheme["down"]):
            commands.append(InputCommandType.InputCommandType.down)

        return commands