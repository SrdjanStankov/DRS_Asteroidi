class Signal(object):

    subscribers = []

    def connect(self, method):
        self.subscribers.append(method)

    def disconnect(self, method):
        try:
            self.subscribers.remove(method)
        except:
            print("There was an error trying to disconnect method: {}".format(method.__name__))

    def notify_all(self):
        for x in self.subscribers:
            x()


def test1():
    print("Test 1")

def test2():
    print("Test 2")

def test3():
    print("Test 3")

if (__name__=="__main__"):
    s = Signal()

    s.connect(test1)

    s.notify_all()
    s.connect(test2)
    print("\n")
    s.notify_all()
    s.connect(test3)
    print("\n")
    s.notify_all()
    s.disconnect(test2)
    print("\n")
    s.notify_all()