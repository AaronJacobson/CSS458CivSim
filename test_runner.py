from dataplotter import Dataplotter
import matplotlib.pyplot as plt
import numpy as N
from game import Game

num_turns = 400
num_civ = 5
num_sims = 1
sim_vals = N.zeros((num_sims,num_turns,num_civ,6),dtype="f")
for i in range(num_sims):
    print("game " + str(i+1))
    game = Game(y=42,x=66,num_civ=num_civ,num_turns=num_turns)
    sim_vals[i] = game.run(output=False,print_war_peace=False,print_turn=True)
x_axis = N.arange(num_turns)+1
labels = ["Food","Production","Gold","Science","Population","Number of Cities"]
for val in range(6):
    fig = plt.figure()
    fig.suptitle(labels[val],fontsize=20)
    cmap = plt.get_cmap('gist_rainbow')
    cval = N.arange(0,1,1/num_civ)
    ax = fig.add_subplot(111)
    for i in range(num_civ):
        ax.plot(x_axis,N.average(sim_vals[:,:,i,val],axis=0),color=cmap(cval[i]))
plt.show()
#displays the map of the last game, useful if looking at just one game
d = Dataplotter(game.cur_grid,plotType=['All'],numCiv=game.num_civ)
