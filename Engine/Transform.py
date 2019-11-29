from Vector import Vector

class Transform(object):

    def __init__(self, position = Vector(), rotation = Vector()):
        self.position = position
        self.rotation = rotation

    def __str__(self):
        return "position: {}, rotation: {}".format(self.position, self.rotation)

    def rotate(self):
        raise NotImplementedError("Treaba da se implementira!")

    def move(self):
        raise NotImplementedError("Treaba da se implementira!")


if __name__=="__main__":
    t = Transform()
    t1 = Transform(position=Vector(2,5))
    t2 = Transform(rotation=Vector(4,3))
    t3 = Transform(position=Vector(9,9),rotation=Vector(8,8))
    print(t)
    print(t1)
    print(t2)
    print(t3)