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
        distance = self.civ.settler_base_distance
        while self.target_city_tile == None:
            if distance <= self.grid.x:
                distance += self.civ.settler_distance_increase
            tiles_to_consider = self.grid.tiles[self.y,self.x].get_neighbors(distance=distance)
            N.random.shuffle(tiles_to_consider)
            if tiles_to_consider[0].close_to_city:
                pass
            else:
                self.can_found_city = True
                self.target_city_tile = tiles_to_consider[0]
                neighbors = self.target_city_tile.get_neighbors(distance=3)
                neighbors.append(self.target_city_tile)
                for tile in neighbors:
                    tile.close_to_city = True
        
    def move_once(self):
        moved = False
        if self.target_city_tile.y > self.y:
            self.move_unit(self.y+1,self.x)
            moved = True
        elif self.target_city_tile.y < self.y:
            self.move_unit(self.y-1,self.x)
            moved = True
        elif self.target_city_tile.x > self.x:
            self.move_unit(self.y,self.x+1)
            moved = True
        elif self.target_city_tile.x < self.x:
            self.move_unit(self.y,self.x-1)
            moved = True
        return moved
        
    
    def process_turn(self):
        if self.name== "settler":#TODO move to found city
            if self.target_city_tile == None:
                self.choose_city_location()
            #move to city location
            moved = self.move_once()
            if moved:
                if self.grid.tiles[self.y,self.x].terrain == "hills" or \
                self.grid.tiles[self.y,self.x].terrain == "forest" or \
                self.grid.tiles[self.y,self.x].terrain == "jungle":
                    pass #don't move more
                else:
                    self.move_once()
            if (self.target_city_tile.y == self.y) and (self.target_city_tile.x == self.x):
                #found city
                self.grid.tiles[self.y,self.x].city = city.City(self.grid,self.y,self.x,self.civ)
                self.civ.city_list.append(self.grid.tiles[self.y,self.x].city)
                self.grid.tiles[self.y,self.x].city.process_turn()
                self.grid.tiles[self.y,self.x].unit = None
                self.can_found_city = False

                self.civ.unit_list.remove(self)
                #just in case this unit is accessed again somehow
                self.y = -1
                self.x = -1

    def move_unit(self, y, x):
        if self.grid.tiles[y,x].unit == None:
            self.grid.tiles[self.y,self.x].unit = None
            self.grid.tiles[y,x].unit = self
            self.y = self.grid.tiles[y,x].y
            self.x = self.grid.tiles[y,x].x

    def value(self):
        return 1000 - self.strength * self.civ.strength_value_coef - self.speed * self.civ.speed_value_coef
        
    def __lt__(self,other):
        return self.value() < other.value()