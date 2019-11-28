import GameLoop as gl


class GameObject():

    def __init__(self, *args, **kwargs):
        gl.GameLoop.getInstance().connect_to_update(self.update)
    def update(self):
        print("GAME OBJECT UPDATE")
        

class ConcreteObject(GameObject):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def update(self):
        print("CONCRETE OBJECT UPDATE")
        pass

if __name__ == '__main__':
    from time import sleep
    
    go1 = ConcreteObject()
    go2 = ConcreteObject()
    go3 = ConcreteObject()
    go4 = ConcreteObject()

    sleep(1)
    gl.GameLoop.getInstance().cancel()