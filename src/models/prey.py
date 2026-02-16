from .agent import Agent

class Prey(Agent):
    """ Prey class """
    def __init__(self, model):
        super().__init__(model)
        self.type = "Prey"

    def interact(self):
        if len(self.model.agents_at(self, self.x, self.y)) == 0:
            if self.model.rng.randrange(0, self.model.prey_reproduce_rate) == 1:
                self.reproduce()

    def reproduce(self):
        if self.energy >= self.model.reproduce_threshold:
            self.model.add_agent(Prey(self.model))

