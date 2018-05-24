import numpy as N

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
            self.moving_to_city = False
    
    
    def process_turn(self):
        if self.name== "settler":#TODO move to found city
            if self.moving_to_city:
                #move to city location
                pass
            else:
                #find a city location to move to and move to it
                self.moving_to_city = True
                self.clear_best_city_checked(self.y,self.x)
        else:
            pass
        #TODO if civ is at war
        #move unit to army if forming one, move it as part of the army if attacking city
        #TODO if civ is not at war
        #move unit to protect city
    def move_unit(self, y, x):
        remove_unit()
        self.y = y
        self.x = x
        self.grid[y,x].move_unit(self) #check if this is correct for moving unit to a new space
       
    """ 
    def find_best_city_spot(self,y,x,max_distance=30):#might want to move this to the tile class
        self.grid[y,x].best_city_checked = True
        if max_distance == 0:
            return [self.grid.total_value(),y,x]
        else:
            neighbors = N.array(self.grid[y,x].get_neighbors)
            neighbors = N.where(neighbors.best_city_checked == False)#not sure if this is correct, I'm trying to remove all the places that have been checked already
            #TODO call this method on all the remaining neighbors
        #TODO clear the best_city_checked values
    
    def clear_best_city_checked(self,y,x):#TODO this may or may not work
        if self.grid.tiles[y,x].best_city_checked:
            self.grid.tile[y,x].best_city_checked = False
            neighbors = self.grid.tiles[y,x].get_neighbors()
            for tile in neighbors:
                self.clear_best_city_checked(tile.y,tile.x)
    """