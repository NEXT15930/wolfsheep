from .agent import Agent
from .constants import *
import random

class Prey(Agent):

    def interact(self):
        if len(self.model.agents_at(self, self.x, self.y)) == 0:
            if random.randrange(0, REPRODUCE_RATE) == 1:
                self.reproduce()

    def reproduce(self):
        self.model.add_agent(Prey(self.model))
        print("Reproduce")

