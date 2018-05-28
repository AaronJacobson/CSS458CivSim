from heapq import heappush,heappop
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

        if self.name == "settler":
            self.target_city_tile = None


    def process_turn(self):
        if self.name== "settler":#TODO move to found city
            if self.target_city_tile == None:
                #find a city location to move to
                tiles_to_consider = self.grid.tiles[self.y,self.x].get_neighbors(distance=10)
                heap_of_tiles = []
                for tile in tiles_to_consider:
                    if not tile.close_to_city:
                        city_val = 0
                        city_tiles = tile.get_neighbors(distance=1)
                        for tile in city_tiles:
                            city_val += tile.total_yield()
                        heappush(heap_of_tiles,(100-city_val,tile))#it's a min heap function
                self.target_city_tile = heappop(heap_of_tiles)[1]
                # print("------------target= " + str(self.target_city_tile.y) + "," + str(self.target_city_tile.x))
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
                print("--------------attempting to found city")
                self.grid.tiles[self.y,self.x].city = city.City(self.grid,self.y,self.x,self.civ)
                self.civ.city_list.append(self.grid.tiles[self.y,self.x].city)
                self.grid.tiles[self.y,self.x].city.process_turn()
                self.grid.tiles[self.y,self.x].unit = None
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