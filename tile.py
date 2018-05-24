from game import Game

class Tile(object):
    
    def __init__(self,grid,y,x,biome,elevation,terrain,unique_resource,food_yield=0,prod_yield=0,\
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
            
    def add_improvement(self, name):
        if(self.improvement == None):
            self.improvement = name
            improvement = Game.improvement_lookup[name]
            improve_food(improvement.food_yield)
            improve_prod(improvement.prod_yield)
            improve_gold(improvement.gold_yield)
            improve_science(improvement.science_yield)
            
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

    def get_neighbors(self,radius=1):
        list_of_neighbors = []
        list_of_neighbors = self.get_neighbors_recursive(list_of_neighbors,radius=radius)
        for tile in list_of_neighbors:
            tile.get_neighbors_check = False
        return list_of_neighbors
    
    def get_neighbors_recursive(self,neighbor_list,radius=1):
        if not self.get_neighbors_check and radius > 0:
            self.get_neighbors_check = True
            if self.y > 0:
                neighbor_list.append(self.grid.tiles[self.y-1,self.x])
                if self.y % 2 == 0:
                    #even row
                    neighbor_list.append(self.grid.tiles[self.y-1,self.x-1])
                else:
                    #odd row
                    if self.x+1 == self.grid.x:
                        neighbor_list.append(self.grid.tiles[self.y-1,0])
                    else:
                        neighbor_list.append(self.grid.tiles[self.y-1,self.x+1])
            
            neighbor_list.append(self.grid.tiles[self.y,self.x-1])
            if self.x+1 == self.grid.x:
                neighbor_list.append(self.grid.tiles[self.y,0])
            else:
                neighbor_list.append(self.grid.tiles[self.y,self.x+1])
            
            if self.y < self.grid.y - 1:
                neighbor_list.append(self.grid.tiles[self.y+1,self.x])
                if self.y % 2 == 0:
                    #even row
                    neighbor_list.append(self.grid.tiles[self.y+1,self.x-1])
                else:
                    #odd row
                    if self.x+1 == self.grid.x:
                        neighbor_list.append(self.grid.tiles[self.y+1,0])
                    else:
                        neighbor_list.append(self.grid.tiles[self.y+1,self.x+1])
        for tile in neighbor_list:
            tile.get_beighbors_recursive(neighbor_list,radius=radius-1)
        return neighbor_list