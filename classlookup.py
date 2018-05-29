#Imports from elsewhere in Simulation
from building import Building
from unit import Unit
from improvement import Improvement

class ClassLookUp(object):
    """
    Summary:
        Contains the dictionary lookups for different classes of the simulation.
    Class Variables:
        unit_lookup*: Dictionary which contains Unit class examples containing information on each type of Unit.
        building_lookup*: Dictionary which contains Building class examples containing information on each type of Building.
        improvement_lookup*: Dictionary which contains Improvement class examples containing information on each type of Improvement.
        biome_lookup*: Dictionary which contains lists of information for each type of biome.
        terrain_lookup*: Dictionary which contains lists of information for each type of terrain.
        researchVal*: List of research values for each column of research in the Civ V Technology Tree.
        buildingResearch*: List of Lists of strings of Building names, used to determine what Buildings a Civ has unlocked.
        unitResearch*: List of Lists of strings of Unit names, used to determine what Units a Civ has unlocked.
        improvementResearch*: List of Lists of strings of Improvement names, used to determine what Improvements a Civ has unlocked.
        pop_table*: A List of population values used to determine total Civ population
    """
    def initUnitLookUp():
        """
        Summary:
                Creates Unit objects, then fills them into a dictionary and returns it.
        Output:
                A dictionary of every unit in the model.
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
        pikeman = Unit(name="pikeman",atype="melee",prod_cost=90,speed=2,strength=16)
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

        unit_lookup = {warrior.name:warrior,settler.name:settler,scout.name:scout,\
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
        xcom_squad.name:xcom_squad,giant_death_robot.name:giant_death_robot,\
        pikeman.name:pikeman }
        return unit_lookup
    
    #Create Class Dictionary for find unit information
    unit_lookup = initUnitLookUp()
    
    def initBuildingLookUp():
        """
        Summary:
                Creates Building objects, then fills them into a dictionary and returns it.
        Output:
                A dictionary of every building in the model.
        """
        granary = Building(name="granary",gold_yield=-1,food_yield=2,prod_cost=60)
        library = Building(name="library",gold_yield=-1,science_pop_bonus=.5,prod_cost=75)
        stoneworks = Building(name="stoneworks",gold_yield=-1,prod_yield=1,prod_cost=75)
        watermill = Building(name="watermill",gold_yield=-2,food_yield=2,prod_yield=1,prod_cost=75)
        market = Building(name="market",gold_yield=2,gold_bonus=.25,prod_cost=100)
        university = Building(name="university",gold_yield=-2,science_bonus=.33,prod_cost=160)
        workshop = Building(name="workshop",gold_yield=-2,prod_yield=2,prod_bonus=.1,prod_cost=120)
        bank = Building(name="bank",gold_yield=2,gold_bonus=.25,prod_cost=200)
        observatory = Building(name="observatory",science_bonus=.5,prod_cost=200)
        #We're ignoring the clause of windmill only helping building construction
        windmill = Building(name="windmill",gold_yield=-2,prod_yield=2,prod_bonus=.1,prod_cost=250)
        factory = Building(name="factory",gold_yield=-3,prod_yield=4,prod_bonus=.1,prod_cost=360)
        hospital = Building(name="hospital",gold_yield=-2,food_yield=5,prod_cost=360)
        public_school = Building(name="public_school",gold_yield=-3,science_yield=3,science_pop_bonus=.5,prod_cost=360)
        hydro_plant = Building(name="hydro_plant",gold_yield=-3,prod_cost=360)
        stock_exchange = Building(name="stock_exchange",gold_yield=3,gold_bonus=.33,prod_cost=500)
        research_lab = Building(name="research_lab",gold_yield=-3,science_yield=4,science_bonus=.5,prod_cost=500)
        #We're combining nuclear and solar plants since we're not looking at strategic resource counts
        power_plant = Building(name="power_plant",gold_yield=-3,prod_yield=5,prod_bonus=.15,prod_cost=500)
        prod_gold = Building(name="prod_gold")
        building_lookup = { granary.name:granary, library.name:library \
        ,stoneworks.name:stoneworks, watermill.name:watermill, market.name:market \
        , university.name:university, workshop.name:workshop, bank.name:bank \
        , observatory.name:observatory, windmill.name:windmill, factory.name:factory \
        , hospital.name:hospital, public_school.name:public_school, stock_exchange.name:stock_exchange \
        , research_lab.name:research_lab, power_plant.name:power_plant\
        , hydro_plant.name:hydro_plant, prod_gold.name:prod_gold}
        return building_lookup
    
    #Create class dictionary for finding building information
    building_lookup = initBuildingLookUp()
    
    def initImprovementLookUp():
        """
        Summary:
                Creates Improvement objects, then fills them into a dictionary and returns it.
        Output:
                A dictionary of every improvement in the model.
        """
        farm = Improvement(name='farm',food_yield=1)
        fort = Improvement(name='fort',strength_mod=0.50)
        lumber_mill = Improvement(name='lumber_mill',prod_yield=1)
        mine = Improvement(name='mine',prod_yield=1)
        trading_post = Improvement(name='trading_post',gold_yield=1)
        improvement_lookup = {farm.name:farm,fort.name:fort,lumber_mill.name:lumber_mill,
        mine.name:mine,trading_post.name:trading_post}
        return improvement_lookup
    
    #Create class dictionary for finding improvement information
    improvement_lookup = initImprovementLookUp()
    
    #Reasearch creation
    researchVal = [    0,    35,    90,   175,   350,   625,  1000,  1780,  2930,
        4530,  6880,  9980, 14080, 19180, 25580, 33280, 42080]
    buildingResearch = [[],["granary"],["library","stoneworks","watermill"],[],["market"],["workshop"],["university"],
        ["bank","observatory"],["windmill"],["factory","public_school"],["hospital","stock_exchange"],[],["research_lab"],[],["power_plant"],[],[]]
    unitResearch = [["warrior","settler","scout"],["archer"],["chariot_archer","spearman"],["horseman","composite_bowman"],
        ["swordsman"],["pikeman"],["knight","crossbowman","trebuchet","longswordsman"],
        ["musketman"],["lancer","cannon"],["rifleman","cavalry","gatling_gun"],["artillery"],
        ["great_war_infantry"],["infantry","machine_gun","landship"],["paratrooper","tank"],
        ["bazooka","rocket_artillery","helicopter","mobile_sam"],["mech_infantry","modern_armor"],["xcom_squad","giant_death_robot"]]
    improvementResearch =[['farm'],['mine'],['lumber_mill'],['fort'],['trading_post'],[],[],[],[],[],[],[],[],[],[],[],[]]
    
    
    #Class Biome Definition
    #Biome name, Food Val, Prod Val, Gold Val, Movement Cost, Strength Mod, Map Color
    desert = ["desert",0,0,0,1,0,'beige']
    grassland = ["grassland",1,2,2,1,0,'darkseagreen']
    plains = ["plains",1,1,0,1,0,'y']
    snow = ["snow",0,0,0,1,0,'snow']
    tundra = ["tundra",1,0,0,1,0,'silver']
    biome_lookup = {desert[0]:desert,grassland[0]:grassland,plains[0]:plains,snow[0]:snow,tundra[0]:tundra}
    
    #Class Terrain Definition
    #Terrain name, Food Val, Prod Val, Gold Val, Movement Cost, Strength Mod, Map Color
    hill = ["hill",0,2,0,2,0.25,'olive']
    forest = ["forest",1,1,0,2,0.25,'green']
    jungle = ["jungle",2,0,0,2,0.25,'darkgreen']
    terrain_lookup = {hill[0]:hill,forest[0]:forest,jungle[0]:jungle}
    
    #Population relation Table Definition
    pop_table = [1000,1000,6000,21000,48000,90000,150000,232000,337000,469000]
    