
from dataplotter import Dataplotter
import matplotlib.pyplot as plt
import numpy as N
from game import Game

def print_pop():
    for civ in game.civs:
        for city in civ.city_list:
            print("pop " + str(city.pop))
        print("next civ")
num_turns = 250
num_civ = 6
game = Game(num_civ=num_civ,num_turns=num_turns)
print("initialized the map")
print_pop()
vals = game.run()

x_axis = N.arange(num_turns)+1
for i in range(num_civ):
    plt.plot(x_axis,vals[:,i,4])
plt.show()
d = Dataplotter(game.cur_grid,plotType=['All'],numCiv=game.num_civ)