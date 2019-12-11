import GameObject as gameObject
Types = ["Spaceship", "Asteroid" , "srdjan"]    # ;)
class ObjectFactory:
    def __init__(self):
        print("Factory on duty.")

    def Create(self,type):
        if(type == Types[0]):
            return self._CreateSpaceShip()
        elif(type == Types[1]):
            return self._CreteAsteroid()

    # Here populate Asteroid with all his properties
    def _CreteAsteroid(self):
        #print("Asteroid")
        self.go = gameObject.GameObject()
        self.go.Type = "Asteroid"
        return self.go

    # Here populate Spaceship with all his properties
    def _CreateSpaceShip(self):
        #print("Spaceship")
        self.go = gameObject.GameObject()
        self.go.Type = "Spaceship"
        return self.go
