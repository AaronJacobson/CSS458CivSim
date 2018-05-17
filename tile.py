class Tile(object):
    
    def __init__(self,grid,y,x,biome,elevation,terrain,food_yield=0,prod_yield=0,\
    science_yield=0,gold_yield=0):
        self.grid = grid
        self.y = y
        self.x = x
        self.elevation = elevation
        self.biome = biome
        self.terrain = terrain
        #is this how we should deal with cities and units?
        self.unit = None
        self.city = None
        self.owner = None
        self.food_yield = food_yield
        self.prod_yield = prod_yield
        self.science_yield = science_yield
        self.gold_yield = gold_yield
        
        #TODO init yields based on elevation and biome
        #TODO manage roads, won't change yields
        #TODO manage improvements
