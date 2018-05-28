from heapq import heappush,heappop
import numpy as N
import city
class Unit(object):

    def __init__(self,name="none",atype="nothing",prod_cost=0,strength=0,\
    speed=0,range_strength=0,rangeSize=0,civ=None,grid=None,y=0,x=0,airdrop=0):
        self.name = name
        self.atype = atype
        self.prod_cost = prod_cost
        self.strength = strength
        self.range_strength = range_strength
        self.rangeSize = rangeSize
        self.speed = speed
        self.civ = civ
        self.grid = grid
        self.y = y
        self.x = x
        self.health = 100
        self.airdrop = airdrop
        self.type = "unit"
        self.can_found_city = False

        if self.name == "settler":
            self.target_city_tile = None
    
    def choose_city_location(self):
        #find a city location to move to
        distance = 5
        while self.target_city_tile == None:
            distance += 5
            tiles_to_consider = self.grid.tiles[self.y,self.x].get_neighbors(distance=distance)
            N.random.shuffle(tiles_to_consider)
            if tiles_to_consider[1].close_to_city:
                pass
            else:
                self.can_found_city = True
                self.target_city_tile = tiles_to_consider[1]
                neighbors = self.target_city_tile.get_neighbors(distance=2)
                neighbors.append(self.target_city_tile)
                for tile in neighbors:
                    tile.close_to_city = True
        # print("-------------------target= " + str(self.target_city_tile.y) + "," + str(self.target_city_tile.x))
        
    
    def process_turn(self):
        if self.name== "settler":#TODO move to found city
            if self.target_city_tile == None:
                self.choose_city_location()
            #move to city location
            moved = False
            if self.target_city_tile.y > self.y:
                self.move_unit(self.y+1,self.x)
                moved = True
            if self.target_city_tile.y < self.y:
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
                    if self.target_city_tile.x < self.x:
                        self.move_unit(self.y,self.x-1)
            if (self.target_city_tile.y == self.y) and (self.target_city_tile.x == self.x):
                #found city
                print("--------------------------------------founding city")
                self.grid.tiles[self.y,self.x].city = city.City(self.grid,self.y,self.x,self.civ)
                self.civ.city_list.append(self.grid.tiles[self.y,self.x].city)
                self.grid.tiles[self.y,self.x].city.process_turn()
                self.grid.tiles[self.y,self.x].unit = None
                self.can_found_city = False
                self.y = -1
                self.x = -1
                # self.civ.unit_list.remove(self)#this might or might not work
        else:
            pass
        #TODO if civ is at war
        #move unit to army if forming one, move it as part of the army if attacking city
        #TODO if civ is not at war
        #move unit to protect city
    def move_unit(self, y, x):
        if self.grid.tiles[y,x].unit == None:
            # print("moving from " + str(self.y) + " " + str(self.x) + " to " + str(y) + " " + str(x))
            # print("target is   " + str(self.target_city_tile.y) + " " + str(self.target_city_tile.x))
            self.grid.tiles[self.y,self.x].unit == None
            self.grid.tiles[y,x].unit = self
            self.y = self.grid.tiles[y,x].y
            self.x = self.grid.tiles[y,x].x
    def value(self):
        return self.prod_cost - self.strength - self.speed * 2
        
    def __lt__(self,other):
        return self.value() < other.value()