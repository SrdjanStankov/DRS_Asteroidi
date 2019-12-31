import GameLoop as gl
import Transform

class GameObject():

    def __init__(self):
        """If you are defining something inside here be sure to call __init__ of base class"""
        gl.GameLoop.getInstance().connect_to_update(self.update)
        self.transform = Transform.Transform()
        self.name = ""
        self.collisionWithId = -1
        self.active = True
    
    # Nesto se desava
    def update(self):
        """This method will be automatically called inside Game Loop when defined."""
        pass