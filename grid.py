import numpy as N
from tile import Tile

class Grid(object):

    def __init__(self,y,x,precentGrass=.5,articWidth=3,tundraWidth=5,precentForrest=0.1,self.precentJungle=0.1):
        self.y = y
        self.x = x
        self.precentGrass
        self.articWidth
        self.tundraWidth
        self.precentForrest
        self.precentJungle

        self.tiles = N.zeros((y,x),dtype='object')

        #---------------setting terrain for map---------------------------------
        #Set both artic circle
        for row in range(self.articWidth):
            for col in range(x):
                #top artic circle
                self.tiles[row,col] = Tile(self,row,col,"artic","none")
                #bottom artic circle
                self.tiles[y-row,col] = Tile(self,row,col,"artic","none")

        #Set both tundric circle
        for row in range(self.tundraWidth):
            for col in range(x):
                #top tundra circle
                self.tiles[row,col] = Tile(self,row,col,"tundra","none")
                #bottom tundra circle
                self.tiles[y-row-self.articWidth,col] = Tile(self,row,col,"tundra","none")

        for row in range(:y):
            for col in range(x):
                #Random initialization of tiles terrain
                isGrassTile = N.random.binomial(1,self.precentGrass,1000)
                if(isGrassTile):
                    biome = "grassland"
                else:
                    biome = "plain"
                self.tiles[row,col] = Tile(self,row,col,isGrassTile,"none")

        
        #-----------------------------------------------------------------------
        #TODO initialize all the tiles in the grid
