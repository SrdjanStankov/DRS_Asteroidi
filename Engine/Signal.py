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