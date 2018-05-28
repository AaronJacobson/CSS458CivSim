
from dataplotter import Dataplotter
from game import Game

game = Game(num_civ=5,num_turns=150)
print("initialized the map")
vals = game.run()


d = Dataplotter(game.cur_grid,plotType=['All'],numCiv=game.num_civ)