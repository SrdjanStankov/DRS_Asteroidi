from Vector import Vector
import math

class Transform(object):

    def __init__(self, rotation = 0, speed = 10, rotationSpeed = 2, x = 0, y = 0):
        self.x = x
        self.y = y
        self.rotation = rotation
        self.speed = speed
        self.rotationSpeed = rotationSpeed

    def __str__(self):
        return "position: {}, rotation: {}".format((self.x,self.y), self.rotation)

    def rotate(self, direction = 1):
        self.rotation += direction * self.rotationSpeed

    def move(self, Direction = 1):
        dx = Direction * math.sin(math.radians(self.rotation)) * self.speed
        dy = Direction * math.cos(math.radians(self.rotation)) * self.speed
        self.x += dx
        self.y -= dy
        if self.x >= 1400 or self.x < -110 or self.y >= 880 or self.y < -110:
            return False
        else:
            return True

if __name__=="__main__":
    t = Transform()
    t1 = Transform(position=Vector(2,5))
    t2 = Transform(rotation=Vector(4,3))
    t3 = Transform(position=Vector(9,9),rotation=Vector(8,8))
    print(t)
    print(t1)
    print(t2)
    print(t3)