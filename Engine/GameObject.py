import GameLoop as loop
import sys

class GameObject():

    def __init__(self, *args, **kwargs):
        self.gl = loop.GameLoop.getInstance()
        self.gl._update.connect(self.update)
        print("GAME OBJECT INITIALIZED")

    def update(self):
        print("GAME OBJECT UPDATE")


class ConcreteObject(GameObject):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print("CONCRETE OBJECT INITIALIZED")

    def update(self):
        print("CONCRETE OBJECT UPDATE")