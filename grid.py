import numpy as N

class Grid(object):

    def __init__(self,y,x,game):
        self.Game = game
        self.y = y
        self.x = x
        self.tiles = N.array((y,x),dtype=str(object))
        for row in range(y):
            for col in range(x):
                self.tiles[y,x].y = row
                self.tiles[y,x].x = col
        #TODO initialize all the tiles in the grid
