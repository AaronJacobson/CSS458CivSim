class City(object):
    
    def __init__(self,grid,y,x,civ):
        self.grid = grid
        self.y = y
        self.x = x
        self.civ = civ
        self.building_list = []
        self.pop = 1
        self.food = 0
        self.production = 0
        self.health = 200
        self.strength = 8 #this depends on many factors