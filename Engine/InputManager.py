import GameLoop as loop
import keyboard
import InputCommandType
import json
from enum import IntEnum


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
        self.pipeOut = None
        self.pipeIn = None
    
    def SetPipes(self,write,read):
        self.pipeOut = write
        self.pipeIn = read
       
    def GetCommands(self):
        return self.Command

    def GetInput(self):
        if self.pipeIn is not None:
            self.Command = json.loads(self.pipeIn.recv())
        self.Command_internal = []
        if keyboard.is_pressed(shoot):
            self.Command_internal.append(InputCommandType.InputCommandType.shoot)

        if keyboard.is_pressed(left):
            self.Command_internal.append(InputCommandType.InputCommandType.left)

        if keyboard.is_pressed(right):
            self.Command_internal.append(InputCommandType.InputCommandType.right)

        if keyboard.is_pressed(up):
            self.Command_internal.append(InputCommandType.InputCommandType.up)
        
        if keyboard.is_pressed(down):
            self.Command_internal.append(InputCommandType.InputCommandType.down)
        if self.pipeOut is not None:
            self.pipeOut.send(json.dumps(self.Command_internal))