from GameObject import GameObject

class Player(GameObject):
    
    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)

    def update(self):
        print("Player update");