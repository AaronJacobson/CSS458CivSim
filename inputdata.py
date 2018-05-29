import numpy as N
import csv
import os

#file will be read as turn, player, gross gold, science, production, food, population, tech
#in that order. All numbers are read from 1 to 500 as in the amount of turns.
#there will be 6 2D arrays and the player will determine the first value of the index
#while 0-499 will determine the second value of the index.

os.chdir(os.path.dirname(__file__))

#create numpy arrays for each of the data being measured
gold = N.zeros((20,500), dtype = int)
science = N.zeros((20,500), dtype = int)
prod = N.zeros((20,500), dtype = int)
food = N.zeros((20,500), dtype = int)
pop = N.zeros((20,500), dtype = int)
tech = N.zeros((20,500), dtype = int)

with open("inputdata.csv") as csvfile:
    datareader = csv.reader(csvfile, delimiter = ",")
    
    #create a header to navigate through the data
    header = datareader.__next__()
    
    #create indexies for each type of data we are measuring
    turn_index = header.index("turn")
    player_index = header.index("player")
    gold_index = header.index("gold")
    science_index = header.index("science")
    prod_index = header.index("prod")
    food_index = header.index("food")
    pop_index = header.index("pop")
    tech_index = header.index("tech")
    
    #add data into respective numpy arrays
    for row in datareader:
        gold[int(row[player_index])-1][int(row[turn_index])-1] = int(row[gold_index])
        science[int(row[player_index])-1][int(row[turn_index])-1] = int(row[science_index])
        prod[int(row[player_index])-1][int(row[turn_index])-1] = int(row[prod_index])
        food[int(row[player_index])-1][int(row[turn_index])-1] = int(row[food_index])
        pop[int(row[player_index])-1][int(row[turn_index])-1] = int(row[pop_index])
        tech[int(row[player_index])-1][int(row[turn_index])-1] = int(row[tech_index])
