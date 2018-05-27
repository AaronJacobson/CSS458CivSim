from heapq import heappush,heappop
import classlookup
import unit
import random

class City(object):
    
    def __init__(self,grid,y,x,civ):
        self.grid = grid
        self.y = y
        self.x = x
        self.civ = civ
        self.building_list = []
        self.tile_list = []
        self.pop = 1
        self.food = 0
        self.production = 0
        self.to_build = None
        self.health = 200
        self.strength = 8 #this depends on many factors
        self.border_growth_count = 0
        self.border_distance = 1
        self.has_hydro_plant = False
        self.has_university = False
        """
        self.set_close_to_city()
        self.tile_list = self.grid.tiles[y,x].get_neighbors(distance=1)
        self.tile_list.append(self.grid.tiles[y,x])
        self.grid.tiles[y,x].has_city = True
        for tile in self.tile_list:
            tile.city = self
            tile.owner = self.civ
        """
    
    def set_close_to_city(self):
        close_tiles = self.grid.tiles[self.y,self.x].get_neighbors(distance=3)
        for tile in close_tiles:
            tile.close_to_city = True
        self.grid.tiles[self.y,self.x].close_to_city = True
    
    def get_food_yield(self):
        food_yield = 0
        total_bonus = 0
        for tile in self.tile_list:
            if tile.worked:
                food_yield = food_yield + tile.food_yield
        for building in self.building_list:
            food_yield = food_yield + building.food
            total_bonus = total_bonus + building.food_bonus
        food_yield = food_yield * (1.0 + total_bonus)
        return food_yield
    
    def get_prod_yield(self):
        prod_yield = 0
        total_bonus = 0
        for tile in self.tile_list:
            if tile.worked:
                prod_yield = prod_yield + tile.prod_yield
        for building in self.building_list:
            prod_yield = prod_yield + building.production
            total_bonus = total_bonus + building.production_bonus
        prod_yield = prod_yield * (1.0 + total_bonus)
        return prod_yield
    
    def get_science_yield(self):
        science_yield = 0
        total_bonus = 0
        for tile in self.tile_list:
            if tile.worked:
                science_yield = science_yield + tile.science_yield
        for building in self.building_list:
            science_yield = science_yield + building.science
            total_bonus = total_bonus + building.science_bonus
        science_yield = science_yield * (1.0 + total_bonus)
        return science_yield
    
    def get_gold_yield(self):
        gold_yield = 0
        total_bonus = 0
        for tile in self.tile_list:
            if tile.worked:
                gold_yield = gold_yield + tile.gold_yield
        for building in self.building_list:
            gold_yield = gold_yield + building.gold
            total_bonus = total_bonus + building.gold_bonus
        gold_yield = gold_yield * (1.0 + total_bonus)
        return gold_yield
    
    def food_to_grow(self,pop):
        return int(15 + 6*(pop-1) + (pop-1.0)**1.8)
    
    def has_building(self,name_to_find):
        for building in self.building_list:
            if name_to_find == building.name:
                return True
        return False
        
    def choose_production(self,yield_coef=1.0,food_val_coef=1.0,prod_val_coef=1.0,\
    science_val_coef=1.0,gold_val_coef=1.0,settler_chance=.1,unit_chance=.4):
        look = classlookup.ClassLookUp()
        building_heap = []
        unit_heap = []
        for i in range(len(look.researchVal)):
            if self.civ.science >= look.researchVal[i]:
                building_stage = look.buildingResearch[i]
                unit_stage = look.unitResearch[i]
                for name in building_stage:
                    if not self.has_building(name):
                        building = look.building_lookup[name]
                        priority = building.prod_cost
                        food = (building.food + building.food_bonus*self.get_food_yield()) * food_val_coef
                        prod = (building.production + building.production_bonus*self.get_prod_yield()) * prod_val_coef
                        science = (building.science + building.science_bonus*self.get_science_yield()) * science_val_coef
                        gold = (building.gold + building.gold_bonus*self.get_gold_yield()) * gold_val_coef
                        priority = priority - food - prod - science - gold
                        heappush(building_heap,(priority,look.building_lookup[name]))
                for name in unit_stage:
                    if not name == "settler":
                        unit = look.unit_lookup[name]
                        unit_priority = 1.0/(unit.prod_cost+unit.strength+unit.range_strength)
                        heappush(unit_heap,(unit_priority,unit))
        decision = random.uniform(0,1)
        if decision < settler_chance:
            return look.unit_lookup["settler"]
        elif decision < unit_chance:
            return heappop(unit_heap)[1]
        else:
            return heappop(building_heap)[1]
    
    def grow_borders(self):
        self.border_distance = self.border_distance + 1
        tiles_to_add = self.grid[self.y,self.x].get_neighbors(distance=self.border_distance)
        for tile in tiles_to_add:
            if tile.owner == None:
                tile.city = self
                tile.ownder = self.civ
                self.tile_list.append(tile)
    
    def process_turn(self):
        #TODO update improvements
        
        #check food, update pop
        self.food = self.food + self.get_food_yield()
        if self.food >= self.food_to_grow(self.pop+1):
            #grow
            self.pop = self.pop + 1
            #TODO set which tile is being worked.
            self.food = 0

        #add prod, check production
        self.production = self.production + self.get_prod_yield
        if self.to_build == None:
            #choose something to build
            self.to_build = self.choose_production()
        
        if self.production >= self.to_build.prod_cost:
            #complete production
            if self.to_build.type == "building":
                self.building_list.append(self.to_build)#TODO make work with units
            else:
                if self.to_build.name == "settler":
                    self.grid.tiles[self.y,self.x].unit = unit.Unit(name="settler",atype="civilian",prod_cost=106,speed=2,y=self.y,x=self.x,civ=self.civ,grid=self.grid)
                    self.civ.unit_list.append(self.grid.tiles[self.y,self.x].unit)
                    self.grid.tiles[self.y,self.x].unit.process_turn()
                else:
                    unit = self.to_build
                    unit_to_add = unit.Unit(name=unit.name,atype=unit.atype,prod_cost=unit.prod_cost,speed=unit.speed,y=-1,x=-1,civ=self.civ)
                    self.civ.mil_unit_list.append(unit_to_add)
                    
            if self.to_build.name == "hydro_plant":#TODO make this use the lookup
                self.has_hydro_plant = True
            elif self.to_build.name == "university":
                self.has_university = True
            #choose new production
            self.to_build = self.choose_production()
            self.production = 0
        
        #growing borders
        if self.border_growth_count >= 100 and self.border_distance == 1:
            self.grow_borders()
        elif self.border_growth_count >= 200 and self.border_distance == 2:
            self.grow_borders()

        #Setting which tiles will be worked.
        heap_of_tiles = []
        for i in range(len(self.tile_list)):
            self.tile_list[i].worked = False
            heappush(heap_of_tiles,(self.tile_list[i].total_yield,i))
        for i in range(self.pop):
            self.tile_list[heappop(heap_of_tiles)[1]].worked = True
    
    def popF(self,x):
        return 959.0549*x**2.8132

    def calculate_population(self):
        look = classlookup.ClassLookUp()
        if self.pop < 10:
            return look.pop_table[self.pop]
        else:
            return self.popF(self.pop)
    
if __name__ == "__main__":
    test_city = City(None,None,None,None)
    for i in range(41):
        test_city.pop = i
        print(test_city.calculate_population())