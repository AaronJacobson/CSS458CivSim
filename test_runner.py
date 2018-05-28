
from dataplotter import Dataplotter
from game import Game

game = Game(num_civ=5)
print("initialized the map")
for i in range(150):
    if (i+1) % 10 == 0:
        print("turn " + str(i+1))
    game.run(i+1)

d = Dataplotter(game.cur_grid,plotType=['All'],numCiv=game.num_civ)