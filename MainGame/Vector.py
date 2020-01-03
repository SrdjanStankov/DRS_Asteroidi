class Vector(object):
    
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __str__(self):
        return "x: {}, y: {}".format(self.x,self.y)


if __name__=="__main__":
    v1 = Vector()
    v2 = Vector(2,5)
    v3 = Vector(2)
    v4 = Vector(y=2)
    print(v1)
    print(v2)
    print(v3)
    print(v4)
