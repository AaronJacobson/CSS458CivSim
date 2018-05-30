
import numpy as N
from tile import Tile
from classlookup import ClassLookUp

class Grid(object):
    """
    Summary:
    Grid holds the map of the game. The way this is done is by holding the
    2-dimensional array of tile objects. Tile objects will hold all the data
    about each tile but grid will be used to change the overall actions of the
    board.
    """
    def __init__(self,y,x,percent_grass=.5,desert_chance=.01,desert_size=2,\
    snow_width=0.05,tundra_width=0.075,prob_forest=0.05,prob_jungle=0.05,\
    prob_river = 0.2,prob_hill=.085):
        """
        Summary:
            Constructor for the Grid class that runs the simulation. Initializes
            state variables, creates the 2-d array and populates it with tiles. Then
            creates gives each tile the correct biom, elevation, and terrain.
    
        Method Arguments:
            y*: the height of the grid to be created
            x*: the length of the grid to be created
            percent_grass*: Percent chance that a tile in the middle of the map is
                            grassland instead of plains.
            desert_chance*: Percent chance that a tile and its surrounding tiles up
                            to distance desert_size are made into desert tiles.
            desert_size*:   The number of steps away from a central desert tile that
                            will be made into desert upon map generation.
            snow_width*:    The percentage of the top and bottom of the grid that will
                            become snow tiles.
            tundra_width*:  The percentage of the top and bottom of the grid that will
                            become tundra tiles.
            prob_forest*:   Percent chance that any tile and its next neighbor will be
                            made into forests.
            prob_jungle*:   Percent chance that any tile and its next neighbor will be
                            made into jungles.
            prob_river*:    Percent chance that any tile and its next neighbor will
                            have a river running through them.
            prob_hill*:     Percent chance that any tile will become a hill.
        """
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
                self.tiles[row+self.snow_width,col].biome = "tundra"
                #bottom snow circle
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

        #-------------------Sets the yeilds for each tile-----------------------
        for row in range(self.y):
            for col in range(self.x):
                tile = self.tiles[row,col]
                if tile.terrain == "forest":
                    tile.food_yield = 1
                    tile.prod_yield = 1
                elif tile.terrain == "jungle":
                    tile.food_yield = 2
                elif tile.elevation == "hill":
                    tile.prod_yield = 2
                elif tile.biome == "grassland":
                    tile.food_yield = 2
                elif tile.biome == "tundra":
                    tile.food_yield = 1
                elif tile.biome == "plains":
                    tile.food_yield = 1
                    tile.prod_yield = 1
                elif tile.biome == "desert" and tile.near_river:
                    tile.food_yield = 2
        #-----------------------------------------------------------------------
