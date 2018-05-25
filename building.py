class Building(object):
    
    
    def __init__(self,name="none",gold_yield=0,gold_bonus=0.0,food_yield=0,food_bonus=0.0,
    science_yield=0,science_bonus=0.0,science_pop_bonus=0,prod_yield=0,prod_bonus=0.0):
        self.name = name
        self.gold = gold_yield
        self.gold_bonus = gold_bonus
        self.food = food_yield
        self.food_bonus = food_bonus
        self.science = science_yield
        self.science_bonus = science_bonus
        self.science_pop_bonus = science_pop_bonus
        self.production = prod_yield
        self.production_bonus = prod_bonus
    
        
    