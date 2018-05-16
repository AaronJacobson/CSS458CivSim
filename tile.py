class Tile(object):
    
    def __init__(self,grid,y,x,elevation,biome):
        self.grid = grid
        self.y = y
        self.x = x
        self.elevation = elevation
        self.biome = biome
        #is this how we should deal with cities and units?
        self.unit = None
        self.city = None
        #TODO init yields based on elevation and biome
        #TODO manage roads, won't change yields
        #TODO manage improvements