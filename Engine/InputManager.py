import sys
import GameLoop as loop
import keyboard
import InputCommandType
from time import sleep
from threading import Thread
from queue import Queue


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
        self.Command = InputCommandType.InputCommandType.none

    def GetCommand(self):
        return self.Command

    def GetInput(self):
        if keyboard.is_pressed(shoot):
            self.Command = InputCommandType.InputCommandType.shoot
        elif keyboard.is_pressed(left):
            self.Command = InputCommandType.InputCommandType.left

        elif keyboard.is_pressed(right):
            self.Command = InputCommandType.InputCommandType.right

        elif keyboard.is_pressed(up):
            self.Command = InputCommandType.InputCommandType.up
        
        elif keyboard.is_pressed(down):
            self.Command = InputCommandType.InputCommandType.down
        else:
            self.Command = InputCommandType.InputCommandType.none
       # print(self.Command) #test