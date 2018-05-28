import numpy as N
from tile import Tile
from classlookup import ClassLookUp

class Grid(object):

    def __init__(self,y,x,percent_grass=.5,desert_chance=.01,desert_size=2,\
    snow_width=0.05,tundra_width=0.075,prob_forest=0.05,prob_jungle=0.05,\
    prob_river = 0.2,prob_hill=.085):
        self.y = y
        self.x = x
        self.percent_grass = percent_grass
        self.snow_width = int(y*snow_width)
        self.tundra_width = int(y*tundra_width)
        self.prob_forest = prob_forest
        self.prob_jungle = prob_jungle
        self.prob_river = prob_river
        self.prob_hill = prob_hill

        self.tiles = N.zeros((y,x),dtype='object')
        
        for row in range(self.y):
            for col in range(self.x):
                self.tiles[row,col] = Tile(self,row,col)

        #---------------setting terrain for map---------------------------------
        #Set both snow circle
        for row in range(self.snow_width):
            for col in range(x):
                #print("pretest")
                #top tundra circle
                #self.tiles[row,col] = Tile(self,row,col,"tundra","none")
                self.tiles[row,col].biome = "snow"
                #bottom tundra circle
                #self.tiles[self.y-(1+row),col] = Tile(self,self.y-(1+row),col,"tundra","none")
                self.tiles[self.y-(1+row),col].biome = "snow"
                #print("test")

                isHillTile = N.random.binomial(1,self.prob_hill)#for top
                #set elevation
                if(isHillTile):
                    self.tiles[row,col].elevation = "hill"
                    self.tiles[row,col-1].elevation = "hill"
                    
                isHillTile = N.random.binomial(1,self.prob_hill)#for bottom
                #set elevation
                if(isHillTile):
                    self.tiles[self.y-(1+row),col].elevation = "hill"
                    self.tiles[self.y-(1+row),col-1].elevation = "hill"

        #Set both tundric circle
        for row in range(self.tundra_width):
            for col in range(x):
                #top snow circle
                #self.tiles[row+self.tundraWidth,col] = Tile(self,row+self.tundraWidth,col,"snow","none")
                self.tiles[row+self.snow_width,col].biome = "tundra"
                #bottom snow circle
                #self.tiles[self.y-(1+row+self.tundraWidth),col] = Tile(self,self.y-(1+row+self.tundraWidth),col,"snow","none")
                self.tiles[self.y-(1+row+self.snow_width),col].biome = "tundra"

                isHillTile = N.random.binomial(1,self.prob_hill)#for top
                #set elevation
                if(isHillTile):
                    self.tiles[row+self.snow_width,col].elevation = "hill"
                    self.tiles[row+self.snow_width,col-1].elevation = "hill"
                    
                isHillTile = N.random.binomial(1,self.prob_hill)#for bottom
                #set elevation
                if(isHillTile):
                    self.tiles[self.y-(1+row+self.snow_width),col].elevation = "hill"
                    self.tiles[self.y-(1+row+self.snow_width),col-1].elevation = "hill"

        #Set the middle terrain

        for row in range((self.tundra_width+self.snow_width),(self.y-self.tundra_width-self.snow_width)):
            for col in range(x):
                if self.tiles[row,col].biome == "none":
                    #Random initialization of tiles terrain
                    isGrassTile = N.random.binomial(1,self.percent_grass)
                    if(isGrassTile):
                        self.tiles[row,col].biome = "grassland"
                    else:
                        self.tiles[row,col].biome = "plains"
                    if (N.random.binomial(1,desert_chance)):
                        self.tiles[row,col].biome = "desert" 
                        neighbors = self.tiles[row,col].get_neighbors(distance=desert_size)
                        for tile in neighbors:
                            tile.biome = "desert"

                isHillTile = N.random.binomial(1,self.prob_hill)
                #set elevation
                if(isHillTile):
                    self.tiles[row,col].elevation = "hill"
                    self.tiles[row,col-1].elevation = "hill"
                    #self.tiles[row,col] = Tile(self,row,col,biome,"none")
        #-----------------------------------------------------------------------,

        #----------------------Setting rivers/terrain/elevation-----------------------------------
        for row in range(self.snow_width+self.tundra_width,y-(self.snow_width+self.tundra_width)):
            isRiverTile = N.random.binomial(1,self.prob_river)
            
            for col in range(x-1):
                isJungleTile = N.random.binomial(1,self.prob_jungle)
                isForrestTile = N.random.binomial(1,self.prob_forest)
                #set River
                if(isRiverTile):
                    self.tiles[row,col].near_river = True
                    self.tiles[row,col+1].near_river = True
                #set terrain
                if not (self.tiles[row,col].biome == "desert"):
                    if(isForrestTile):
                        self.tiles[row,col].terrain = "forest"
                        self.tiles[row,col+1].terrain = "forest"
                        self.tiles[row,col+1].biome = self.tiles[row,col].biome
                    elif(isJungleTile):
                        self.tiles[row,col].terrain = "jungle"
                        self.tiles[row,col+1].terrain = "jungle"
                        self.tiles[row,col].biome = "plains"
                        self.tiles[row,col+1].biome = "plains"
        #-----------------------------------------------------------------------
        #TODO initialize all the tiles in the grid