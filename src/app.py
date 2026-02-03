from model import Model
from models.prey import Prey
from models.predator import Predator
import matplotlib.pyplot as plt

PREY = 10
PREDATOR = 4
STEPS = 30

def main():
    model = Model(seed=2)
    for i in range(PREY):
        model.add_agent(Prey(model))
    for i in range(PREDATOR):
        model.add_agent(Predator(model))

    # Data variables
    time = []
    prey_count = []
    predator_count = []
    
    # Loop
    for i in range(STEPS):
        model.step()
        # Data collection
        prey_count.append(model.get_prey())
        predator_count.append(model.get_predator())
    # TODO: plot data
    print(prey_count)
    print(predator_count)
    plt.plot(prey_count)
    plt.plot(predator_count)
    plt.show()

main()
        
