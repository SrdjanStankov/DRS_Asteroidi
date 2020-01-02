import GameLoop as gl
import Transform

class GameObject():

    def __init__(self,callable = None):
        """If you are defining something inside here be sure to call __init__ of base class"""
        if callable is not None:
           self.callable = callable
        else:
            self.callable = self.update
        gl.GameLoop.getInstance().connect_to_update(self.callable)
        self.transform = Transform.Transform()
        self.name = ""
    
    # Nesto se desava
    def update(self):
        """This method will be automatically called inside Game Loop when defined."""
        pass