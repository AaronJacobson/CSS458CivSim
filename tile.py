import numpy as N
import classlookup

class Tile(object):
    """
    Summary:
        Tile class stors and controls what is stored in a single tile. This
        includes what kind of biome is on the tile and what yeids does it produce.
        Notice that tile does include improvments to yields that can be caused
        by irrigation/mines and buildings.
    """
    def __init__(self,grid,y=-1,x=-1,biome="none",elevation="none",terrain="none",unique_resource=None,food_yield=0,prod_yield=0,\
    science_yield=0,gold_yield=0, road=False, river = False):
        """
        Summary:
            This is a construtor that intializes all the values that belong in a tile.

        Method Arguments:
            y*:         the height of the grid to be created.
            x*:         the length of the grid to be created.
            biome*:     a string that holds the biome of the tile.
                        (snow/tundra/desert/plain/grassland)
            elevation*: a string that holds the elevation of the tile.
                        (hill/clear)
            terrain*:   a string that holds the terrain of the tile.
                        (forrest/jungle/clear)
            unique_resource*: a string that holds a resource of the tile.
            science_yield*: an integer that holds the science output of the tile.
            gold_yield*: an integer that holds the gold output of the tile.
            road*: a bool that determins if there is a road on the tile.
            river*: a bool that determins if a river flows next to the tile.
        """
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
        self.look = classlookup.ClassLookUp()

    def set_owner(self,civ):
        '''
        Setter for the civilization that owns this tile.
        '''
        self.owner = civ

    def get_science_yield(self):
        '''
        Deternins the science yield of a tile by looking at its biome and terrain and
        buildings that influence the area.

        '''
        science_bonus = 0
        if not (self.city == None):
            if(self.city.has_university == True):
                if(self.terrain == "jungle"):
                    science_bonus += 2
        return (self.science_yield + science_bonus)

    def get_prod_yield(self):
        '''
        Deternins the production yield of a tile by looking at its biome and terrain and
        buildings that influence the area.

        '''
        prod_bonus = 0
        if not (self.city == None):
            if(self.city.has_hydro_plant == True):
                if(self.near_river == True):
                    prod_bonus += 1
        if not (self.owner == None):
            if(self.improvement == "mine"):
                if(self.owner.science >= self.look.researchVal[8]*self.owner.science_cost_multiplier()):
                    prod_bonus += 1
            if(self.improvement == "lumber_mill"):
                if(self.owner.science >= self.look.researchVal[9]*self.owner.science_cost_multiplier()):
                    prod_bonus += 1
        return (self.prod_yield + prod_bonus)

    def get_food_yield(self):
        '''
        Determins the food yield of a tile by looking at its biome, terrain, and
        buildings that influence the area.

        '''
        food_bonus = 0
        if not (self.owner == None):
            if(self.improvement == "farm"):
                if(self.owner.science >= self.look.researchVal[5]*self.owner.science_cost_multiplier()):
                    if(self.near_river == True):
                        food_bonus += 1
                if(self.owner.science >= 4530):
                    food_bonus += 1
        return (self.food_yield + food_bonus)

    def get_gold_yield(self):
        '''
        Determins the gold yield of a tile by looking at its biome, terrain, and
        buildings that influence the area.

        '''
        gold_bonus = 0
        if not (self.owner == None):
            if(self.improvement == "trading_post"):
                if(self.owner.science >= self.look.researchVal[8]*self.owner.science_cost_multiplier()):
                    gold_bonus += 1
        return (self.gold_yield + gold_bonus)

    #TODO change how to deal with improvements
    def add_improvement(self, name):
        '''
        Adds an improvment to the tile. This will change what the tiles yeilds are,
        so the yeild changing methods are invocked.

        Method Arguments:
            name: name of the improvment added to the tile.
        '''
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
        """
        Summary:
            Returns a list of tiles that are the "neighbor" of this tile. For 
            distance = 1, will return the 6 closest. If distance > 1, will get the
            neighbors based on their distance in the tile grid, which isn't
            completely accurate, it will give additional tiles.
            
        Method Arguments:
            distance*:      The "radius" of the shape of the tiles in the returned list.
            
        """
        list_of_neighbors = []
        #Special case to properly get the first layer of tiles.
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
            #dirty way of getting the surrounding nodes, would have to special
            #case each node or use recurision to be more accurate. When distance
            #is large the recursion went to the recursion limit.
            y_coords = N.arange(1+distance*2)-distance+self.y
            x_coords = N.arange(1+distance*2)-distance+self.x
            for row in range(1+distance*2):
                for col in range(1+distance*2):
                    x_actual = x_coords[col]
                    while x_actual < -1*(self.grid.x-1):
                        x_actual += self.grid.x
                    while x_actual > self.grid.x-1:
                        x_actual -= self.grid.x
                        
                    if y_coords[row] >= 0 and y_coords[row] < self.grid.y:
                        # if x_actual < self.grid.x:
                        if y_coords[row] == self.y and x_actual == self.x:
                            pass #found yourself
                        else:
                            # print("y " + str(y_coords[row]) + " x " + str(x_actual))
                            list_of_neighbors.append(self.grid.tiles[y_coords[row],x_actual])
        return list_of_neighbors

    
    def total_yield(self,food_coefficient=1.0,prod_coefficient=1.0,science_coefficient=1.0,gold_coefficent=1.0):
        """
        Summary:
            Adds the yields together to get a simple way of determining the overall
            "value" of the tile.
        Method Arguments:
            food_coefficient*:      The value to determine how much to weight food.
            prod_coefficient*:      The value to determine how much to weight production.
            science_coefficient*:   The value to determine how much to weight science.
            gold_coefficient*:      The value to determine how much to weight gold.
        """
        return int(self.get_food_yield() * food_coefficient + self.get_prod_yield() * prod_coefficient \
        + self.get_science_yield() * science_coefficient + self.get_gold_yield() * gold_coefficent)

    def __lt__(self,other):
        """
        Summary:
            Returns whether the given other has a greater total yield or not.
        Method Arguments:
            other*: The other tile to compare this one to.
        """
        if self.owner != None:
            return self.total_yield(food_coefficient=self.owner.tile_food_value_coef,\
                prod_coefficient=self.owner.tile_prod_value_coef,\
                science_coefficient=self.owner.tile_science_value_coef,
                gold_coefficent=self.owner.tile_gold_value_coef) < \
                other.total_yield(food_coefficient=self.owner.tile_food_value_coef,\
                prod_coefficient=self.owner.tile_prod_value_coef,\
                science_coefficient=self.owner.tile_science_value_coef,
                gold_coefficent=self.owner.tile_gold_value_coef)
        else:
            return self.totol_yield() < other.total_yield()