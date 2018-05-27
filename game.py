
#Import Statements
from grid import Grid
from civilization import Civ
from building import Building
from unit import Unit
from interpreter import Interpreter
import numpy as N
import os

class Game(object):
    """
    """

    def __init__(self,y = 50,x = 100,numTurns = 500,mapName = None):
        """
        """

        #Initialize Total Turns
        self.num_turns = numTurns

        #Initialize tile grids and civ list
        self.x = x
        self.y = y
        self.civs = []
        self.turns = []
        self.curGrid = None


        #Fill grid values and civ list
        self.simInit()
        #TODO initialize the list/dictionary of biomes and they're yields
        #TODO List of grids\


    def simInit(self):
        """
        """
        #RUN MAP GENERATOR HERE TO POPULATE INITIAL GRID!
        #REPLACE NONE WITH CALL TO MAP GEN OR SIMPLY GET THAT THROUGH MAP GEN
        self.curGrid = None
        self.turns.append(self.curGrid)




    def run(self):
        """
        """
        yield_vals = N.zeros((self.numTurns,len(self.civs),4))
        #Initialize run loop
        for i in range(self.numTurns):
            #Grab Grid for Processing
            curGrid = self.turns[-1]

            #Process Civ Wars

            #Process Civs Individual turns
            for civ in self.civs:
                yield_vals[i,civ.civNum]=civ.process_turn()

            #Process Tiles
            #Gods this is inefficient, but without creating a list of tile changes, cellular automata is the way to go!
            for m in range(y):
                for n in range(x):
                    curGrid[m][n].process_turn()
            #Update State Variables if any exist
            self.turns.append(curGrid)
