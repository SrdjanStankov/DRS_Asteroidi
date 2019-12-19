from Asteroid import Asteroid
from Player import Player

if __name__ == "__main__":
    from GameLoop import GameLoop as gl
    from time import sleep
    loop = gl.getInstance()
    

    p = Player()
    a = Asteroid()


    sleep(1);

    loop.cancel();