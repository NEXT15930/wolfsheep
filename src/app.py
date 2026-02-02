from model import Model
from models.prey import Prey
from models.predator import Predator

PREY = 12
PREDATOR = 4
STEPS = 15

def main():
    model = Model(seed=2)
    for i in range(PREY):
        model.add_agent(Prey())

    # Loop
    for i in range(STEPS):
        model.step()

main()
        
