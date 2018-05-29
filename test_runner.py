
from dataplotter import Dataplotter
import matplotlib.pyplot as plt
import numpy as N
from game import Game

num_turns = 500
num_civ = 5
game = Game(y=42,x=66,num_civ=num_civ,num_turns=num_turns)
print("initialized the map")
vals = game.run()
# total_vals = N.zeros((num_turns,5))
# for turn in range(num_turns):
#     for civ in range(num_civ):
#         for value in range(5):
#             total_vals[turn,value] = total_vals[turn,value] + vals[turn,civ,value]
x_axis = N.arange(num_turns)+1
labels = ["food","prod","gold","science","pop","num_cities"]
for val in range(6):
    fig = plt.figure()
    fig.suptitle(labels[val],fontsize=20)
    cmap = plt.get_cmap('gist_rainbow')
    cval = N.arange(0,1,1/num_civ)
    ax = fig.add_subplot(111)
    for i in range(num_civ):
        ax.plot(x_axis,vals[:,i,val],color=cmap(cval[i]))
plt.show()
d = Dataplotter(game.cur_grid,plotType=['All'],numCiv=game.num_civ)