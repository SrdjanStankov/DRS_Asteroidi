import GameLoop as gameLoop
from PyQt5.QtCore import QPointF, QThread, pyqtSignal, QObject
import threading as th
import time
from time import sleep
import math


class internalUpdate(QObject):

    update = pyqtSignal()

    def __init__(self):
        super(internalUpdate, self).__init__()
        self.t = th.Thread(target=self.loop)
        self.t.start()

    def loop(self):
        while True:
            self.update.emit()
            sleep(1 / 10)


class CollisionDetection:
    def __init__(self, objectManager):
        self.objMan = objectManager
        self.noti = internalUpdate()
        self.noti.update.connect(self.update)

    def update(self):
        for i in range(len(self.objMan.Pool)):
            try:
                self.objMan.Pool[i].collisions.clear()
                self.objMan.Pool[i].collisionsType.clear()
            except:
                pass
        for i in range(len(self.objMan.Pool)):   
            for j in range(i,len(self.objMan.Pool)):
                try:            
                    if self.objMan.Pool[i].Id != self.objMan.Pool[j].Id:
                        if self.objMan.Pool[i].Type != self.objMan.Pool[j].Type:
                        
                            r1 = self.objMan.Pool[i].radius
                            r2 = self.objMan.Pool[j].radius
                            x1 = self.objMan.Pool[i].transform.x + self.objMan.Pool[i].Render.width
                            y1 = self.objMan.Pool[i].transform.y + self.objMan.Pool[i].Render.height
                            x2 = self.objMan.Pool[j].transform.x + self.objMan.Pool[j].Render.width
                            y2 = self.objMan.Pool[j].transform.y + self.objMan.Pool[j].Render.height
                            if pow(r1 + r2,2) > pow(x2 - x1,2) + pow(y2 - y1,2):
                                self.objMan.Pool[i].collisions.append(self.objMan.Pool[j].Id)
                                self.objMan.Pool[j].collisions.append(self.objMan.Pool[i].Id)
                                self.objMan.Pool[i].collisionsType.append(self.objMan.Pool[j].Type)
                                self.objMan.Pool[j].collisionsType.append(self.objMan.Pool[i].Type)

                except:
                    pass