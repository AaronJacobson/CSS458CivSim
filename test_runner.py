
from dataplotter import Dataplotter
import matplotlib.pyplot as plt
import numpy as N
from game import Game

num_turns =250
num_civ = 5
num_sims = 30
# N.zeros((self.num_turns,len(self.civs),6),dtype=N.dtype(int))
average_vals = N.zeros((num_turns,num_civ,6),dtype="f")
for i in range(num_sims):
    print("game " + str(i+1))
    game = Game(y=42,x=66,num_civ=num_civ,num_turns=num_turns)
    print("initialized the map")
    game.civs[0].unit_chance = .4
    game.civs[0].strength_value_coef = 5.0
    game.civs[0].settler_chance_base = .3
    # game.war_chance = 0
    vals = game.run(output=False,print_war_peace=False)
    average_vals = average_vals + vals
average_vals = average_vals / num_sims
x_axis = N.arange(num_turns)+1
labels = ["food","prod","gold","science","pop","num_cities"]
for val in range(6):
    fig = plt.figure()
    fig.suptitle(labels[val],fontsize=20)
    cmap = plt.get_cmap('gist_rainbow')
    cval = N.arange(0,1,1/num_civ)
    ax = fig.add_subplot(111)
    for i in range(num_civ):
        ax.plot(x_axis,average_vals[:,i,val],color=cmap(cval[i]))
plt.show()
d = Dataplotter(game.cur_grid,plotType=['All'],numCiv=game.num_civ)