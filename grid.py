import numpy as N
from tile import Tile
from classlookup import ClassLookUp

class Grid(object):

    def __init__(self,y,x,precentGrass=.5,tundraWidth=0.1,snowWidth=0.15,probForrest=0.05,probJungle=0.05,probRiver = 0.2,probHill = 0.05):
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

        #---------------setting terrain for map---------------------------------
        #Set both tundra circle
        for row in range(self.tundraWidth):
            for col in range(x):
                #print("pretest")
                #top tundra circle
                self.tiles[row,col] = Tile(self,row,col,"tundra","none")
                #bottom tundra circle
                self.tiles[self.y-(1+row),col] = Tile(self,self.y-(1+row),col,"tundra","none")
                #print("test")

        #Set both tundric circle
        for row in range(self.snowWidth):
            for col in range(x):
                #top snow circle
                self.tiles[row+self.tundraWidth,col] = Tile(self,row+self.tundraWidth,col,"snow","none")
                #bottom snow circle
                self.tiles[self.y-(1+row+self.tundraWidth),col] = Tile(self,self.y-(1+row+self.tundraWidth),col,"snow","none")

        #Set the middle terrain

        for row in range((self.snowWidth+self.tundraWidth),(self.y-self.snowWidth-self.tundraWidth)):
            for col in range(x):
                #Random initialization of tiles terrain
                isGrassTile = N.random.binomial(1,self.precentGrass)
                if(isGrassTile):
                    biome = "grassland"
                else:
                    biome = "plains"
                self.tiles[row,col] = Tile(self,row,col,biome,"none")
        #-----------------------------------------------------------------------

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
                if(isForrestTile):
                    self.tiles[row,col].terrain = "forest"
                    self.tiles[row,col+1].terrain = "forest"
                elif(isJungleTile):
                    self.tiles[row,col].terrain = "jungle"
                    self.tiles[row,col+1].terrain = "jungle"
                #set elevation
                if(isHillTile):
                    self.tiles[row,col].elevation = "hill"
                    self.tiles[row,col+1].elevation = "hill"
        #-----------------------------------------------------------------------

        #TODO initialize all the tiles in the grid