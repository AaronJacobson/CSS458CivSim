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

    def science_cost_multiplier(self):
        return 1.0 + .05*len(self.city_list)