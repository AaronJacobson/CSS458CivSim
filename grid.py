import numpy as N
from tile import Tile
from classlookup import ClassLookUp

class Grid(object):

    def __init__(self,y,x,precentGrass=.5,articWidth=3,tundraWidth=5,probForrest=0.1,probJungle=0.1,probRiver = 0.2,probHill = 0.1):
        self.y = y
        self.x = x
        self.precentGrass = precentGrass
        self.articWidth = articWidth
        self.tundraWidth = tundraWidth
        self.probForrest = probForrest
        self.probJungle = probJungle
        self.probRiver = probRiver
        self.probHill = probHill

        self.tiles = N.zeros((y,x),dtype='object')

        #---------------setting terrain for map---------------------------------
        #Set both artic circle
        for row in range(self.articWidth):
            for col in range(x):
                #print("pretest")
                #top artic circle
                self.tiles[row,col] = Tile(self,row,col,"artic","none")
                #bottom artic circle
                self.tiles[self.y-(1+row),col] = Tile(self,row,col,"artic","none")
                #print("test")

        #Set both tundric circle
        for row in range(self.tundraWidth):
            for col in range(x):
                #top tundra circle
                self.tiles[row,col] = Tile(self,row,col,"tundra","none")
                #bottom tundra circle
                self.tiles[self.y-row-self.articWidth,col] = Tile(self,row,col,"tundra","none")

        #Set the middle terrain

        for row in range((self.tundraWidth+self.articWidth),(self.y-self.tundraWidth-self.articWidth)):
            for col in range(x):
                #Random initialization of tiles terrain
                isGrassTile = N.random.binomial(1,self.precentGrass)
                if(isGrassTile):
                    biome = "grassland"
                else:
                    biome = "plain"
                self.tiles[row,col] = Tile(self,row,col,biome,"none")
        #-----------------------------------------------------------------------

        #----------------------Setting rivers/terrain/elevation-----------------------------------
        for row in range(y):
            isRiverTile = N.random.binomial(1,self.probRiver)
            isJungleTile = N.random.binomial(1,self.probJungle)
            isForrestTile = N.random.binomial(1,self.probForrest)
            isHillTile = N.random.binomial(1,self.probHill)
            if(isRiverTile):
                for col in range(x-1):
                    #set River
                    if(isRiverTile):
                        self.tiles[row,col].near_river = True
                        self.tiles[row,col+1].near_river = True
                    #set terrain
                    if(isForrestTile):
                        self.tiles[row,col].terrain = "forrest"
                        self.tiles[row,col+1].terrain = "forrest"
                    elif(isJungleTile):
                        self.tiles[row,col].terrain = "jungle"
                        self.tiles[row,col+1].terrain = "jungle"
                    #set elevation
                    if(isHillTile):
                        self.tiles[row,col].elevation = "hill"
                        self.tiles[row,col+1].elevation = "hill"
        #-----------------------------------------------------------------------

        #TODO initialize all the tiles in the grid
