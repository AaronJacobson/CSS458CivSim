
class Interpreter(object):

    def __init__(self):
        return

    def write(self, grid):

    '''
        #get from grid and write all the info about each tile
        self.mapFile = open("testMap","w")

        for self.x in range(game.grid.x):
            for self.y in range(game.grid.y):
                mapFile.write(self.x + " " + self.y + " " + ) #add grid features like terrain and stuff
        self.mapFile.close()
        #--------------------------------------------------------------


        #get from Civs and write all info about each civ
        self.civFile = open("testCiv","w")
        for self.civNum in game.civs:
            civsFile.write(self.civNum + " ")
        self.civFile.close()
        #-------------------------------------------------------

        #get from Cities and write all info about each cities
        self.cityFile = open("testCities","w")
        for self.city in grid.cities:
            citiesFile.write(self.city.x + " " + self.city.y + " " + self.city.civ + "" \
            + self.city.pop + " " + self.city.food + " " + self.city.production + " " \
            + self.city.health + " " + self.city.strength + " ")
            for self.building in self.city.building_list:
                citiesFile.write(self.building + "$")
            citiesFile.write("EOL")
        self.cityFile.close()
        #--------------------------------------------------------

        #get from Units and write all info about each units
        self.unitFile = open("testUnits", "w")
        for self.unit in grid.units:
            unitFile.write(self.unit.name + " " + )
        self.unitFile.close()
        #--------------------------------------------------------
    '''
    return

    #get from grid and write all the info about each tile
    def writeMap(self, grid):
        self.mapFile = open("testMap","w")
        for x in range(grid.x):
            for y in range(grid.y):
                tile = grid.tiles[y][x]
                mapFile.write(
                x + " " +
                y + " " +
                tile.elevation + " " +
                tile.biome + " " +
                tile.terrain + " " +
                tile.improvement + " " +
                tile.unit + " " +
                tile.city + " " +
                tile.owner + " " +
                tile.food_yield + " " +
                tile.prod_yield + " " +
                tile.science_yield + " " +
                tile.gold_yield + " " +
                tile.road + "\n") #add grid features like terrain and stuff
        self.mapFile.close()
        return
    #--------------------------------------------------------------


    #get from Civs and write all info about each civ
    def writeCiv(self, grid):
        self.civFile = open("testCiv","w")
        for self.civNum in game.civs:
            civsFile.write(self.civNum + " ")
        self.civFile.close()
        return
    #-------------------------------------------------------

    #get from Cities and write all info about each cities
    def writeCities(self, grid):
        self.cityFile = open("testCities","w")
        for self.city in grid.cities:
            citiesFile.write(
            self.city.x + " " +
            self.city.y + " " +
            self.city.civ + " " +
            self.city.pop + " " +
            self.city.food + " " +
            self.city.production + " " +
            self.city.health + " " +
            self.city.strength + " " +)

            for self.building in self.city.building_list:
                citiesFile.write(self.building + "$")
            citiesFile.write("EOL\n")
        self.cityFile.close()
        return
    #------------------------------------------------------

    #get from Units and write all info about each units
    def writeUnits(self, grid):
        self.unitFile = open("testUnits", "w")
        for unit in grid.units:
            unitFile.write(
            unit.x + " " +
            unit.y + " " +
            unit.name + " " +
            unit.health + " " +
            unit.speed + " " +
            unit.atype + " " +
            unit.prod_cost + " " +
            unit.strength + " " +
            unit.civ + " " +
            unit.airdrop)
        self.unitFile.close()
        return
    #--------------------------------------------------------

    def read(self, game):

        #varify that variables is indeed what they should be
        #if(game)


        #varify that gameNum is resonable
        if(type(game.gameNumber) is int):
            if(game.gameNumber > 0):
                gameNum = gameNumber
            else:
                pass
                #Exception
        else:
            pass
            #Exception

        #varify that turnNum is reasoable
        if(type(turnNumber) is int):
            if(turnNumber > 0 and turnNumber <= 500):
                turnNum = turnNumber
            else:
                pass
                #Exception
        else:
            pass
            #Exception


        return
