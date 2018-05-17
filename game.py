from grid import Grid
from Civilization import Civ

class Game(object):
    
    def __init__(self,y=50,x=100,numTurns=500):
        
        self.turns = []
        self.num_turns = numTurns
        self.turns[0] = Grid(y,x)
        
        self.unit_Dict = None
        self.building_Dict = None
        self.yields_Dict = None
        
        self.civs = None
        self.grids = None
        #TODO initialize the list/dictionary of biomes and they're yields
        #TODO List of grids
    def cellInit(self,mapName):
        pass
    
