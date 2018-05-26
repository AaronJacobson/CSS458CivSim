
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
        
        if self.name == "settler":
            self.target_city_tile = None
    
    
    def process_turn(self):
        if self.name== "settler":#TODO move to found city
            if self.target_city_tile == None:
                #find a city location to move to and move to it
                pass
            #move to city location
            moved = False
            if self.target_city_tile.y > self.y:
                self.move_unit(self.y+1,self.x)
                moved = True
            elif self.target_city_tile.y < self.y:
                self.move_unit(self.y-1,self.x)
                moved = True
            if moved:
                if self.grid.tiles[self.y,self.x].terrain == "hills" or \
                self.grid.tiles[self.y,self.x].terrain == "forest" or \
                self.grid.tiles[self.y,self.x].terrain == "jungle":
                   pass #don't move more
                else:
                    if self.target_city_tile.x > self.x:
                        self.move_unit(self.y,self.x+1)
                    elif self.target_city_tile.x < self.x:
                        self.move_unit(self.y,self.x-1)
            if self.target_city_tile.y == self.y and self.targey_city_tile == self.x:
                #found city
                pass
            
        else:
            pass
        #TODO if civ is at war
        #move unit to army if forming one, move it as part of the army if attacking city
        #TODO if civ is not at war
        #move unit to protect city
    def move_unit(self, y, x):
        self.remove_unit()
        self.y = y
        self.x = x
        self.grid.tiles[y,x].move_unit(self) #check if this is correct for moving unit to a new space
    