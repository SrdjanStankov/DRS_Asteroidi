import GameLoop as gloop
import InputManager as inputManager
import ObjectManager as objMan
# Here start up StartUI
if __name__ == "__main__":
    print("This is main")
    gameLoop = gloop.GameLoop()
    Input = inputManager.InputManager()
    ObjectManager = objMan.ObjectManager()
    
    
    #====test=======
    gameLoop.start_loop()
    go1 = ObjectManager.Instantiate("Spaceship")
    print(f"{go1.Id} { go1.Type}")
    go2 = ObjectManager.Instantiate("Asteroid")
    print(f"{go2.Id} { go2.Type}")
    go3 = ObjectManager.Instantiate("Asteroid")
    print(f"{go3.Id} { go3.Type}")

    print("test ")
    
    go4 = ObjectManager.FindById(2)
    print(f"{go4.Id} { go4.Type}")


    gos = ObjectManager.FindObjectsOfType("Asteroid")
    for i in gos:
        print(i.Id)
    ObjectManager.Destroy(1)

    for i in ObjectManager.Pool:
        print(i.Id)
    #=====test==========






