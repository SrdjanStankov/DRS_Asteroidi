from GameObject import GameObject
import Managers as mgr
import InputCommandType as inputCommand
import time

class Player(GameObject):

    def __init__(self,name,projectileManager):
        super().__init__()
        self.spaceshipObj = mgr.Managers.getInstance().objects.Instantiate("Spaceship",name = name)
        self.spaceshipObj.transform.speed = 2
        self.spaceshipObj.transform.x = 1000
        self.spaceshipObj.transform.y = 450
        self.shootCounter = 0
        self.projectiles = []
        self.projectileManager = projectileManager
        self.shootInterval = 0.2
        self.nextShootTime = time.time()

    def update(self):

        if self.isDeath():
            return

        command = mgr.Managers.getInstance().input.GetCommand() 
        if command == inputCommand.InputCommandType.left:
            self.spaceshipObj.transform.rotate(-1)
        if command == inputCommand.InputCommandType.right:
            self.spaceshipObj.transform.rotate(1)
        if command == inputCommand.InputCommandType.up:
            self.spaceshipObj.transform.move(1)
        if command == inputCommand.InputCommandType.down:
            self.spaceshipObj.transform.move(-1)
        if command == inputCommand.InputCommandType.shoot and time.time() > self.nextShootTime:
            self.projectileManager.createProjectile(self.spaceshipObj)
            self.nextShootTime = time.time() + self.shootInterval 

    def isDeath(self):
        for item in self.spaceshipObj.collisionsType:
            if item == "Asteroid":
                try:
                    mgr.Managers.getInstance().objects.Destroy(self.spaceshipObj.Id)
                    return True
                except:
                    pass
        return False