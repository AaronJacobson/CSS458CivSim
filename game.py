
#Import Statements
from grid import Grid
from civilization import Civ
from building import Building
from unit import Unit
from city import City
import classlookup
#from interpreter import Interpreter
import numpy as N
import os
import copy

class Game(object):
    """
    """

    def __init__(self,y = 50,x = 100,num_turns = 500, num_civ = 0):
        """
        """

        #Initialize Total Turns
        self.num_turns = num_turns

        #Initialize tile grids and civ list
        self.x = x
        self.y = y
        self.civs = []
        self.turns = []

        self.num_civ = num_civ
        self.cur_grid = Grid(y,x)
        self.initCivs(num_civ)

        #TODO initialize the list/dictionary of biomes and they're yields
        #TODO List of grids\

    def initCivs(self,num_civ):
        """
        """
        if num_civ // 2 <= 3:
            xdiv = 4
            ydiv = 3
        else:
            xdiv=4
            ydiv=4
        for i in range(num_civ):
            self.civs.append(Civ(i))
            xrand = N.random.normal(0,0.05*self.x)
            yrand = N.random.normal(0,0.05*self.y)

            self.civs[i].city_list.append(City(self.cur_grid,int(self.y//ydiv*((i//ydiv)+1)+yrand),int(((self.x//xdiv)*((i+1)%4))+xrand),self.civs[i]))
            warrior = classlookup.ClassLookUp.unit_lookup['warrior']
            warrior_add = Unit(name = warrior.name,atype = warrior.atype,prod_cost = warrior.prod_cost,speed = warrior.speed,y=-1,x=-1,civ=self.civs[i])
            self.civs[i].mil_unit_list.append(warrior_add)
                
    
    def run(self):
        """
        """
        yield_vals = N.zeros((self.num_turns,len(self.civs),4))
        #Initialize run loop
        for i in range(self.num_turns):
            #Process Civ Wars

            #Process Civs Individual turns
            for civ in self.civs:
                yield_vals[i,civ.civNum]=civ.process_turn(i)

            #Process Tiles
            #Gods this is inefficient, but without creating a list of tile changes, cellular automata is the way to go!
            for m in range(self.y):
                for n in range(self.x):
                    self.cur_grid[m][n].process_turn()
            #Update State Variables if any exist
            self.turns.append(copy.deepcopy(self.cur_grid))
            return yield_vals
