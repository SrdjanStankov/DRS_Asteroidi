import GameLoop as gameLoop


class CollisionDetection:
    def __init__(self, objectManager):
        gameLoop.Signal.connect(CollisionCheck)
        self.objMan = objectManager

    def CollisionCheck():
        for it in range(self.objMan.Pool.count):   
            it.transform
            pass;


