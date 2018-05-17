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
        granary = Building(building_name="granary",gold_yield=-1,food_yield=2)
        library = Building(building_name="library",gold_yield=-1,science_pop_bonus=.5)
        stoneworks = Building(building_name="stoneworks",gold_yield=-1,prod_yield=1)
        watermill = Building(building_name="watermill",gold_yield=-2,food_field=2,prod_yield=1)
        market = Building(building_name="market",gold_yield=2,gold_bonus=.25)
        university = Building(building_name="university",gold_yield=-2,science_bonus=.33)
        workshop = Building(building_name="workshop",gold_yield=-2,prod_yield=2,prod_bonus=.1)
        bank = Building(building_name="bank",gold_yield=2,gold_bonus=.25)
        self.building_lookup = { granary.building_name:granary }
        
        #TODO List of grids
    def cellInit(self,mapName):
        pass
