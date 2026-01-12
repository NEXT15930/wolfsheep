# Agent abstract class
import random

class Agent:
    def __init__(self, WIDTH, HEIGHT):
        self.x = random.randrange(0, WIDTH)
        self.x = random.randrange(0, HEIGHT)
        
    def eat():
        pass
    def move():
        self.x += random.randrange(-1, 1)
        self.y += random.randrange(-1, 1)
        # Bring the object back into the screen
        if self.x > 100:
            self.x -= 1
        else if self.x < 0:
            self.x += 1
        if self.y > 100:
            self.y -= 1
        else if self.y < 0:
            self.y += 1
    def reproduce():
        pass
