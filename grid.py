import numpy as N

class Grid(object):

    def __init__(self,y,x,grid):
        self.grid = grid
        self.y = y
        self.x = x
        self.tiles = N.zeros((y,x),dtype="object")
        #TODO initialize all the tiles in the grid
