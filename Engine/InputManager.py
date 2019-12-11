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


# Should be instantiated first to get priority in update cycles
class InputManager:
    def __init__(self):
        self.gl = loop.GameLoop.getInstance()
        self.gl.connect_to_update(self.GetInput)
        self.Command = InputCommandType.InputCommandType.none

    def GetCommnad(self):
        return self.Command

    def GetInput(self):
        if keyboard.is_pressed(left):
            self.Command = InputCommandType.InputCommandType.left

        elif keyboard.is_pressed(right):
            self.Command = InputCommandType.InputCommandType.right

        else:
            self.Command = InputCommandType.InputCommandType.none
       # print(self.Command) #test