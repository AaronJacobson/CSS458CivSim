from grid import Grid
from building import Building
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
        #TODO List of grids\
        
    def initBuildingLookUp(self):
        granary = Building(building_name="granary",gold_yield=-1,gold_bonus=0,food_yield=2,\
        food_bonus=0,science_yield=0,science_bonus=0,science_pop_bonus=0,\
        prod_yield=0,prod_bonus=0)
        
        self.building_lookup = { granary.building_name:granary }
        
        #TODO List of grids
    def cellInit(self,mapName):
        pass
