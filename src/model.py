from models.agent import Agent
from models.prey import Prey
from models.predator import Predator
import random

class Model:
    def __init__(self, seed):
        self.rng = random.Random(seed)
        self.agents = []
        # Keep track of how long its run
        self.time = 0

    def add_agent(self, agent):
        self.agents.append(agent)

    def remove_agent(self, agent):
        self.agents.remove(agent)
        
    def step(self):
        # Randomize sequence for fairness
        self.rng.shuffle(self.agents)

        for agent in self.agents:
            # Move agents
            agent.move()

            # TODO interact
            # TODO reproduce

            # Clean up dead
            if not agent.alive:
                self.remove_agent(agent)

        self.time += 1
