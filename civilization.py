class Civ(object):
    """
    """
    def __init__(self,civNum):
        """
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
        return sum_food,sum_prod,sum_gold,sum_sci,sum_pop
    
    def unit_maintenance(unit, turn):
        #TODO input formula
        #maintenance = ((0.5 + (8/1000)*turn) round(unit, 2))**(1 + (2/700) * turn)
        return unit
