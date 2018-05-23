
class Interpreter(object):

    def __init__(self):
        return

    def write(self, game):
        #self.gridFile = game.grid
        self.mapFile = open("testMap","w")
        self.civFile = open("testCiv","w")
        self.cityFile = open("testCities","w")
        self.unitFile = open("testUnits", "w")

        #get from grid and write all the info about each tile
        for self.x in range(game.grid.x):
            for self.y in range(game.grid.y):
                mapFile.write(self.x + " " + self.y + " ") #add grid features like terrain and stuff

        #get from Civs and write all info about each civ
        for self.civNum in game.civs:
            civsFile.write(self.civNum + " ")

        #get from Cities and write all info about each cities
        for self.city in grid.cities:
            citiesFile.write(self.city.x + " " + self.city.y + " " + self.city.civ + ""
            + self.city.pop + " " + self.city.food + " " + self.city.production + " "
            + self.city.health + " " + self.city.strength + " ")
            for self.building in self.city.building_list:
                citiesFile.write(self.building + "$")
            citiesFile.write("EOL")
        #--------------------------------------------------------

        #get from Units and write all info about each units
        for self.unit in grid.units:
            unitFile.write(self.unit.name + " " + )



        return

    def read(self, game):

        #varify that variables is indeed what they should be
        #if(game)

        #varify that gameNum is resonable
        if(type(game.gameNumber) is int):
            if(game.gameNumber > 0):
                gameNum = gameNumber
            else:
                #Exception
        else:
            #Exception

        #varify that turnNum is reasoable
        if(type(turnNumber) is int):
            if(turnNumber > 0 and turnNumber <= 500):
                turnNum = turnNumber
            else:
                #Exception
        else:
            #Exception


        return
