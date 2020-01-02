from GameObject import GameObject
import Managers as mgr
import InputCommandType as inputCommand

class Player(GameObject):
    
    def __init__(self,projectileManager):
        super().__init__()
        self.go1 = mgr.Managers.getInstance().objects.Instantiate("Spaceship")
        self.go1.transform.speed = 2
        self.go1.transform.x = 1000
        self.go1.transform.y = 450
        self.shootCounter = 0
        self.projectiles = []
        self.projectileManager = projectileManager
        
    def update(self):
        self.shootCounter = (self.shootCounter + 1) % 50
        command = mgr.Managers.getInstance().input.GetCommand() 
        if  command == inputCommand.InputCommandType.left:
            self.go1.transform.rotate(-1)
        if command == inputCommand.InputCommandType.right:
            self.go1.transform.rotate(1)
        if command == inputCommand.InputCommandType.up:
            self.go1.transform.move(1)
        if command == inputCommand.InputCommandType.down:
            self.go1.transform.move(-1)
        if command == inputCommand.InputCommandType.shoot:
            if self.shootCounter == 0:
                self.projectileManager.createProjectile(self.go1)