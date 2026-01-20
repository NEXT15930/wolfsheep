from .agent import Agent
from .constants import *
import random

class Prey(Agent):
    def move(self):
        moves = [-1, 1]
        if random.randint(0, 1) == 1:
            self.x += random.choice(moves)
        else:
            self.y += random.choice(moves)
        # Wrap around the screen
        if self.x >= WIDTH:
            self.x = 0
        elif self.x < 0:
            self.x = WIDTH-1
        elif self.y >= HEIGHT:
            self.y = 0
        elif self.y < 0:
            self.y = HEIGHT-1

        self.energy -= 1
        if self.energy <= 0:
            self.die()
        print(f"x: {self.x}\ny: {self.y}\nenergy: {self.energy}")
        return self.x, self.y

    def interact(self):
        pass

    def reproduce(self):
        pass

