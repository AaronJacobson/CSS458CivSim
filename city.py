from heapq import heappush,heappop

class City(object):
    
    def __init__(self,grid,y,x,civ_number):
        self.grid = grid
        self.y = y
        self.x = x
        self.civ_number = civ_number
        self.building_list = []
        self.tile_list = []
        self.pop = 1
        self.food = 0
        self.production = 0
        self.to_build = None
        self.health = 200
        self.strength = 8 #this depends on many factors
        
        self.set_close_to_city()
        self.tile_list = self.grid.tiles[y,x].get_neighbors(distance=1)
        self.tile_list.append(self.grid.tiles[y,x])
    
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
    
    def choose_production(self):#TODO: have a list of things that can be built, and choose one of them
        pass
    
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
            #complete building and choose another thing to build
            self.building_list.append(self.to_build)
            if self.to_build.name == "hydro_plant":#TODO make this use the lookup
                pass#TODO increase prod on river tiles

            self.to_build = self.choose_production()
            self.production = 0
        
        #Setting which tiles will be worked.
        heap_of_tiles = []
        for i in range(len(self.tile_list)):
            self.tile_list[i].worked = False
            heappush(heap_of_tiles,(self.tile_list[i].total_yield,i))
        for i in range(self.pop):
            self.tile_list[heappop(heap_of_tiles)[1]].worked = True