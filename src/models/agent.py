# Agent abstract class
from .constants import *
from abc import ABC, abstractmethod
import random

class Agent(ABC):
    def __init__(self):
        self.x = random.randrange(0, WIDTH)
        self.y = random.randrange(0, HEIGHT)
        self.energy = ENERGY
        self.alive = True

    # This doesn't work for some reason
    # @property
    # def x(self):
    #     return self.x
    
    # @property
    # def y(self):
    #     return self.y

    def die(self):
        self.alive = False
        
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

    @abstractmethod
    def interact(self):
        raise NotImplementedError
    
    @abstractmethod
    def reproduce():
        raise NotImplementedError
