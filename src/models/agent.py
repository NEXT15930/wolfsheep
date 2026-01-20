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

    @property
    def x(self):
        return self.x
    
    @property
    def y(self):
        return self.y

    def die(self):
        self.alive = False
        
    @abstractmethod
    def move(self):
        raise NotImplementedError

    @abstractmethod
    def interact(self):
        raise NotImplementedError
    
    @abstractmethod
    def reproduce():
        raise NotImplementedError
