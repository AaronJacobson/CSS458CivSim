class City(object):
    
    def __init__(self,grid,y,x,civ):
        self.grid = grid
        self.y = y
        self.x = x
        self.civ = civ
        self.building_list = []
        self.tile_list = []
        self.pop = 1
        self.food = 0
        self.production = 0
        self.health = 200
        self.strength = 8 #this depends on many factors
        
        self.set_close_to_city()
        self.tile_list = self.grid.tiles[y,x].get_neighbors(distance=1)
    
    def set_close_to_city(self):
        close_tiles = self.grid.tiles[self.y,self.x].get_neighbors(distance=3)
        for tile in close_tiles:
            tile.close_to_city = True
        self.grid.tiles[self.y,self.x].close_to_city = True