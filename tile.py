import numpy as N
import classlookup

class Tile(object):
    """
    """
    def __init__(self,grid,y=-1,x=-1,biome="none",elevation="none",terrain="none",unique_resource=None,food_yield=0,prod_yield=0,\
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
        

    def set_owner(self,civ):
        self.owner = civ

    def get_science_yield(self):
        science_bonus = 0
        if not (self.city == None):
            if(self.city.has_university == True):
                if(self.terrain == "jungle"):
                    science_bonus += 2
        return (self.science_yield + science_bonus)
        
    def get_prod_yield(self):
        prod_bonus = 0
        if not (self.city == None):
            if(self.city.has_hydro_plant == True):
                if(self.near_river == True):
                    prod_bonus += 1
        if not (self.owner == None):
            if(self.improvement == "mine"):
                if(self.owner.science >= 2930):
                    prod_bonus += 1
            if(self.improvement == "lumber_mill"):
                if(self.owner.science >= 4530):
                    prod_bonus += 1
        return (self.prod_yield + prod_bonus)
        
    def get_food_yield(self):
        food_bonus = 0
        if not (self.owner == None):
            if(self.improvement == "farm"):
                if(self.owner.science >= 625):
                    if(self.near_river == True):
                        food_bonus += 1
                if(self.owner.science >= 4530):
                    food_bonus += 1
        return (self.food_yield + food_bonus)
        
    def get_gold_yield(self):
        gold_bonus = 0
        if not (self.owner == None):
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
                        list_of_neighbors.append(self.grid.tiles[self.y-1,0])
                        pass
                    else:
                        list_of_neighbors.append(self.grid.tiles[self.y-1,self.x+1])
                        
            list_of_neighbors.append(self.grid.tiles[self.y,self.x-1])
            if self.x+1 == self.grid.x:
                list_of_neighbors.append(self.grid.tiles[self.y,0])
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
                        list_of_neighbors.append(self.grid.tiles[self.y+1,0])
                        pass
                    else:
                        list_of_neighbors.append(self.grid.tiles[self.y+1,self.x+1])
        else:
            y_coords = N.arange(1+distance*2)-distance+self.y
            x_coords = N.arange(1+distance*2)-distance+self.x
            for row in range(1+distance*2):
                for col in range(1+distance*2):
                    x_actual = x_coords[col]
                    while x_actual >= self.grid.x:
                        x_actual -= (self.grid.x+1)
                    
                    if y_coords[row] >= 0 and y_coords[row] < self.grid.y:
                        if x_actual >= 0 and x_actual < self.grid.x:
                            if y_coords[row] == self.y and x_actual == self.x:
                                pass #found yourself
                            else:
                                # print("y " + str(y_coords[row]) + " x " + str(x_actual))
                                list_of_neighbors.append(self.grid.tiles[y_coords[row],x_actual])
        return list_of_neighbors

    def total_yield(self,food_coefficient=1.0,prod_coefficient=1.0,science_coefficient=1.0,gold_coefficent=1.0):
        return int(self.get_food_yield() * food_coefficient + self.get_prod_yield() * prod_coefficient \
        + self.get_science_yield() * science_coefficient + self.get_gold_yield() * gold_coefficent)
        
    def __lt__(self,other):
        return self.total_yield() < other.total_yield()