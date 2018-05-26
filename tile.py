import numpy as N

class Tile(object):
    """
    """
    def __init__(self,grid,y=-1,x=-1,biome="grassland",elevation="none",terrain="none",unique_resource=None,food_yield=0,prod_yield=0,\
    science_yield=0,gold_yield=0, road=0):
        self.grid = grid
        self.y = y
        self.x = x
        self.elevation = elevation
        self.biome = biome
        self.terrain = terrain
        self.unique_resource = None
        #is this how we should deal with cities and units?
        self.improvement = None
        self.unit = None
        self.city = None
        self.has_city = False
        self.owner = None
        self.food_yield = food_yield
        self.prod_yield = prod_yield
        self.science_yield = science_yield
        self.gold_yield = gold_yield
        self.road = road
        self.get_neighbors_checked = False
        
    """
    Roads take 2 turns to build. Road is set to .5 when starting to build.
    on following turn, processing turn will increase number to 1 to represent
    a built road. Railroad will be represented the same way, but with 1.5 and 2.
    """
    def build_road(self):
        self.road = 0.5
    def build_railroad(self):
        if(self.road == 1):
            self.road = 1.5
    
    def set_owner(self,civ):
        self.owner = civ
    
    #TODO change how to deal with improvements        
    def add_improvement(self, name):
        if(self.improvement == None):
            self.improvement = name
            improvement = Game.improvement_lookup[name]
            self.improve_food(improvement.food_yield)
            self.improve_prod(improvement.prod_yield)
            self.improve_gold(improvement.gold_yield)
            self.improve_science(improvement.science_yield)
            
    def move_unit(self, unit_object):
        if(self.unit == None):
            self.unit = unit_object
        
    def remove_unit(self):
        if(self.unit != None):
            self.unit = None
            
    def process_turn(self):
        if(self.road == 0.5):
            self.road = 1
        if(self.road == 1.5):
            self.road = 2
        #TODO add processing new improvement for the turn
        
    #Class calls with amount needed to improve resource
    def improve_food(self,amount):
        self.food_yield += amount
    def improve_prod(self,amount):
        self.prod_yield += amount
    def improve_science(self,amount):
        self.science_yield += amount
    def improve_gold(self,amount):
        self.gold_yield += amount
        
        #TODO init yields based on elevation and biome
        #TODO manage roads, won't change yields
        #TODO manage improvements

    def get_neighbors(self,distance=1):
        list_of_neighbors = []
        y_coords = N.arange(1+distance*2)-distance+self.y
        x_coords = N.arange(1+distance*2)-distance+self.x
        for row in range(1+distance*2):
            for col in range(1+distance*2):
                if y_coords[row] >= 0 and y_coords[row] < self.grid.y:
                    xActual = x_coords[col]
                    if xActual >= self.grid.x:
                        xActual = xActual - self.grid.x
                    if y_coords[row] == self.y and xActual == self.x:
                        pass #found yourself
                    else:
                        list_of_neighbors.append(self.grid.tiles[y_coords[row],xActual])
        return list_of_neighbors
    
    def distance(self,other):
        if type(other) == Tile:
            return ((self.x-other.x)**2+(self.y-other.y)**2)**.5

if __name__ == "__main__":
    #Moved this in here to prevent circular imports
    from grid import Grid
    
    test_grid = Grid(5,5)
    list_of_tiles = test_grid.tiles[2,0].get_neighbors(distance=2)
    for tile in list_of_tiles:
        print("x " + str(tile.x) + " y " + str(tile.y))
    print("length: " + str(len(list_of_tiles)))
