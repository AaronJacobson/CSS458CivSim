
from dataplotter import Dataplotter
import matplotlib.pyplot as plt
import numpy as N
from game import Game

def print_pop_cities():
    for civ in game.civs:
        for city in civ.city_list:
            print("pop " + str(city.pop))
        print("next civ")
num_turns = 500
num_civ = 6
game = Game(num_civ=num_civ,num_turns=num_turns)
print("initialized the map")
vals = game.run()

x_axis = N.arange(num_turns)+1
labels = ["food","prod","gold","science","pop"]
for val in range(5):
    fig = plt.figure()
    fig.suptitle(labels[val],fontsize=20)
    ax = fig.add_subplot(111)
    for i in range(num_civ):
        ax.plot(x_axis,vals[:,i,val])
plt.show()
d = Dataplotter(game.cur_grid,plotType=['All'],numCiv=game.num_civ)