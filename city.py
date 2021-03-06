from heapq import heappush,heappop
import classlookup
import unit as tunit
import random

class City(object):

    def __init__(self,grid,y,x,civ,capitol=False):
        """
        Summary:
            Initializes the city
        Method Arguments:
            grid*: The map this city exists in.
            y*: The row this city is stored in.
            x*: The column this city is stored in.
            civ*: The civilization that owns this city.
            capitol*: True if this city is the first city built by the civilization that owns it.
        """
        self.capitol = capitol
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
        self.border_growth_count = 0
        self.border_distance = 1
        self.has_hydro_plant = False
        self.has_university = False
        self.improving_tiles = []
        self.tile_improve_heap = []

        self.set_close_to_city()
        self.tile_list = self.grid.tiles[y,x].get_neighbors(distance=1)
        self.tile_list.append(self.grid.tiles[y,x])
        self.grid.tiles[y,x].has_city = True
        self.trade_and_road_sub_coef = self.civ.city_trade_and_road_substitute_per_pop
        self.temp_gold = 0
        for tile in self.tile_list:
            if tile.city == None:
                tile.city = self
                tile.owner = self.civ
                heappush(self.tile_improve_heap,(int(tile.total_yield()),tile))
        
        self.grid.tiles[self.y,self.x].city = self#not sure if this is redundant
        



    def set_close_to_city(self):
        """
        Summary: 
            Sets the tiles around it that are too close for another city to be
            founded on.
        """
        close_tiles = self.grid.tiles[self.y,self.x].get_neighbors(distance=3)
        for tile in close_tiles:
            tile.close_to_city = True
        self.grid.tiles[self.y,self.x].close_to_city = True

    def get_food_yield(self):
        """
        Summary:
            Gets the total food yield of all the worked tiles and all the buildings
            in this city then adds the bonus by %.
        """
        food_yield = 2
        total_bonus = 0
        for tile in self.tile_list:
            if tile.worked:
                food_yield = food_yield + tile.get_food_yield()
        for building in self.building_list:
            food_yield = food_yield + building.food
            total_bonus = total_bonus + building.food_bonus
        food_yield = food_yield * (1.0 + total_bonus)
        return food_yield

    def get_prod_yield(self):
        """
        Summary:
            Gets the total production yield of all the worked tiles and all the 
            buildings in this city then adds the bonus by %.
        """
        prod_yield = 2
        total_bonus = 0
        for tile in self.tile_list:
            if tile.worked:
                prod_yield = prod_yield + tile.get_prod_yield()
        for building in self.building_list:
            prod_yield = prod_yield + building.production
            total_bonus = total_bonus + building.production_bonus
        prod_yield = prod_yield * (1.0 + total_bonus)
        return prod_yield

    def get_science_yield(self):
        """
        Summary:
            Gets the total science yield of all the worked tiles, all the buildings
            in this city, and the base for the population then adds the bonus by %.
        """
        science_yield = self.pop
        total_bonus = 0
        for tile in self.tile_list:
            if tile.worked:
                science_yield = science_yield + tile.get_science_yield()
        for building in self.building_list:
            science_yield = science_yield + building.science
            total_bonus = total_bonus + building.science_bonus
        science_yield = science_yield * (1.0 + total_bonus)
        return science_yield

    def get_gold_yield(self):
        """
        Summary:
            Gets the total gold yield of all the worked tiles and all the buildings
            in this city then adds the bonus by %.
        """
        gold_yield = 0
        total_bonus = 0
        for tile in self.tile_list:
            if tile.worked:
                gold_yield = gold_yield + tile.get_gold_yield()
        for building in self.building_list:
            gold_yield = gold_yield + building.gold
            total_bonus = total_bonus + building.gold_bonus
        gold_yield = gold_yield * (1.0 + total_bonus)
        if not self.capitol:
            gold_yield = int(gold_yield + self.pop * self.trade_and_road_sub_coef)
        return gold_yield

    def food_to_grow(self,pop):
        """
        Summary:
            Calculates the food required to grow to the next level of population
            based on the input population.
        Method Arguments:
            pop*: The population to grow from.
        """
        return int(15 + 6*(pop-1) + (pop-1.0)**1.8)

    def has_building(self,name_to_find):
        """
        Summary:
            Checks whether this city has the building with the given name.
        Method Arguments:
            name_to_find*: The name of the building to check for.
        """
        for building in self.building_list:
            if name_to_find == building.name:
                return True
        return False
    

    def choose_production(self,food_val_coef=1.0,prod_val_coef=1.0,\
    science_val_coef=1.0,gold_val_coef=1.0,settler_chance=.1,unit_chance=.1):
        """
        Summary:
            Chooses what the city will build next based on probabilities and the
            weights given.
        Method Arguments:
            food_val_coef*: The amount to multiply the yield of food by when valuing.
            prod_val_coef*: The amount to multiply the yield of production by when valuing.
            science_val_coef*: The amount to multiply the yield of science by when valuing.
            gold_val_coef*: The amount to multiply the yield of gold by when valuing.
            settler_chance*: The base chance that a settler will be built, is then modified based
                on an equation.
        """
        look = classlookup.ClassLookUp()
        building_heap = []
        unit_heap = []
        for i in range(len(look.researchVal)):
            if self.civ.science >= look.researchVal[i]*self.civ.science_cost_multiplier():
                building_stage = look.buildingResearch[i]
                unit_stage = look.unitResearch[i]
                for name in building_stage:
                    if not self.has_building(name):
                        if self.get_gold_yield() < 0:
                            gold_val_coef = gold_val_coef * 100
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
                        unit_priority = (unit.prod_cost-unit.strength-unit.range_strength)
                        heappush(unit_heap,(unit_priority,unit))
        #decide whether to build a settler, military unit, or building
        decision = random.uniform(0,1)
        settler_chance = settler_chance * min(self.civ.settler_chance_city_size_max_multiplier,self.pop*self.civ.settler_chance_city_size_coef)\
        * (self.civ.settler_chance_city_count_coef/len(self.civ.city_list)) * self.civ.settler_chance_settler_count_coef / (len(self.civ.unit_list)+1)
        if decision < settler_chance:
                if self.civ.get_total_pop_count() > (len(self.civ.unit_list) + len(self.civ.mil_unit_list)):
                    return look.unit_lookup["settler"]
                else:
                    return look.building_lookup["prod_gold"]
        elif decision < unit_chance+settler_chance:
                if self.civ.get_total_pop_count() > (len(self.civ.unit_list) + len(self.civ.mil_unit_list)):
                    return heappop(unit_heap)[1]
                else:
                    return look.building_lookup["prod_gold"]
        else:
            if len(building_heap) == 0:
                if self.civ.get_total_pop_count() > (len(self.civ.unit_list) + len(self.civ.mil_unit_list)):
                    return heappop(unit_heap)[1]
                else:
                    return look.building_lookup["prod_gold"]
            else:
                return heappop(building_heap)[1]

    def grow_borders(self):
        """
        Summary:
            Increases the size of the city's borders by 1, this also increases
            how many tiles can be improved as well as worked.
        """
        self.border_distance = self.border_distance + 1
        tiles_to_add = self.grid.tiles[self.y,self.x].get_neighbors(distance=self.border_distance)
        for tile in tiles_to_add:
            if tile.owner == None:
                tile.city = self
                tile.owner = self.civ
                self.tile_list.append(tile)
                heappush(self.tile_improve_heap,(int(tile.total_yield()),tile))
    
    def improve_tiles(self):
        """
        Summary:
            Improves the tiles around the city. Has special case for when the city
            is costing the civ money that it will build more trading posts.
        """
        look = classlookup.ClassLookUp()
        #improve one at a time
        if len(self.improving_tiles) == 0:
            if len(self.tile_improve_heap) > 0:
                tile_to_improve = heappop(self.tile_improve_heap)[1]
                tile_to_improve.improvement_turns = 4
                self.improving_tiles.append(tile_to_improve)
        if self.border_distance == 2 and len(self.improving_tiles) < 2:
            if len(self.tile_improve_heap) > 0:
                tile_to_improve = heappop(self.tile_improve_heap)[1]
                tile_to_improve.improvement_turns = 4
                self.improving_tiles.append(tile_to_improve)
        if self.border_distance == 3 and len(self.improving_tiles) < 3:
            if len(self.tile_improve_heap) > 0:
                tile_to_improve = heappop(self.tile_improve_heap)[1]
                tile_to_improve.improvement_turns = 4
                self.improving_tiles.append(tile_to_improve)
        for tile in self.improving_tiles:
            if tile.improvement == None:
                tile.improvement_turns = tile.improvement_turns - 1
                if tile.improvement_turns == 0:
                    if self.get_gold_yield() <= -2 and self.civ.science >= look.researchVal[4]*self.civ.science_cost_multiplier():
                        tile.add_improvement("trading_post")
                    elif tile.terrain == "forest" and self.civ.science >= look.researchVal[2]*self.civ.science_cost_multiplier():
                        tile.add_improvement("lumber_mill")
                    elif tile.terrain == "hills" and self.civ.science >= look.researchVal[1]*self.civ.science_cost_multiplier():
                        tile.add_improvement("mine")
                    elif tile.terrain == "jungle" and self.civ.science >= look.researchVal[4]*self.civ.science_cost_multiplier():
                        tile.add_improvement("trading_post")
                    else:
                        if tile.biome == "grassland" or tile.biome == "plains" or tile.near_river:
                            tile.add_improvement("farm")
                        elif self.civ.science >= look.researchVal[4]*self.civ.science_cost_multiplier():
                            tile.add_improvement("trading_post")
                        else:
                            tile.add_improvement("farm")
                    self.improving_tiles.remove(tile)

    def check_food(self):
        """
        Summary:
            Checks to see if the city will grow, shrink, or keep the same
            population count.
        """
        self.food = self.food + (self.get_food_yield()-self.pop*2)
        food = self.food
        # food -= self.pop*2
        if food >= self.food_to_grow(self.pop+1):
            #grow
            self.pop = self.pop + 1
            self.food = 0
        elif self.pop > 1 and food < (-1*self.food_to_grow(self.pop-1)):
            self.pop = self.pop - 1

    def process_turn(self):
        """
        Summary:
            Improves tiles, checks for growth, chooses production, expands borders,
            and returns the yield values of the city for analysis.
        """
        #improve the tiles
        self.improve_tiles()
        
        #check food, update pop
        self.check_food()
        
        #add prod, check production
        self.production = self.production + self.get_prod_yield()
        if self.to_build == None:
            #choose something to build
            self.to_build = self.choose_production(food_val_coef=self.civ.building_food_value_coef,\
            prod_val_coef=self.civ.building_prod_value_coef,science_val_coef=self.civ.building_science_value_coef,\
            gold_val_coef=self.civ.building_gold_value_coef,settler_chance=self.civ.settler_chance_base,\
            unit_chance=self.civ.unit_chance)

        if self.production >= self.to_build.prod_cost:
            #complete production
            if self.to_build.type == "building":
                if self.to_build.name == "prod_gold":
                    self.temp_gold = int(self.production * .25)
                    self.production = 0
                else:
                    self.building_list.append(self.to_build)
            else:
                if self.to_build.name == "settler":
                    # print("-------------------finished a settler")
                    self.grid.tiles[self.y,self.x].unit = tunit.Unit(name="settler",atype="civilian",prod_cost=106,speed=2,y=self.y,x=self.x,civ=self.civ,grid=self.grid)
                    self.civ.unit_list.append(self.grid.tiles[self.y,self.x].unit)
                    self.grid.tiles[self.y,self.x].unit.process_turn()
                else:
                    unit = self.to_build
                    unit_to_add = tunit.Unit(name=unit.name,atype=unit.atype,prod_cost=unit.prod_cost,speed=unit.speed, strength=unit.strength,y=-1,x=-1,civ=self.civ)
                    self.civ.mil_unit_list.append(unit_to_add)

            if self.to_build.name == "hydro_plant":
                self.has_hydro_plant = True
            elif self.to_build.name == "university":
                self.has_university = True
            #choose new production
            self.production = self.production - self.to_build.prod_cost
            self.to_build = self.choose_production(food_val_coef=self.civ.building_food_value_coef,\
            prod_val_coef=self.civ.building_prod_value_coef,science_val_coef=self.civ.building_science_value_coef,\
            gold_val_coef=self.civ.building_gold_value_coef,settler_chance=self.civ.settler_chance_base,\
            unit_chance=self.civ.unit_chance)

        #growing borders
        self.border_growth_count += 1
        if self.border_growth_count >= self.civ.first_border_threshold and self.border_distance == 1:
            self.grow_borders()
        elif self.border_growth_count >= self.civ.second_border_threshold and self.border_distance == 2:
            self.grow_borders()

        #Setting which tiles will be worked.
        heap_of_tiles = []
        prioritization_change_count = self.pop/2
        for tile in self.tile_list:
            tile.worked = False
            gold_coef = 1.0
            if self.get_gold_yield() < 0:
                gold_coef = 3
            if prioritization_change_count <= 0:
                gold_coef = 1.0
            prioritization_change_count -= 1
            heappush(heap_of_tiles,(int(100-tile.total_yield(gold_coefficent=gold_coef)),tile))
        for i in range(self.pop):
            if len(heap_of_tiles) > 0:
                tile_to_work = heappop(heap_of_tiles)[1]
                tile_to_work.worked = True
        #food,prod,gold,sci
        to_return_gold = self.get_gold_yield() + self.temp_gold
        self.temp_gold = 0
        return self.get_food_yield(),self.get_prod_yield(),to_return_gold,self.get_science_yield(),self.calculate_population()
        # return self.get_food_yield(),self.get_prod_yield(),to_return_gold,self.get_science_yield(),self.pop #kept to make it easier to compare civilizations' pop count
      

    def popF(self,x):  
        """
        Summary:
            Takes a given value and returns the population based on previous data.
        """
        return 959.0549*x**2.8132

    def calculate_population(self):
        """
        Summary:
            Returns the population, not population points, in the city. Uses a look
            up table for the first 9 values to increase accuracy. Likely innaccurate
            beyond pop = 40.
        """
        look = classlookup.ClassLookUp()
        if self.pop < 10:
            return int(look.pop_table[self.pop])
        else:
            return int(self.popF(self.pop))
