import os

#Set working directory
os.chdir(os.path.dirname(__file__))
os.chdir("..")

from grid import Grid
from game import Game
from city import City
from civilization import Civ
from dataplotter import Dataplotter


game = Game(num_civ=5)
game.run()

# civ0 = Civ(0)
# civ1 = Civ(1)
# civ2 = Civ(2)
# civ3 = Civ(3)
# civ4 = Civ(4)

# city1 = City(g,3,4,civ0)
#print('city 1: '+str(city1.y)+', '+str(city1.x)+', '+str(city1.civ.civNum))
#print(str(g.tiles[3,4].city.y)+', '+str(g.tiles[3,4].city.x)+', '+str(g.tiles[3,4].city.civ.civNum))
# city2 = City(g,12,13,civ1)
#print('city 2: '+str(city2.y)+', '+str(city2.x)+', '+str(city2.civ.civNum))
#print(str(g.tiles[12,13].city.y)+', '+str(g.tiles[12,13].city.x)+', '+str(g.tiles[12,13].city.civ.civNum))
# city3 = City(g,4,16,civ2)
#print('city 3: '+str(city3.y)+', '+str(city3.x)+', '+str(city3.civ.civNum))
#print(str(g.tiles[4,16].city.y)+', '+str(g.tiles[4,16].city.x)+', '+str(g.tiles[4,16].city.civ.civNum))
# city4 = City(g,15,5,civ3)
#print('city 4: '+str(city4.y)+', '+str(city4.x)+', '+str(city4.civ.civNum))
#print(str(g.tiles[15,5].city.y)+', '+str(g.tiles[15,5].city.x)+', '+str(g.tiles[15,5].city.civ.civNum))
# city5 = City(g,17,15,civ4)
#print('city 5: '+str(city5.y)+', '+str(city5.x)+', '+str(city5.civ.civNum))
#print(str(g.tiles[17,15].city.y)+', '+str(g.tiles[17,15].city.x)+', '+str(g.tiles[17,15].city.civ.civNum))
"""
print('\n')
print('city 1: '+str(city1.y)+', '+str(city1.x)+', '+str(city1.civ.civNum))
print(str(g.tiles[3,4].city.y)+', '+str(g.tiles[3,4].city.x)+', '+str(g.tiles[3,4].city.civ.civNum))
print('city 2: '+str(city2.y)+', '+str(city2.x)+', '+str(city2.civ.civNum))
print(str(g.tiles[12,13].city.y)+', '+str(g.tiles[12,13].city.x)+', '+str(g.tiles[12,13].city.civ.civNum))
print('city 3: '+str(city3.y)+', '+str(city3.x)+', '+str(city3.civ.civNum))
print(str(g.tiles[4,16].city.y)+', '+str(g.tiles[4,16].city.x)+', '+str(g.tiles[4,16].city.civ.civNum))
print('city 4: '+str(city4.y)+', '+str(city4.x)+', '+str(city4.civ.civNum))
print(str(g.tiles[15,5].city.y)+', '+str(g.tiles[15,5].city.x)+', '+str(g.tiles[15,5].city.civ.civNum))
print('city 5: '+str(city5.y)+', '+str(city5.x)+', '+str(city5.civ.civNum))
print(str(g.tiles[17,15].city.y)+', '+str(g.tiles[17,15].city.x)+', '+str(g.tiles[17,15].city.civ.civNum))
"""

d = Dataplotter(game.cur_grid,plotType=['All'],numCiv=game.num_civ)