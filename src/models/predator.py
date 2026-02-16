from .agent import Agent

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
                    self.energy = self.model.energy
                    # Reproduce if they eat
                    if self.model.rng.randrange(0, self.model.predator_reproduce_rate) == 1:
                        self.reproduce()

    def reproduce(self):
        if self.energy >= self.model.reproduce_threshold:
            self.model.add_agent(Predator(self.model))
