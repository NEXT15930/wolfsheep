from .agent import Agent
from .constants import *
import random

class Prey(Agent):
    """ Prey class """
    def __init__(self, model):
        super().__init__(model)
        self.type = "Prey"

    def interact(self):
        if len(self.model.agents_at(self, self.x, self.y)) == 0:
            if random.randrange(0, PREY_REPRODUCE_RATE) == 1:
                self.reproduce()

    def reproduce(self):
        if self.energy >= REPRODUCE_THRESHOLD:
            self.model.add_agent(Prey(self.model))
            print("Prey reproduce")

