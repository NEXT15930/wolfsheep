from model import Model
from models.prey import Prey
from models.predator import Predator
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

PREY = 10
PREDATOR = 4
STEPS = 300

model = Model(seed=2)
# Data variables
time = []
prey_count = []
predator_count = []

# Setup plot
fig, ax = plt.subplots()
line, = ax.plot([], [], label = "Prey count")
line2, = ax.plot([], [], label = "Predator count")
ax.legend()
ax.set_title("ABM: Prey vs Predator")
ax.set_xlabel("Time")
ax.set_ylim(0, 150)
ax.set_xlim(0, STEPS)

def update(frame):
    global ani
    if frame >= STEPS-1:
        ani.pause()
    model.step()
    # Data collection
    time.append(model.time)
    prey_count.append(model.get_prey())
    predator_count.append(model.get_predator())
    line.set_xdata(time)
    line.set_ydata(prey_count)
    line2.set_xdata(time)
    line2.set_ydata(predator_count)
    return line, line2

# Add agents to model
for i in range(PREY):
    model.add_agent(Prey(model))
for i in range(PREDATOR):
    model.add_agent(Predator(model))

# Animation
ani = FuncAnimation(fig, update, frames = STEPS, interval = 50)
plt.show()
