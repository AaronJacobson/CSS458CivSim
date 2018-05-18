from grid import Grid
from building import Building
from Civilization import Civ

class Game(object):
    
    def __init__(self,y=50,x=100,numTurns=500):
        self.initBuildingLook()
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
        granary = Building(name="granary",gold_yield=-1,food_yield=2)
        library = Building(name="library",gold_yield=-1,science_pop_bonus=.5)
        stoneworks = Building(name="stoneworks",gold_yield=-1,prod_yield=1)
        watermill = Building(name="watermill",gold_yield=-2,food_field=2,prod_yield=1)
        market = Building(name="market",gold_yield=2,gold_bonus=.25)
        university = Building(name="university",gold_yield=-2,science_bonus=.33)
        workshop = Building(name="workshop",gold_yield=-2,prod_yield=2,prod_bonus=.1)
        bank = Building(name="bank",gold_yield=2,gold_bonus=.25)
        observatory = Building(name="observatory",science_bonus=.5)
        windmill = Building(name="windmill",gold_yield=-2,prod_yield=2,prod_bonus=.1)
        factory = Building(name="factory",gold_yield=-3,prod_yield=4,prod_bonus=.1)
        hospital = Building(name="hospital",gold_yield=-2,food_yield=5)
        public_school = Building(name="public_school",gold_yield=-3,science_yield=3,science_pop_bonus=.5)
        stock_exchange = Building(name="stock_exchange",gold_yield=3,gold_bonus=.33)
        research_lab = Building(name="research_lab",gold_yield=-3,science_yield=4,science_bonus=.5)
        power_plant = Building(name="power_plant",gold_yield=-3,prod_yield=5,prod_bonus=.15)
        #We're combining nuclear and solar plants since we're not looking at strategic resource counts
        self.building_lookup = { granary.name:granary, library.name:library \
        ,stoneworks.name:stoneworks, watermill.name:watermill, market.name:market \
        , university.name:university, workshop.name:workshop, bank.name:bank \
        , observatory.name:observatory, windmill.name:windmill, factory.name:factory \
        , hospital.name:hospital, public_school.name:public_school, stock_exchange.name:stock_exchange \
        , research_lab.name:research_lab, power_plant.name:power_plant}
        
        #TODO List of grids
    def cellInit(self,mapName):
        pass
