import GameLoop as gl
import Transform

class GameObject():

    def __init__(self, *args, **kwargs):
        gl.GameLoop.getInstance().connect_to_update(self.update)
        self.transform = Transform.Transform()
    def update(self):
        pass