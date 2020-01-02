import GameLoop as loop
import keyboard
import InputCommandType


#Set desired input for commands
left = "left"
right = "right"
up = "up"
down = "down"
shoot = "ctrl"


# Should be instantiated first to get priority in update cycles
class InputManager:
    def __init__(self):
        self.gl = loop.GameLoop.getInstance()
        self.gl.connect_to_update(self.GetInput)
        self.Command = []

    def GetCommand(self):
        return self.Command

    def GetInput(self):
        self.Command = []
        if keyboard.is_pressed(shoot):
            self.Command.append(InputCommandType.InputCommandType.shoot)
        if keyboard.is_pressed(left):
            self.Command.append(InputCommandType.InputCommandType.left)

        if keyboard.is_pressed(right):
            self.Command.append(InputCommandType.InputCommandType.right)

        if keyboard.is_pressed(up):
            self.Command.append(InputCommandType.InputCommandType.up)
        
        if keyboard.is_pressed(down):
            self.Command.append(InputCommandType.InputCommandType.down)
       
       # print(self.Command) #test