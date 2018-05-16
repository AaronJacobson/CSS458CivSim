class Unit(object):
    
    def __init__(self,strength,speed,civ,grid,y,x):
        self.strength = strength
        self.speed = speed
        self.civ = civ
        self.grid = grid
        self.y = y
        self.x = x
        self.health = 100