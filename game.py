
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

    def __init__(self,y = 50,x = 100,num_turns = 500, num_civ = 0,war_chance = 0.01,loss_chance = 0.005,percent_grass=.5,\
    desert_chance=.01,desert_size=2,snow_width=0.05,tundra_width=0.075,\
    prob_forest=0.05,prob_jungle=0.05,prob_river = 0.2,prob_hill=.085):
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
        self.war_chance = war_chance
        self.loss_chance = loss_chance
        self.cur_grid = Grid(y,x,percent_grass=percent_grass,desert_chance=desert_chance,\
        desert_size=desert_size,snow_width=snow_width,tundra_width=tundra_width,\
        prob_forest=prob_forest,prob_jungle=prob_jungle,prob_river=prob_river,prob_hill=prob_hill)
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
            while self.x//xdiv - xrand < 0 or xrand > self.x//xdiv:
                xrand = N.random.normal(0,0.05*self.x)
            yrand = N.random.normal(0,0.05*self.y)
            while self.y//ydiv - yrand < 0 or yrand > self.y//ydiv:
                yrand = N.random.normal(0,0.05*self.y)
            self.civs[i].city_list.append(City(self.cur_grid,int(self.y//ydiv*((i//ydiv)+1)+yrand),int(((self.x//xdiv)*((i+1)%4))+xrand),self.civs[i]))
            warrior = classlookup.ClassLookUp.unit_lookup['warrior']
            warrior_add = Unit(name = warrior.name,atype = warrior.atype,prod_cost = warrior.prod_cost,speed = warrior.speed,strength=warrior.strength,y=-1,x=-1,civ=self.civs[i])
            self.civs[i].mil_unit_list.append(warrior_add)
                
    
    def run(self):
        """
        """
        yield_vals = N.zeros((self.num_turns,len(self.civs),5),dtype=N.dtype(int))
        #Initialize run loop
        for i in range(self.num_turns):
            print("Turn: "+str(i))
            #Process Civs Individual turns and Civ Wars
            for civ in self.civs:
                if civ.civNum!=-1:
                    #Process turn
                    #print("get yields")
                    yield_vals[i,civ.civNum]=civ.process_turn(i)
                    #Temporily get Settlers position
                    print("Civ #"+str(civ.civNum))
                    #for i in range(len(civ.unit_list)):
                    #    print("Settler "+str(i)+":\t"+str(civ.unit_list[i].y)+'\t'+str(civ.unit_list[i].x))
                    #print("Trying to War!")
                    #Try to be at war if not at war
                    if len(civ.wars) == 0 and len(civ.at_war) == 0:
                        close_val = 999999999
                        for otherciv in self.civs:
                            if otherciv is not civ:
                                dist = ((otherciv.city_list[0].x-civ.city_list[0].x)**2+(otherciv.city_list[0].y-civ.city_list[0].y)**2)**0.5
                                if dist < close_val:
                                    close_val = dist
                        for otherciv in self.civs:
                            if otherciv is not civ:
                                dist = ((otherciv.city_list[0].x-civ.city_list[0].x)**2+(otherciv.city_list[0].y-civ.city_list[0].y)**2)**0.5
                                sum_strength = 0
                                for unit in civ.mil_unit_list:
                                    sum_strength += unit.strength
                                other_sum_strength = 0
                                for unit in otherciv.mil_unit_list:
                                    other_sum_strength += unit.strength
                                if other_sum_strength != 0:
                                    rel_strength = sum_strength/other_sum_strength
                                else:
                                    rel_strength = sum_strength/1
                                if yield_vals[i,otherciv.civNum,1] != 0:
                                    rel_prod = yield_vals[i,civ.civNum,1]/yield_vals[i,otherciv.civNum,1]
                                else:
                                    rel_prod = yield_vals[i,civ.civNum,1]/1
                                
                                rel_dist = close_val / dist
                                if sum_strength != 0:
                                    mil_strength = N.log(sum_strength/(8+(0.5*i)))
                                else:
                                    mil_strength = -1
                                if mil_strength > 0:
                                    mil_strength = 0    
                                adjusted_chance = self.war_chance * rel_strength * rel_prod * rel_dist + mil_strength
                                if adjusted_chance > N.random.uniform():
                                    print("War were declared")
                                    #Civ, Turns war has gone on, Lost cities, Lost Units, Gained Cities, Killed units
                                    civ.wars.append([otherciv,0,0,0,0,0])
                                    otherciv.at_war.append(civ)
                    #print("Warring!")
                    #Process War!
                    for entry in civ.wars:
                                #Compute Relative Strength
                                sum_strength = 0
                                for unit in civ.mil_unit_list:
                                    sum_strength += unit.strength
                                other_sum_strength = 0
                                for unit in otherciv.mil_unit_list:
                                    other_sum_strength += unit.strength
                                if other_sum_strength != 0:
                                    rel_strength = sum_strength/other_sum_strength
                                else:
                                    rel_strength = sum_strength/1
                                if rel_strength == 0:
                                    rel_strength = 0.0001
                                #Compute our mil_strength score
                                if sum_strength != 0:
                                    mil_strength = N.log(sum_strength/(8+(0.5*i)))
                                else:
                                    mil_strength = -1
                                if mil_strength > 0:
                                    mil_strength = 0 
                                #Compute their mill strength score
                                if other_sum_strength != 0:
                                    other_mil_strength = N.log(other_sum_strength/(8+(0.5*i)))
                                else:
                                    other_mil_strength = -1
                                if other_mil_strength > 0:
                                    other_mil_strength = 0 
                                
                                #Lose a city (oh no)
                                if self.loss_chance*(1/rel_strength)+other_mil_strength > N.random.uniform():
                                    civ.city_list[-1].pop = civ.city_list[-1].pop//2
                                    entry[0].city_list.append(civ.city_list[-1])
                                    entry[0].city_list[-1].civ=entry[0]
                                    for tile in entry[0].city_list[-1].tile_list:
                                        tile.owner = entry[0]
                                    del(civ.city_list[-1])
                                    entry[2]+=1
                                
                                #Gain a city (yay)
                                if self.loss_chance*(rel_strength)+mil_strength > N.random.uniform():
                                    entry[0].city_list[-1].pop = entry[0].city_list[-1].pop//2
                                    civ.city_list.append(entry[0].city_list[-1])
                                    civ.city_list[-1].civ=civ
                                    for tile in civ.city_list[-1].tile_list:
                                        tile.owner = civ
                                    del(entry[0].city_list[-1])
                                    entry[4]+=1
                                                    
                                    
                                #Kill Unit!
                                if len(entry[0].mil_unit_list) != 0:
                                    if self.loss_chance*rel_strength > N.random.uniform():
                                        other_sum_strength -= entry[0].mil_unit_list[0].strength
                                        del(entry[0].mil_unit_list[0])
                                        entry[5]+=1
                                
                                #Lose Unit
                                if len(civ.mil_unit_list) != 0:
                                    if self.loss_chance*(1/rel_strength) > N.random.uniform():
                                        sum_strength -= civ.mil_unit_list[0].strength
                                        del(civ.mil_unit_list[0])
                                        entry[3]+=1
                                #Other Civ has no cities and loses
                                if len(entry[0].city_list) == 0:
                                    lose_civ = entry[0]
                                    #Get all the civs that losing civ is at war with
                                    for warciv in lose_civ.at_war:
                                        #Look at their wars lists
                                        for item in warciv.wars:
                                            #remove entry if the civ they are at war with is the civ that has just lost
                                            if item[0] == lose_civ:
                                                warciv.wars.remove(item)
                                    for war in lose_civ.wars:
                                        war[0].at_war.remove(lose_civ)
                                    lose_civ.civNum=-1
                                    self.civs.remove(lose_civ)
                                    # lose_civ.dead = True
                                #This civ has no cities and loses
                                elif len(civ.city_list) == 0:
                                    for warciv in civ.at_war:
                                        for item in warciv.wars:
                                            if item[0] == civ:
                                                warciv.wars.remove(item)
                                    for war in civ.wars:
                                        war[0].at_war.remove(civ)
                                    civ.civNum=-1
                                    self.civs.remove(civ)
                                else:
                                    #Peace time?
                                    age_factor = entry[1]*0.05
                                    if entry[5] != 0:
                                        rel_unit_lost = entry[3]/entry[5]
                                    else:
                                        rel_unit_lost = entry[3]/1
                                    if entry[4] != 0:
                                        rel_city_lost = entry[2]/entry[4]
                                    else:
                                        rel_city_lost = entry[2]/1
                                    
                                    if (self.war_chance + age_factor + (0.05*rel_unit_lost) + (0.1*rel_city_lost)) > N.random.uniform():
                                        entry[0].at_war.remove(civ)
                                        civ.wars.remove(entry)
                                    else:
                                        entry[1]+=1
                                    
                                        
                

            #Update State Variables
            #self.turns.append(copy.deepcopy(self.cur_grid))
            # inp = input()
            # if inp == 'ret':
            #     return
        return yield_vals
