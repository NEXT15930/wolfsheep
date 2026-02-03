from model import Model
from models.prey import Prey
from models.predator import Predator

PREY = 10
PREDATOR = 4
STEPS = 10

def main():
    model = Model(seed=2)
    for i in range(PREY):
        model.add_agent(Prey(model))
    for i in range(PREDATOR):
        model.add_agent(Predator(model))

    # Loop
    for i in range(STEPS):
        model.step()

main()
        
