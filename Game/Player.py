from PyQt5.QtCore import QObject
import Managers as mng
import InputCommandType as inputCommand
import time
import PlayerAttributes as playerAttributes

class Player(QObject):

    def __init__(self, name, playerType, projectileManager):
        super(Player, self).__init__()
        self.player = mng.Managers.getInstance().objects.Instantiate("Spaceship", name=name, callable=self.update,playerType = playerType)
        self.player.lives = 3
        self.player.points = 0
        self.player.transform.speed = 2
        self.player.transform.x = 750
        self.player.transform.y = 500
        self.player.radius = 45
        self.playerType = playerType
        self.shootCounter = 0
        self.projectiles = []
        self.projectileManager = projectileManager
        self.player.shootInterval = 0.5
        self.nextShootTime = time.time()
        self.player.invulnerableTime = 4
        self.player.nextAliveTime = time.time()
        attributesItem = playerAttributes.PlayerAttributes(self.player)
        mng.Managers.getInstance().scene.AddItem(attributesItem)

    def update(self):
        for command in mng.Managers.getInstance().input.GetCommands(self.playerType): 
            if command == inputCommand.InputCommandType.left:
                self.player.transform.rotate(-1)
            if command == inputCommand.InputCommandType.right:
                self.player.transform.rotate(1)
            if command == inputCommand.InputCommandType.up:
                topCenter = self.player.Render.getTopCenter()
                if topCenter[0] <= 1400 and topCenter[1] <= 788  and topCenter[0] > 34 and topCenter[1] > 75:
                    self.player.transform.move(1)
            if command == inputCommand.InputCommandType.down:
                botCenter = self.player.Render.getBottomCenter()
                if botCenter[0] <= 1400 and botCenter[1] <= 788  and botCenter[0] > 34 and botCenter[1] > 75:
                    self.player.transform.move(-1)
            if command == inputCommand.InputCommandType.shoot and time.time() > self.nextShootTime:
                self.projectileManager.createProjectile(self.player)
                self.nextShootTime = time.time() + self.player.shootInterval 