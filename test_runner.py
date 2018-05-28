
from dataplotter import Dataplotter
import matplotlib.pyplot as plt
from game import Game

game = Game(num_civ=5,num_turns=150)
print("initialized the map")
vals = game.run()
for i in range(150):
    # print(vals[i,1])
    pass
# print(game.civs[1].city_list[0].pop)
d = Dataplotter(game.cur_grid,plotType=['All'],numCiv=game.num_civ)