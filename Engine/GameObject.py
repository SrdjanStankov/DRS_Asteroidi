import GameLoop as gl


class GameObject():

    def __init__(self, *args, **kwargs):
        gl.GameLoop.getInstance().connect_to_update(self.update)
    def update(self):
        print("GAME OBJECT UPDATE")