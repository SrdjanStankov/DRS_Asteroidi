import sys
import GameLoop as loop
import keyboard
import InputCommandType
from time import sleep
from threading import Thread
from queue import Queue

# Should be instantiated first to get priority in update cycles
class InputManager:
    def __init__(self):
        self.gl = loop.GameLoop.getInstance()
        self.gl.connect_to_update(self.GetInput)
        self.Command = InputCommandType.InputCommandType.none

    def GetCommnad(self):
        return self.Command

    def GetInput(self):
        print("checking")
        if keyboard.is_pressed("left"):
            self.Command = InputCommandType.InputCommandType.left

        elif keyboard.is_pressed("right"):
            selfCommand = InputCommandType.InputCommandType.right

        else:
            self.Command = InputCommandType.InputCommandType.none