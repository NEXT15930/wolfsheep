import random

class Model:
    def __init__(self, seed):
        self.rng = random.Random(seed)
        self.agents = []
        # Keep track of how long its run
        self.time = 0

    def add_agent(self, agent):
        self.agents.insert(0, agent)

    def remove_agent(self, agent):
        self.agents.remove(agent)

    def agents_at(self, caller,  x, y):
        """ This method returns a list of agents at the given position """
        agents_list = []
        for agent in self.agents:
            if agent.x == x and agent.y == y and agent != caller:
                agents_list.append(agent)
        return agents_list

    def get_prey(self):
        """ Returns the amount of prey alive """
        prey_count = 0
        for agent in self.agents:
            if agent.type == "Prey":
                prey_count += 1
        return prey_count

    def get_predator(self):
        """ Returns the amount of predator alive """
        predator_count = 0
        for agent in self.agents:
            if agent.type == "Predator":
                predator_count += 1
        return predator_count
        
    def step(self):
        # Randomize sequence for fairness
        self.rng.shuffle(self.agents)

        # We need a counter to stop the loop from running the reproduced
        agents_length = len(self.agents)
        step_counter = 0
        for agent in self.agents:
            if step_counter < agents_length:
                # Move agents
                agent.move()

                # Interact
                agent.interact()

                # Clean up dead
                if not agent.alive:
                    self.remove_agent(agent)
                step_counter += 1

        self.time += 1
