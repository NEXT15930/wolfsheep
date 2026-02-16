from .agent import Agent
from .constants import *
import random

class Predator(Agent):
    """ Predator class """
    def __init__(self, model):
        super().__init__(model)
        self.type = "Predator"
        
    def interact(self):
        agents_at_position = self.model.agents_at(self, self.x, self.y)
        if len(agents_at_position) > 0:
            for agent in agents_at_position:
                if agent.type == "Prey":
                    agent.die()
                    self.energy = ENERGY
                    # Reproduce if they eat
                    if random.randrange(0, PREDATOR_REPRODUCE_RATE) == 1:
                        self.reproduce()

    def reproduce(self):
        if self.energy >= REPRODUCE_THRESHOLD:
            self.model.add_agent(Predator(self.model))
