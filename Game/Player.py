from GameObject import GameObject
import Managers as mng
import InputCommandType as inputCommand
import time

class Player(GameObject):

    def __init__(self,name,projectileManager):
        super().__init__()
        self.player = mng.Managers.getInstance().objects.Instantiate("Spaceship",name = name)
        self.player.lives = 3
        self.player.points = 0
        self.player.transform.speed = 2
        self.player.transform.x = 1000
        self.player.transform.y = 450
        self.shootCounter = 0
        self.projectiles = []
        self.projectileManager = projectileManager
        self.shootInterval = 0.2
        self.nextShootTime = time.time()
        self.player.invulnerableTime = 4
        self.player.nextAliveTime = time.time()

    def update(self):
        for command in mng.Managers.getInstance().input.Command: 
            if command == inputCommand.InputCommandType.left:
                self.player.transform.rotate(-1)
            if command == inputCommand.InputCommandType.right:
                self.player.transform.rotate(1)
            if command == inputCommand.InputCommandType.up:
                self.player.transform.move(1)
            if command == inputCommand.InputCommandType.down:
                self.player.transform.move(-1)
            if command == inputCommand.InputCommandType.shoot and time.time() > self.nextShootTime:
                self.projectileManager.createProjectile(self.player)
                self.nextShootTime = time.time() + self.shootInterval 