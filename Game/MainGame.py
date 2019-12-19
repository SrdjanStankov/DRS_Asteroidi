from GameObject import GameObject

class Asteroid(GameObject):
    
    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)

    def update(self):
        print("asteroid update")


if __name__ == "__main__":
    
    a = Asteroid();

    from time import sleep

    sleep(5);

    from GameLoop import GameLoop as gl

    gl.getInstance().cancel();