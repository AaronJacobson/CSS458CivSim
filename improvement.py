
class Improvement(object):
    """
    Summary:
        Contains information pertinent to an Improvement object as defined by Civilization V
    """
    
    def __init__(self,name="none",gold_yield=0,food_yield=0,science_yield=0,prod_yield=0,strength_mod=0.0):
        """
        Summary:
            Constructor for Improvement class.
            Takes in variables and sets them.
        
        Method Arguments:
            name*: The name of this Improvement
            gold_yield*: How much gold this Improvement produces
            food_yield*: How much food this Improvement produces
            science_yield*: How much science this Improvement produces
            prod_yield*: How much production this Improvement produces
            strength_mod*: How much this improvement modifies the strength of a unit standing on it.
        """
        self.name = name
        self.gold_yield = gold_yield
        self.food_yield = food_yield
        self.science_yield = science_yield
        self.prod_yield = prod_yield
        self.strength_mod = strength_mod