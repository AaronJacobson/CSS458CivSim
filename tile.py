class Tile(object):
    
    def __init__(self,grid,y,x,biome,elevation,terrain,food_yield=0,prod_yield=0,\
    science_yield=0,gold_yield=0, road=0):
        self.grid = grid
        self.y = y
        self.x = x
        self.elevation = elevation
        self.biome = biome
        self.terrain = terrain
        #is this how we should deal with cities and units?
        self.improvement = None
        self.unit = None
        self.city = None
        self.owner = None
        self.food_yield = food_yield
        self.prod_yield = prod_yield
        self.science_yield = science_yield
        self.gold_yield = gold_yield
        self.road = road
        
    """
    Roads take 2 turns to build. Road is set to .5 when starting to build.
    on following turn, processing turn will increase number to 1 to represent
    a built road. Railroad will be represented the same way, but with 1.5 and 2.
    """
    def build_road():
        self.road = 0.5
    def build_railroad():
        if(self.road == 1):
            self.road = 1.5
            
    def process_turn():
        if(self.road == 0.5):
            self.road = 1
        if(self.road == 1.5):
            self.road = 2
        #TODO add processing new improvement for the turn
        
    #Class calls with amount needed to improve resource
    def improve_food(amount):
        self.food_yield += amount
    def improve_prod(amount):
        self.prod_yield += amount
    def improve_science(amount):
        self.science_yield += amount
    def improve_gold(amount):
        self.gold_yield += amount
        
        #TODO init yields based on elevation and biome
        #TODO manage roads, won't change yields
        #TODO manage improvements
