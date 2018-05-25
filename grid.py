import numpy as N
from tile import Tile

class Grid(object):

    def __init__(self,y,x):
        self.y = y
        self.x = x
        self.tiles = N.zeros((y,x),dtype='object')
        for row in range(y):
            for col in range(x):
                self.tiles[row,col] = Tile(self,row,col)
        #TODO initialize all the tiles in the grid
