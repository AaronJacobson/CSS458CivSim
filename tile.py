import numpy as N
import classlookup

class Tile(object):
    """
    """
    def __init__(self,grid,y=-1,x=-1,biome="grassland",elevation="none",terrain="none",unique_resource=None,food_yield=0,prod_yield=0,\
    science_yield=0,gold_yield=0, road=False, river = False):
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
        self.close_to_city = False
        self.owner = None
        self.food_yield = food_yield
        self.prod_yield = prod_yield
        self.science_yield = science_yield
        self.gold_yield = gold_yield
        self.road = road
        self.near_river = river
        self.get_neighbors_checked = False
        self.worked = False
        self.improvement_turns = -1
        
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

    def get_science_yield(self):
        science_bonus = 0
        if(self.city.has_university == True):
            if(self.terrain == "jungle"):
                science_bonus += 2
        return (self.science_yield + science_bonus)
        
    def get_prod_yield(self):
        prod_bonus = 0
        if(self.city.has_hydro_plant == True):
            if(self.near_river == True):
                prod_bonus += 1
        if(self.improvement == "mine"):
            if(self.owner.science >= 2930):
                prod_bonus += 1
        if(self.improvement == "lumber_mill"):
            if(self.owner.science >= 4530):
                prod_bonus += 1
        return (self.prod_yield + prod_bonus)
        
    def get_food_yield(self):
        food_bonus = 0
        if(self.improvement == "farm"):
            if(self.owner.science >= 625):
                if(self.near_river == True):
                    food_bonus += 1
            if(self.owner.science >= 4530):
                food_bonus += 1
        return (self.food_yield + food_bonus)
        
    def get_gold_yield(self):
        gold_bonus = 0
        if(self.improvement == "trading_post"):
            if(self.owner.science >= 2930):
                gold_bonus += 1
        return (self.gold_yield + gold_bonus)

    #TODO change how to deal with improvements
    def add_improvement(self, name):
        if(self.improvement == None):
            self.improvement = name
            improvement = classlookup.ClassLookUp.improvement_lookup[name]
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
        if distance == 1:
            if self.y > 0:
                list_of_neighbors.append(self.grid.tiles[self.y-1,self.x])
            if self.y % 2 == 0:
                #even row
                list_of_neighbors.append(self.grid.tiles[self.y-1,self.x-1])
            else:
                #odd row
                if self.x+1 == self.grid.x:
                    #list_of_neighbors.append(self.grid.tiles[self.y-1,0])
                    pass
                else:
                    list_of_neighbors.append(self.grid.tiles[self.y-1,self.x+1])

            list_of_neighbors.append(self.grid.tiles[self.y,self.x-1])
            if self.x+1 == self.grid.x:
                #list_of_neighbors.append(self.grid.tiles[self.y,0])
                pass
            else:
                list_of_neighbors.append(self.grid.tiles[self.y,self.x+1])

            if self.y < self.grid.y - 1:
                list_of_neighbors.append(self.grid.tiles[self.y+1,self.x])
                if self.y % 2 == 0:
                    #even row
                    list_of_neighbors.append(self.grid.tiles[self.y+1,self.x-1])
                else:
                    #odd row
                    if self.x+1 == self.grid.x:
                        #list_of_neighbors.append(self.grid.tiles[self.y+1,0])
                        pass
                    else:
                        list_of_neighbors.append(self.grid.tiles[self.y+1,self.x+1])
        else:
            y_coords = N.arange(1+distance*2)-distance+self.y
            x_coords = N.arange(1+distance*2)-distance+self.x
            for row in range(1+distance*2):
                for col in range(1+distance*2):
                    if y_coords[row] >= 0 and y_coords[row] < self.grid.y \
                    and x_coords[col] >= 0 and x_coords[col] < self.grid.x:
                        if y_coords[row] == self.y and x_coords[col] == self.x:
                            pass #found yourself
                        else:
                            list_of_neighbors.append(self.grid.tiles[y_coords[row],x_coords[col]])
        return list_of_neighbors

    def total_yield(self,food_coefficient=1.0,prod_coefficient=1.0,science_coefficient=1.0,gold_coefficent=1.0):
        return int(self.get_food_yield() * food_coefficient + self.get_prod_yield() * prod_coefficient \
        + self.get_science_yield() * science_coefficient + self.get_gold_yield() * gold_coefficent)

if __name__ == "__main__":
    #Moved this in here to prevent circular imports

    from grid import Grid

    test_grid = Grid(50,50)
    list_of_tiles = test_grid.tiles[2,2].get_neighbors(distance=1)
    for tile in list_of_tiles:
        print("y " + str(tile.y) + " x " + str(tile.x))
    print("length: " + str(len(list_of_tiles)))
