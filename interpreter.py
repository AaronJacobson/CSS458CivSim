class Interpreter(object):

    def __init__(self):
        return

    def write(self, grid):
        return

    def read(self, gameNumber, turnNumber, game):
        #varify that variables is indeed what they should be
        #if(game)

        #varify that gameNum is resonable
        if(type(gameNumber) is int):
            if(gameNumber > 0):
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
