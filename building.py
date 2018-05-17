class Building(object):
    
    def __init__(self,gold_yield=0,gold_bonus=0,food_yield=0,food_bonus=0,science_yield=0, \
    science_bonus=0,science_pop_bonus=0,production_yield=0,production_bonus=0):
        self.gold = gold_yield
        self.gold_bonus = gold_bonus
        self.food = food_yield
        self.food_bonus = food_bonus
        self.science = science_yield
        self.science_bonus = science_bonus
        self.science_pop_bonus = science_pop_bonus
        self.production = production_yield
        self.production_bonus = production_bonus