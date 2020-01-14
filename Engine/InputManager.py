import GameLoop as loop
import keyboard
import InputCommandType
from AsteroidAndPlayerTypes import PlayerType
from multiprocessing import Process, Queue
from time import sleep

playerOne = {"left":"left","right":"right","up":"up","down":"down","shoot":"ctrl"}
playerTwo = {"left":"a","right":"d","up":"w","down":"s","shoot":42}
playerThree = {"left":"g","right":"j","up":"y","down":"h","shoot":"v"}
playerFour = {"left":"l","right":"'","up":"p","down":";","shoot":","}

commands = {}

def checkCommands(commandScheme):
    temp = []

    if keyboard.is_pressed(commandScheme["shoot"]):
        temp.append(InputCommandType.InputCommandType.shoot)

    if keyboard.is_pressed(commandScheme["left"]):
        temp.append(InputCommandType.InputCommandType.left)

    if keyboard.is_pressed(commandScheme["right"]):
        temp.append(InputCommandType.InputCommandType.right)

    if keyboard.is_pressed(commandScheme["up"]):
        temp.append(InputCommandType.InputCommandType.up)
        
    if keyboard.is_pressed(commandScheme["down"]):
        temp.append(InputCommandType.InputCommandType.down)

    return temp

def getInput(queue,commandScheme):
    while True:
        temp = checkCommands(commandScheme)
        for command in temp:
            queue.put(command)
        sleep(1/50)   
# Should be instantiated first to get priority in update cycles
class InputManager:
    def __init__(self):
        #self.gl = loop.GameLoop.getInstance()
        #self.gl.connect_to_update(self.GetInput)
        #self.commands = {PlayerType.player1:Queue(), PlayerType.player2:Queue(), PlayerType.player3:[], PlayerType.player4:[]}
        
        self.processes = []

    def startListening(self,players):
        if PlayerType.player1 in players:
            commands[PlayerType.player1] = Queue()
            self.processes.append(Process(target = getInput, args = [commands[PlayerType.player1],playerOne]))
        if PlayerType.player2 in players:
            commands[PlayerType.player2] = Queue()
            self.processes.append(Process(target = getInput, args = [commands[PlayerType.player2],playerTwo]))
        if PlayerType.player3 in players:
            commands[PlayerType.player3] = Queue()
            self.processes.append(Process(target = getInput, args = [commands[PlayerType.player3],playerThree]))
        if PlayerType.player4 in players:
            commands[PlayerType.player4] = Queue()
            self.processes.append(Process(target = getInput, args = [commands[PlayerType.player4],playerFour]))
        for item in self.processes:
            item.start()

    def GetCommands(self,player:PlayerType):
       queue = commands[player]
       temp = []
       while queue.qsize():
           temp.append(queue.get())

       return temp

    def stopListening(self):
        for item in self.processes:
            item.terminate()
            self.processes.remove(item)

    

