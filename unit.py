class Unit(object):
    
    def __init__(self,name="none",atype="nothing",prod_cost=0,strength=0,\
    speed=0,range_strength=0,rangeSize=0,civ=0,grid=None,y=0,x=0,airdrop=0):
        self.name = name
        self.atype = atype
        self.prod_cost = prod_cost
        self.strength = strength
        self.speed = speed
        self.civ = civ
        self.grid = grid
        self.y = y
        self.x = x
        self.health = 100
        self.airdrop = airdrop