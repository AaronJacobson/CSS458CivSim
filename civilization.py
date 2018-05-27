class Civ(object):
    """
    """
    def __init__(self,civNum):
        """
        """
        self.civNum = civNum
        self.unit_list = []
        self.city_list = []
        self.science = 0
        
    def process_turn(self):
        """
        """
        #Create variables for turn processing
        sum_food = 0
        sum_prod = 0
        sum_gold = 0
        sum_sci = 0
        
        #Process each cities turn
        for city in self.city_list:
            food,prod,gold,sci = city.process_turn()
            #Do stuff with that
            #add to sums
            sum_food += food
            sum_prod += prod
            sum_gold += gold
            sum_sci += sci
        
        #add new science to civ science value
        self.science += sum_sci
        
        #return sum values
        return sum_food,sum_prod,sum_gold,sum_sci