from grid import Grid

class Game(object):
    
    def __init__(self,y=50,x=100,numTurns=500,numCivs=8):
        self.turns = []
        self.num_turns = numTurns
        self.turns[0] = Grid(y,x)
        #TODO Dictionary of Biomes
        #TODO List of grids
