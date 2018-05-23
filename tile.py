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
    def build_road(self):
        self.road = 0.5
    def build_railroad(self):
        if(self.road == 1):
            self.road = 1.5
            
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

    def get_neighbors(self):
        list_of_neighbors = []
        if self.y > 0:
            list_of_neighbors.append(self.grid.tiles[self.y-1,self.x])
            if self.y % 2 == 0:
                #even row
                list_of_neighbors.append(self.grid.tiles[self.y-1,self.x-1])
            else:
                #odd row
                list_of_neighbors.append(self.grid.tiles[self.y-1,self.x+1])#TODO check if it's on the edge of the map
        list_of_neighbors.append(self.grid.tiles[self.y,self.x-1])
        list_of_neighbors.append(self.grid.tiles[self.y,self.x+1])#TODO check if it's on the edge of the map
        if self.y < self.grid.y - 1:
            list_of_neighbors.append(self.grid.tiles[self.y+1,self.x])
            if self.y % 2 == 0:
                #even row
                list_of_neighbors.append(self.grid.tiles[self.y+1,self.x-1])
            else:
                #odd row
                list_of_neighbors.append(self.grid.tiles[self.y+1,self.x+1])#TODO check if it's on the edge of the map
        return list_of_neighbors