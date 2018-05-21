
#Import Statements
from grid import Grid
from building import Building
from civilization import Civ
from unit import Unit
import numpy as N
import os

class Game(object):
    """
    """
    def __init__(self,y=50,x=100,numTurns=500):
        """
        """
        #Initialize Dictionaries
        #NEEDS YIELD DICTIONARY
        self.initBuildingLookUp()
        self.initBuildingResearch()
        self.initUnitResearch()
        self.initUnitLookUp()
        
        #Initialize Total Turns
        self.num_turns = numTurns
        
        #Initialize tile grids and civ list
        self.civs = None
        self.turns = []
        
        #Fill grid values and civ list
        self.simInit()
        #TODO initialize the list/dictionary of biomes and they're yields
        #TODO List of grids\
        
    def initBuildingLookUp(self):
        """
        """
        granary = Building(name="granary",gold_yield=-1,food_yield=2)
        library = Building(name="library",gold_yield=-1,science_pop_bonus=.5)
        stoneworks = Building(name="stoneworks",gold_yield=-1,prod_yield=1)
        watermill = Building(name="watermill",gold_yield=-2,food_yield=2,prod_yield=1)
        market = Building(name="market",gold_yield=2,gold_bonus=.25)
        university = Building(name="university",gold_yield=-2,science_bonus=.33)
        workshop = Building(name="workshop",gold_yield=-2,prod_yield=2,prod_bonus=.1)
        bank = Building(name="bank",gold_yield=2,gold_bonus=.25)
        observatory = Building(name="observatory",science_bonus=.5)
        #We're ignoring the clause of windmill only helping building construction
        windmill = Building(name="windmill",gold_yield=-2,prod_yield=2,prod_bonus=.1)
        factory = Building(name="factory",gold_yield=-3,prod_yield=4,prod_bonus=.1)
        hospital = Building(name="hospital",gold_yield=-2,food_yield=5)
        public_school = Building(name="public_school",gold_yield=-3,science_yield=3,science_pop_bonus=.5)
        stock_exchange = Building(name="stock_exchange",gold_yield=3,gold_bonus=.33)
        research_lab = Building(name="research_lab",gold_yield=-3,science_yield=4,science_bonus=.5)
        #We're combining nuclear and solar plants since we're not looking at strategic resource counts
        power_plant = Building(name="power_plant",gold_yield=-3,prod_yield=5,prod_bonus=.15)
        self.building_lookup = { granary.name:granary, library.name:library \
        ,stoneworks.name:stoneworks, watermill.name:watermill, market.name:market \
        , university.name:university, workshop.name:workshop, bank.name:bank \
        , observatory.name:observatory, windmill.name:windmill, factory.name:factory \
        , hospital.name:hospital, public_school.name:public_school, stock_exchange.name:stock_exchange \
        , research_lab.name:research_lab, power_plant.name:power_plant}
        
    def initUnitLookUp(self):
        """
        """
        warrior = Unit(name="warrior",atype="melee",prod_cost=40,speed=2,strength=8)
        settler = Unit(name="settler",atype="civilian",prod_cost=106,speed=2)
        scout = Unit(name="scout",atype="melee",prod_cost=25,speed=2,strength=5)
        archer = Unit(name="archer",atype="archery",prod_cost=40,speed=2,strength=5,\
        range_strength=7,rangeSize=2)
        spearman = Unit(name="spearman",atype="melee",prod_cost=56,speed=2,strength=11)
        chariot_archer = Unit(name="chariot_archer",atype="mounted",speed=4,strength=6,\
        range_strength=10,rangeSize=2)
        swordsman = Unit(name="swordsman",atype="melee",prod_cost=75,speed=2,strength=14)
        horseman = Unit(name="horseman",atype="mounted",prod_cost=75,speed=4,strength=12)
        composite_bowman = Unit(name="composite_bowman",atype="archery",prod_cost=75,speed=2,\
        strength=7,range_strength=11,rangeSize=2)
        catapult = Unit(name="catapult",atype="siege",prod_cost=75,speed=2,strength=7,\
        range_strength=8,rangeSize=2)
        crossbowman = Unit(name="crossbowman",atype="archery",prod_cost=120,speed=2,strength=13,\
        range_strength=8,rangeSize=2)
        longswordsman = Unit(name="longswordsman",atype="melee",prod_cost=120,speed=2,strength=21)
        knight = Unit(name="knight",atype="mounted",prod_cost=120,speed=4,strength=20)
        trebuchet = Unit(name="trebuchet",atype="siege",prod_cost=120,speed=2,strength=12,\
        range_strength=14,rangeSize=2)
        musketman = Unit(name="musketman",atype="gunpowder",prod_cost=150,speed=2,strength=24)
        lancer = Unit(name="lancer",atype="mounted",prod_cost=185,speed=4,strength=25)
        cannon = Unit(name="cannon",atype="siege",prod_cost=185,speed=2,strength=14,\
        range_strength=20,rangeSize=2)
        rifleman = Unit(name="rifleman",atype="gunpoweder",prod_cost=225,speed=2,strength=34)
        cavalry = Unit(name="cavalry",atype="mounted",prod_cost=225,speed=4,strength=34)
        gatling_gun = Unit(name="gatling_gun",atype="archery",prod_cost=225,strength=30,\
        range_strength=36,rangeSize=1)
        machine_gun = Unit(name="machine_gun",atype="archery",prod_cost=350,speed=2,strength=60,\
        range_strength=60,rangeSize=1)
        great_war_infantry = Unit(name="great_war_infantry",atype="gunpowder",prod_cost=320,\
        speed=2,strength=50)
        landship = Unit(name="landship",atype="armor",prod_cost=350,speed=4,strength=60)
        infantry = Unit(name="infantry",atype="gunpowder",prod_cost=320,speed=2,strength=70)
        artillery = Unit(name="artillery",atype="siege",prod_cost=250,speed=2,strength = 21,\
        range_strength=28,rangeSize=3)
        tank = Unit(name="tank",atype="armor",prod_cost=375,speed=5,strength=70)
        paratrooper = Unit(name="paratrooper",atype="gunpowder",prod_cost=375,speed=2,\
        strength=65,airdrop=5)
        bazooka = Unit(name="bazooka",atype="archery",prod_cost=375,speed=2,strength=85,\
        range_strength=85,rangeSize=1)
        helicopter = Unit(name="helicopter",atype="helicopter",prod_cost=425,speed=6,strength=60)
        rocket_artillery = Unit(name="rocket_artillery",atype="siege",prod_cost=425,speed=3,\
        strength=45,range_strength=60,rangeSize=3)
        mobile_sam = Unit(name="mobile_sam",atype="gunpowder",prod_cost=425,speed=3,strength=65)
        modern_armor = Unit(name="modern_armor",atype="armor",prod_cost=425,speed=5,strength=100)
        mech_infantry = Unit(name="mech_infantry",atype="gunpowder",prod_cost=375,speed=3,strength=90)
        xcom_squad = Unit(name="xcom_squad",atype="gunpowder",prod_cost=400,speed=2,strength=110,airdrop=40)
        giant_death_robot = Unit(name="giant_death_robot",atype="armor",prod_cost=425,speed=5,strength=150)
        
        self.unit_lookup = {warrior.name:warrior,settler.name:settler,scout.name:scout,\
        archer.name:archer, spearman.name:spearman, chariot_archer.name:chariot_archer,\
        swordsman.name:swordsman,horseman.name:horseman,composite_bowman.name:composite_bowman,\
        catapult.name:catapult,crossbowman.name:crossbowman,longswordsman.name:longswordsman,\
        knight.name:knight,trebuchet.name:trebuchet,musketman.name:musketman,lancer.name:lancer,\
        cannon.name:cannon,rifleman.name:rifleman,cavalry.name:cavalry,gatling_gun.name:gatling_gun,\
        machine_gun.name:machine_gun,great_war_infantry.name:great_war_infantry,\
        landship.name:landship,infantry.name:infantry,artillery.name:artillery,\
        tank.name:tank,paratrooper.name:paratrooper,bazooka.name:bazooka,\
        helicopter.name:helicopter,rocket_artillery.name:rocket_artillery,\
        mobile_sam.name:mobile_sam,modern_armor.name:modern_armor,mech_infantry.name:mech_infantry,\
        xcom_squad.name:xcom_squad,giant_death_robot.name:giant_death_robot}
            
    def initBuildingResearch(self):
        """
        """
        researchVal = [35,55,85,175,275,375,780,1150,1600,2350,3100,4100,5100,6400,7700,8800]
        #REMOVE PIKEMAN?
        buildingResearch = [["archer"],["chariot_archer","spearman"],["horseman","composite_bowman"],["swordsman"],["pikeman"],["knight","crossbowman","trebuchet","longswordsman"],
        ["musketman"],["lancer","cannon"],["rifleman","cavalry","gatling_gun"],["artillery"],["great_war_infantry"],["infantry","machine_gun","landship"],["marine","paratrooper","tank","Anti-tank_gun"],
        ["bazooka","rocket_artillery","helicopter","mobile_sam"],["mech_infantry","modern_armor"],["xcom_squad","death_robot"]]
    
    
    def initUnitResearch(self):
        """
        """
        pass
        
    def simInit(self,mapName="DefaultMap"):
        """
        """
        if os.path.isdir(os.path.dirname(__file__)+"\\"+mapName):
            os.chdir(os.path.dirname(__file__)+"\\"+mapName)
            #RUN INTERPRETER HERE TO FILL CIVLIST + TURNS FROM CURRENT WORKING DIRECTORY
        
    def run():
        """
        """
        pass