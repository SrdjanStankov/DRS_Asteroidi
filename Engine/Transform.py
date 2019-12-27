from Vector import Vector
import math

class Transform(object):

    def __init__(self, position = Vector(), rotation = 0, speed = 10, rotationSpeed = 10):
        self.position = position
        self.rotation = rotation
        self.speed = speed
        self.rotationSpeed = rotationSpeed

    def __str__(self):
        return "position: {}, rotation: {}".format(self.position, self.rotation)

    def rotate(self, direction = 1):
        self.rotation += direction * self.rotationSpeed

    def move(self, Direction = 1):
        dx = Direction * math.sin(math.radians(self.rotation)) * self.speed
        dy = Direction * math.cos(math.radians(self.rotation)) * self.speed
        self.position.x += dx
        self.position.y -= dy

if __name__=="__main__":
    t = Transform()
    t1 = Transform(position=Vector(2,5))
    t2 = Transform(rotation=Vector(4,3))
    t3 = Transform(position=Vector(9,9),rotation=Vector(8,8))
    print(t)
    print(t1)
    print(t2)
    print(t3)