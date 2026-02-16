# Agent abstract class
from abc import ABC, abstractmethod

class Agent(ABC):
    def __init__(self, model):
        self.model = model
        self.x = self.model.rng.randrange(0, self.model.width)
        self.y = self.model.rng.randrange(0, self.model.height)
        self.energy = self.model.energy
        self.alive = True

    def die(self):
        self.alive = False
        
    def move(self):
        moves = [-1, 1]
        if self.model.rng.randint(0, 1) == 1:
            self.x += self.model.rng.choice(moves)
        else:
            self.y += self.model.rng.choice(moves)
        # Wrap around the screen
        if self.x >= self.model.width:
            self.x = 0
        elif self.x < 0:
            self.x = self.model.width-1
        elif self.y >= self.model.height:
            self.y = 0
        elif self.y < 0:
            self.y = self.model.height-1

        self.energy -= 1
        if self.energy <= 0:
            self.die()
        # print(f"x: {self.x}\ny: {self.y}\nenergy: {self.energy}")
        return self.x, self.y

    @abstractmethod
    def interact(self):
        raise NotImplementedError
    
    @abstractmethod
    def reproduce():
        raise NotImplementedError
