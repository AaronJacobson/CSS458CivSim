class Civ(object):
    """
    Every civilization has units, both military and settler, cities, and wars.
    On every turn, each civilization processes the turn of every settler and city it has.
    """
    def __init__(self,civNum):
        """
        Initializes all the fields, the civ uses to keep track of what it has.
        """
        self.civNum = civNum
        self.unit_list = []
        self.mil_unit_list = []
        self.city_list = []
        self.wars = []
        self.at_war = []
        self.science = 0
        self.dead = False
        
        #-----------------------------------------------------------------------
        #These are the base probabilities and the weight this civilization assigns
        #to each yield.
        self.tile_food_value_coef = 1.0
        self.tile_prod_value_coef = 1.0
        self.tile_science_value_coef = 1.0
        self.tile_gold_value_coef = 1.0
        
        self.settler_distance_increase = 1
        self.settler_base_distance = 5
        
        self.speed_value_coef = 2.0
        self.strength_value_coef = 1.0
        
        self.city_trade_and_road_substitute_per_pop = .25
        self.building_food_value_coef = 1.0
        self.building_prod_value_coef = 1.0
        self.building_science_value_coef = 1.0
        self.building_gold_value_coef = 1.0
        
        self.settler_chance_base = .1
        self.unit_chance = .1
        #building chance is 1-settler_chance_base-unit_chance
        self.settler_chance_city_size_max_multiplier = 3
        self.settler_chance_city_size_coef = .5
        self.settler_chance_city_count_coef = 1.0
        self.settler_chance_settler_count_coef = 1.0
        
        self.first_border_threshold = 50
        self.second_border_threshold = 175
        
    
    def process_turn(self, turn):
        if self.dead:
            return
        """
        Processes the turn of every city and unit the civilization has.
        Gets the total yields for every city to allow for analysis.
        """
        #Create variables for turn processing
        sum_food = 0
        sum_prod = 0
        sum_gold = 0
        sum_sci = 0
        sum_pop = 0

        #process settler turns
        for unit in self.unit_list:
            unit.process_turn()

        #Process each cities turn
        for city in self.city_list:
            food,prod,gold,sci,pop = city.process_turn()
            #Do stuff with that
            #add to sums
            sum_food += food
            sum_prod += prod
            sum_gold += gold
            sum_sci += sci
            sum_pop += pop

        #sum_gold -= unit_maintenance(len(sel.unit_list)+len(self.mil_unit_list), turn)

        #add new science to civ science value
        self.science += sum_sci

        #return sum values
        return sum_food,sum_prod,sum_gold,sum_sci,sum_pop,len(self.city_list)

    def unit_maintenance(unit, turn):
        #TODO input formula
        #maintenance = ((0.5 + (8/1000)*turn) round(unit, 2))**(1 + (2/700) * turn)
        return unit

    """
    Helper method that can be used to get the population count, rather than the total
    population, as calculated by the special equation Civilization V uses.
    """
    def get_total_pop_count(self):
        pop_count = 0
        for city in self.city_list:
            pop_count += city.pop
        return pop_count

    """
    Helper method that gets the multiplier for how much 
    """
    def science_cost_multiplier(self):
        return 1.0 + .05*len(self.city_list)