
from dataplotter import Dataplotter
import matplotlib.pyplot as plt
import numpy as N
from game import Game

num_turns = 300
game = Game(num_civ=5,num_turns=num_turns)
print("initialized the map")
vals = game.run()
for i in range(150):
    # print(vals[i,1])
    pass
x_axis = N.arange(num_turns)+1
plt.plot(x_axis,vals[:,0,4])
plt.show()
# print(game.civs[1].city_list[0].pop)
d = Dataplotter(game.cur_grid,plotType=['All'],numCiv=game.num_civ)