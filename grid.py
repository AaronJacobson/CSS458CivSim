import numpy as N
from tile import Tile
from classlookup import ClassLookUp

class Grid(object):

    def __init__(self,y,x,precentGrass=.5,desert_chance=.0075,desert_size=2,tundraWidth=0.1,snowWidth=0.15,\
    probForrest=0.05,probJungle=0.05,probRiver = 0.2,probHill = 0.1):
        self.y = y
        self.x = x
        self.precentGrass = precentGrass
        self.tundraWidth = int(y*tundraWidth)
        self.snowWidth = int(y*snowWidth)
        self.probForrest = probForrest
        self.probJungle = probJungle
        self.probRiver = probRiver
        self.probHill = probHill

        self.tiles = N.zeros((y,x),dtype='object')
        
        for row in range(self.y):
            for col in range(self.x):
                self.tiles[row,col] = Tile(self,row,col)

        #---------------setting terrain for map---------------------------------
        #Set both tundra circle
        for row in range(self.tundraWidth):
            for col in range(x):
                #print("pretest")
                #top tundra circle
                #self.tiles[row,col] = Tile(self,row,col,"tundra","none")
                self.tiles[row,col].biome = "tundra"
                #bottom tundra circle
                #self.tiles[self.y-(1+row),col] = Tile(self,self.y-(1+row),col,"tundra","none")
                self.tiles[self.y-(1+row),col].biome = "tundra"
                #print("test")

        #Set both tundric circle
        for row in range(self.snowWidth):
            for col in range(x):
                #top snow circle
                #self.tiles[row+self.tundraWidth,col] = Tile(self,row+self.tundraWidth,col,"snow","none")
                self.tiles[row+self.tundraWidth,col].biome = "snow"
                #bottom snow circle
                #self.tiles[self.y-(1+row+self.tundraWidth),col] = Tile(self,self.y-(1+row+self.tundraWidth),col,"snow","none")
                self.tiles[self.y-(1+row+self.tundraWidth),col].biome = "snow"

        #Set the middle terrain

        for row in range((self.snowWidth+self.tundraWidth),(self.y-self.snowWidth-self.tundraWidth)):
            for col in range(x):
                if self.tiles[row,col].biome == "none":
                    #Random initialization of tiles terrain
                    isGrassTile = N.random.binomial(1,self.precentGrass)
                    if(isGrassTile):
                        self.tiles[row,col].biome = "grassland"
                    else:
                        self.tiles[row,col].biome = "plains"
                    if (N.random.binomial(1,desert_chance)):
                        self.tiles[row,col].biome = "desert" 
                        neighbors = self.tiles[row,col].get_neighbors(distance=desert_size)
                        for tile in neighbors:
                            tile.biome = "desert"
                    #self.tiles[row,col] = Tile(self,row,col,biome,"none")
        #-----------------------------------------------------------------------,

        #----------------------Setting rivers/terrain/elevation-----------------------------------
        for row in range(self.tundraWidth+self.snowWidth,y-(self.tundraWidth+self.snowWidth)):
            isRiverTile = N.random.binomial(1,self.probRiver)
            
            for col in range(x-1):
                isJungleTile = N.random.binomial(1,self.probJungle)
                isForrestTile = N.random.binomial(1,self.probForrest)
                isHillTile = N.random.binomial(1,self.probHill)
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
                #set elevation
                if(isHillTile):
                    self.tiles[row,col].elevation = "hill"
                    self.tiles[row,col+1].elevation = "hill"
        #-----------------------------------------------------------------------
        #TODO initialize all the tiles in the grid