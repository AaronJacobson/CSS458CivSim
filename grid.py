import numpy as N

class Grid(object):
    
    def __init__(self,y,x):
        self.y = y
        self.x = x
        self.tiles = N.array((y,x),dtype=str(object))
        #TODO initialize all the tiles in the grid
