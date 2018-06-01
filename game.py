
#Import Statements from internal classes
from grid import Grid
from civilization import Civ
from unit import Unit
from city import City
import classlookup
from dataplotter import Dataplotter
#General Import statements
import numpy as N
import os

class Game(object):
    """
    Summary:
        Creates and runs a simulation of the Civilization V video game.
    """

    def __init__(self,y = 50,x = 100,num_turns = 500, num_civ = 0,war_chance = 0.02,loss_chance = 0.01,war_base = 9, war_mod = 0.2,percent_grass=.5,\
    desert_chance=.01,desert_size=2,snow_width=0.05,tundra_width=0.075,\
    prob_forest=0.05,prob_jungle=0.05,prob_river = 0.2,prob_hill=.085):
        """
        Summary:
            Constructor for the Game class that runs the simulation. Initializes
            state variables, creates the grid using inputted parameters,
            populates civs into grid and civ list using inputted parameters.

        Method Arguments:
            y*: the height of the grid to be created
            x*: the length of the grid to be created
            num_turns*: the number of turns that the simulation should run for.
            num_civ*: the number of civilizations that should be created for the simulation.
            war_chance*: the base chance that any civ will go to war with another.
            loss_chance*: the base chance that any civ will lose or gain cities, and lose or kill units.
            war_base*: The base value for computing minimum military strength at any turn in the game.
                        Used for determining if a city is lost, gained, or if war is declared.
            war_mod*: The modifying value for computing minimum military strength at any turn in the game.
            percent_grass*: Percent chance that a tile in the middle of the map is grassland instead of plains.
            desert_chance*: Percent chance that a tile and its surrounding tiles up to distance desert_size are made into desert tiles.
            desert_size*: The number of steps away from a central desert tile that will be made into desert upon map generation.
            snow_width*: The percentage of the top and bottom of the grid that will become snow tiles.
            tundra_width*: The percentage of the top and bottom of the grid that will become tundra tiles.
            prob_forest*: Percent chance that any tile and its next neighbor will be made into forests.
            prob_jungle*: Percent chance that any tile and its next neighbor will be made into jungles.
            prob_river*: Percent chance that any tile and its next neighbor will have a river running through them.
            prob_hill*: Percent chance that any tile will become a hill.

        """

        #Initialize Total Turns
        self.num_turns = num_turns

        #Initialize tile grids and civ list
        self.x = x
        self.y = y
        self.civs = []

        #Initialize important variables
        self.num_civ = num_civ
        self.war_chance = war_chance
        self.loss_chance = loss_chance
        self.war_mod = war_mod
        self.war_base = war_base

        #Initialize and generate Grid
        self.cur_grid = Grid(y,x,percent_grass=percent_grass,desert_chance=desert_chance,\
        desert_size=desert_size,snow_width=snow_width,tundra_width=tundra_width,\
        prob_forest=prob_forest,prob_jungle=prob_jungle,prob_river=prob_river,prob_hill=prob_hill)

        #Place Civs in the civ list and put their inital cities and warriors on the Grid
        self.initCivs(num_civ)

    def initCivs(self,num_civ):
        """Generates Civs, places them in state variable civs and puts their initial cities and units on the Grid

        Method Arguments:
            num_civ*: The number of civs to be generated.
        """
        #Checking to see if number of civs fits nicely into 2 rows
        if num_civ // 2 <= 3:
            #The number of sections to cut the grid into
            xdiv = 4
            ydiv = 3
        #They don't so make it 3 rows
        else:
            xdiv=4
            ydiv=4
        #For each new civ
        for i in range(num_civ):
            #Append them to the civ list
            self.civs.append(Civ(i))
            #Generate a random value to adjust starting x location
            xrand = N.random.normal(0,0.05*self.x)
            #Check if that variable would violate game rules and recreate until it doesn't
            while self.x//xdiv - xrand < 0 or xrand > self.x//xdiv:
                xrand = N.random.normal(0,0.05*self.x)
            #Generate y value
            yrand = N.random.normal(0,0.05*self.y)
            #Check it until it doesn't break rules
            while self.y//ydiv - yrand < 0 or yrand > self.y//ydiv:
                yrand = N.random.normal(0,0.05*self.y)
            #For that civ, generate a new City at location their location in the grid altered by the random x and y values.
            #Their location in the grid uses modulus and integer division of i to determine a grid location.
            self.civs[i].city_list.append(City(self.cur_grid,int(self.y//ydiv*((i//ydiv)+1)+yrand),int(((self.x//xdiv)*((i+1)%4))+xrand),self.civs[i],capitol=True))
            #Get the unit states for a warrior, the default starting unit
            warrior = classlookup.ClassLookUp.unit_lookup['warrior']
            #Create the new warrior
            warrior_add = Unit(name = warrior.name,atype = warrior.atype,prod_cost = warrior.prod_cost,speed = warrior.speed,strength=warrior.strength,y=-1,x=-1,civ=self.civs[i])
            #Add them to the civs military unit list
            self.civs[i].mil_unit_list.append(warrior_add)


    def run(self,output=False,print_war_peace=False,print_turn=False):
        """Runs the Civilization V simulation and outputs through dataplotter every turn if output is set.

        Summary:
            Checks if output is set and then looks for the proper directory to switch to, creating it if it doesn't exist.
            initializes the yield values numpy array used for storing important return values.
            Runs the simulation for loop num_turns times.
            In that for loop Each civ is told to run, first by telling them to process their turn.
            Then if that civ is not at war they look to see if they want to be at war
            Following that any wars they have initiated are run.
            That running of wars consists first of calculating important values for running the war,
            then trying to lose a city, take a city, lose units, kill units.
            The war checks if either side has lost and therefore should be removed and does so if necessary.
            Finally peace conditions are checked and peace may occur.
            Back outside the civ loop output is again checked and the dataplotter called every other turn.
            Then outside the entire sim loop the yield vals array is returned.

        Method Arguments:
            output*: Tells the method whether or not to output dataplotter images every turn to Exampleoutput\\Gameoutput\\
        """
        #Check output and set directory as necessary
        if output:
            if not os.path.isdir(os.path.dirname(__file__)+"\\ExampleOutput\\GameOutput\\"):
                os.makedirs(os.path.dirname(__file__)+"\\ExampleOutput\\GameOutput\\")
                os.chdir(os.path.dirname(__file__)+"\\ExampleOutput\\GameOutput\\")
            else:
                os.chdir(os.path.dirname(__file__)+"\\ExampleOutput\\GameOutput\\")

        #Create array for storing return values
        yield_vals = N.zeros((self.num_turns,len(self.civs),6),dtype=N.dtype(int))

        #Initialize run loop
        for i in range(self.num_turns):
            if print_turn:
                #Output the turn number
                print("Turn: "+str(i+1))

            #Process Civs Individual turns and Civ Wars
            for civ in self.civs:
                #Due to a quirk in for each loops, this is necessary to prevent dead civs from being run
                if civ.civNum!=-1:

                    #Process turn
                    yield_vals[i,civ.civNum]=civ.process_turn(i)

                    #Try to be at war if not at war
                    if len(civ.wars) == 0 and len(civ.at_war) == 0:
                        #Set absurd closest distance value.
                        close_val = 999999999
                        #go through civs to get other civs to be at war with to find the closest distance to another civ
                        for otherciv in self.civs:
                            #Make sure otherciv is not in fact the same civ as the turn being processed.
                            if otherciv is not civ:
                                #Compute a basic distance from capitol to capitol
                                dist = ((otherciv.city_list[0].x-civ.city_list[0].x)**2+(otherciv.city_list[0].y-civ.city_list[0].y)**2)**0.5
                                #Override closest distance value if distance to this civ is less than it.
                                if dist < close_val:
                                    close_val = dist
                        #Go through civs again, this time checking for WAR!
                        for otherciv in self.civs:
                            #Make sure otherciv is not the same as this civs
                            if otherciv is not civ:
                                #Compute distance to other civ
                                dist = ((otherciv.city_list[0].x-civ.city_list[0].x)**2+(otherciv.city_list[0].y-civ.city_list[0].y)**2)**0.5
                                #Find the sum strength of this civs military
                                sum_strength = 0
                                for unit in civ.mil_unit_list:
                                    sum_strength += unit.strength
                                #Get the sum strength of the other civs military
                                other_sum_strength = 0
                                for unit in otherciv.mil_unit_list:
                                    other_sum_strength += unit.strength
                                #Compute the relative sum strength between the two militaries
                                #Check that their strength is not 0 to prevent division by 0
                                if other_sum_strength != 0:
                                    rel_strength = sum_strength/other_sum_strength
                                else:
                                    rel_strength = sum_strength/1
                                #Check that their production flow is not 0 to prevent division by 0
                                if yield_vals[i,otherciv.civNum,1] != 0:
                                    #Compute relative production
                                    rel_prod = yield_vals[i,civ.civNum,1]/yield_vals[i,otherciv.civNum,1]
                                else:
                                    rel_prod = yield_vals[i,civ.civNum,1]/1
                                #Find relative distance based off of the closest distance
                                rel_dist = close_val / dist
                                #Compute the base military strength based off turn and use that to compute war chance modifier mil_strength
                                #mil_strength is used as an entirely negative modifier for war. If this civ has less than the expected military strength
                                #at turn i then the chance of war decreases.
                                #First check that this civs sum strength is not 0 though.
                                if sum_strength != 0:
                                    mil_strength = N.log(sum_strength/(self.war_base+(self.war_mod*i)))
                                else:
                                    #set mil_strength to a value that completely prevents war
                                    mil_strength = -1
                                #Prevent mil_strength score from increasing the chance of war, there are other modifiers that do that better already.
                                if mil_strength > 0:
                                    mil_strength = 0
                                #Get the adjusted chance for war
                                adjusted_chance = self.war_chance * rel_strength * rel_prod * rel_dist + mil_strength
                                #Get a random value and see if war needs to happen
                                if adjusted_chance > N.random.uniform():
                                    #For bookkeeping purposes
                                    if print_war_peace:
                                        print("War were declared")
                                    #Civ, Turns war has gone on, Lost cities, Lost Units, Gained Cities, Killed units
                                    civ.wars.append([otherciv,0,0,0,0,0])
                                    #Tell the other civ that they are at war with this civ.
                                    otherciv.at_war.append(civ)
                    #Process War!
                    #For each war that this civ has
                    for entry in civ.wars:
                        if civ.civNum != -1:
                                #Compute Relative Strength
                                #Compute this civs military strength
                                sum_strength = 0
                                for unit in civ.mil_unit_list:
                                    sum_strength += unit.strength
                                #Compute the other civs military strength
                                other_sum_strength = 0
                                for unit in otherciv.mil_unit_list:
                                    other_sum_strength += unit.strength
                                #Check for 0 to prevent division by 0
                                if other_sum_strength != 0:
                                    rel_strength = sum_strength/other_sum_strength
                                else:
                                    #Set a flat value this time to adjust chances of city loss and gain
                                    rel_strength = 3
                                if rel_strength == 0:
                                    #Prevent a relative strength value of 0 to prevent division by 0
                                    rel_strength = 0.0001
                                #Compute our mil_strength score
                                if sum_strength != 0:
                                    #Log(our strength / expected strength)
                                    mil_strength = N.log(sum_strength/(self.war_base+(self.war_mod*i)))
                                else:
                                    mil_strength = -1
                                if mil_strength > 0:
                                    mil_strength = 0
                                #Compute their mill strength score
                                if other_sum_strength != 0:
                                    other_mil_strength = N.log(other_sum_strength/(self.war_base+(self.war_mod*i)))
                                else:
                                    other_mil_strength = -1
                                if other_mil_strength > 0:
                                    other_mil_strength = 0

                                #Lose a city (oh no)
                                #See if adjusted chance value meets the random value necessary
                                if self.loss_chance*(1/rel_strength)+other_mil_strength > N.random.uniform():
                                    #Reduce the population of the affected city.
                                    civ.city_list[-1].pop = civ.city_list[-1].pop//2
                                    #Add the city to the enemies city list
                                    entry[0].city_list.append(civ.city_list[-1])
                                    #Change the city's owner
                                    entry[0].city_list[-1].civ=entry[0]
                                    #Chance that cities tiles owner
                                    for tile in entry[0].city_list[-1].tile_list:
                                        tile.owner = entry[0]
                                    #Delete the city of the original owners city list
                                    del(civ.city_list[-1])
                                    #Increment the war entry tracking cities lost
                                    entry[2]+=1
                                    if print_war_peace:
                                        print("Lost a city!")

                                #Gain a city (yay)
                                #See if adjusted chance value meets the random value necessary
                                if self.loss_chance*(rel_strength)+mil_strength > N.random.uniform():
                                    #Cut the affected city's population in half.
                                    entry[0].city_list[-1].pop = entry[0].city_list[-1].pop//2
                                    #Add the city to this civs list
                                    civ.city_list.append(entry[0].city_list[-1])
                                    #Change the city's owner
                                    civ.city_list[-1].civ=civ
                                    #Chance the city's tile's owner
                                    for tile in civ.city_list[-1].tile_list:
                                        tile.owner = civ
                                    #Remove the city from the original owner's city list
                                    del(entry[0].city_list[-1])
                                    #Increment the war entry tracking cities gained
                                    entry[4]+=1
                                    if print_war_peace:
                                        print("gained a city!")


                                #Kill Unit!
                                #Check that their military units list is not empty
                                if len(entry[0].mil_unit_list) != 0:

                                    #Kill a percentage of their total units
                                    for times in range(int((self.loss_chance+0.1)*len(entry[0].mil_unit_list))):
                                        #Again check that their list is not empty
                                        if len(entry[0].mil_unit_list) != 0:
                                            #Delete the unit from their list
                                            del(entry[0].mil_unit_list[0])
                                            #Increment the war entry tracking units killed
                                            entry[5]+=1

                                #Lose Unit
                                #Check that this civ's military units list is not empty
                                if len(civ.mil_unit_list) != 0:
                                    #Kill a percentage of this civ's military units
                                    for times in range(int((self.loss_chance+0.1)*len(civ.mil_unit_list))):
                                        #Check that the list is not empty
                                        if len(civ.mil_unit_list) != 0:
                                            #Delete the head of the list
                                            del(civ.mil_unit_list[0])
                                            #Increment the war entry tracking units lost
                                            entry[3]+=1

                                #Other Civ has no cities and loses
                                lost = False
                                if len(entry[0].city_list) == 0:
                                    #Grab a reference to the losing civ
                                    lose_civ = entry[0]
                                    #Get all the civs that losing civ is at war with
                                    for warciv in lose_civ.at_war:
                                        #Look at their wars lists
                                        for item in warciv.wars:
                                            #remove entry if the civ they are at war with is the civ that has just lost
                                            if item[0] == lose_civ:
                                                warciv.wars.remove(item)
                                    #For wars that this civ started
                                    for war in lose_civ.wars:
                                        #Remove the flag from the other civs
                                        war[0].at_war.remove(lose_civ)
                                    #Set the losers civ number to -1 to prevent them taking a turn on accident. (Lists are immutable while iterating over.)
                                    lose_civ.civNum=-1
                                    #"Remove" the civ from the civ list.
                                    self.civs.remove(lose_civ)
                                    lost = True

                                #This civ has no cities and loses
                                if len(civ.city_list) == 0:
                                    #Get all the civs that this civ is at war with
                                    for warciv in civ.at_war:
                                        #Look at their wars
                                        for item in warciv.wars:
                                            #Check if it was with this civ
                                            if item[0] == civ:
                                                #Remove the war if it was
                                                warciv.wars.remove(item)
                                    #Look at this civs wars
                                    for war in civ.wars:
                                        #Remove war flags from civs that this civ was at war with
                                        war[0].at_war.remove(civ)
                                    #Set this civs civNum to prevent accidental turns
                                    civ.civNum=-1
                                    #Remove the civ from the civ list
                                    self.civs.remove(civ)
                                    lost = True
                                #If the civ hasn't lost, check for peace
                                if not lost:
                                    #Peace time?
                                    #Calculate an age factor that increases the chance of peace the longer the war has gone on.
                                    age_factor = entry[1]*0.005
                                    #Check that more than 0 units have been killed to prevent division by 0
                                    if entry[5] != 0:
                                        #Calculate relative units lost
                                        rel_unit_lost = entry[3]/entry[5]
                                    else:
                                        rel_unit_lost = entry[3]/1
                                    #Check that more than 0 cities have been list to prevent division by 0
                                    if entry[4] != 0:
                                        #Calculate relative cities lost
                                        rel_city_lost = entry[2]/entry[4]
                                    else:
                                        rel_city_lost = entry[2]/1
                                    #Check if its time for peace
                                    if (self.war_chance + age_factor + (0.05*rel_unit_lost) + (0.1*rel_city_lost)) > N.random.uniform():
                                        #Remove the war flag from the enemy
                                        entry[0].at_war.remove(civ)
                                        #Remove the war from this civ
                                        civ.wars.remove(entry)
                                        if print_war_peace:
                                            print("Peace in our time")
                                    else:
                                        #The civ is not dead, peace has not happened, increase the number of turns that the war has gone on.
                                        entry[1]+=1


            #Outside civ for loop but inside turn for loop
            #Check if output and every other turn
            if (i+1)%2 == 0 and output:
                #Call the dataplotter to output the current grid
                Dataplotter(self.cur_grid,savefig=True,plotType=['All'],numCiv=self.num_civ,turnNum=i+1)
        #Outside both loops
        #Check output and move back up two directories if true
        if output:
            os.chdir("..")
            os.chdir("..")
        #Return the yield values array for analysis
        return yield_vals
