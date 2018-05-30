#-------------Import Statements--------------------------
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as N
from classlookup import ClassLookUp
#---------------------------------------------------------

class Dataplotter(object):
    """
    Summary:
        This class plots a grid and displays several demographic maps with a
        variation of different information being diplayed. Information such as
        city size, food, and reasorce distrbution.
    """
    def __init__ (self,grid, savefig = False, plotType=["Test"], numCiv=0, turnNum=-1):
        """
        Summary:
            This is the constructor, it initializes the plots that will be used to
            visualize the simulation.

        Method Arguments:
            grid:       The grid that holds all the info nessesary to visualize
                        the simulation.
            savefig:    Confirms if the image needs to be saved. If so it is
                        saved in the same file as the program.
            plotType:   Tells you what kind of plot that should be made. The four
                        options: Test, Terrain, Civ, All
            numCiv:     The number of civilizations playing the game.
            turnNum:    The turn number that should be plotted.
        """
        #If multiple plot types passed in
        for item in plotType:
            if item == "Test":
                self.testPlot(grid,savefig,turnNum)
            elif item == "Terrain":
                self.terrainPlot(grid,savefig,turnNum)
            elif item == "Civ":
                self.civPlot(grid,savefig,numCiv,turnNum)
            elif item == "All":
                self.allPlot(grid,savefig,numCiv,turnNum)

    def testPlot(self,grid,savefig,turnNum):
        """
        Summary:
            This method plots the map without any cities or units or terrain
            distiguishment.

        Method Arguments:
            grid:       The grid that holds all the info nessesary to visualize
                        the simulation.
            savefig:    Confirms if the image needs to be saved. If so it is
                        saved in the same file as the program.
            turnNum:    The turn number that should be plotted.
        """
        #Create Plot
        fig = plt.figure()
        axes = fig.gca()
        #Iterate through grid creating hexes in plot.
        for i in range(grid.y):
            for j in range(grid.x):
                #Get Points for hexagon
                pointsX = j+N.array([0.5,1,1,0.5,0,0])
                pointsY = grid.y-((i*0.75)+N.array([0,0.25,0.75,1,0.75,0.25]))
                if i%2!=0:
                    pointsX = pointsX+0.5
                #Combine two arrays in one of Nx2 dimensions
                poly = N.column_stack((pointsX,pointsY))
                #Create the polygon
                #Color Stuff goes in here!
                line = plt.Polygon(poly,edgecolor='k',facecolor='g')
                #Draw the polygon on the plot
                axes.add_patch(line)

        #Scale image to fit plot
        axes.autoscale()
        #Set aspect ratio
        axes.set_aspect('equal','datalim')
        #Turn off axes labels
        axes.set_axis_off()

        #Display or save plot
        if savefig:
            fig.savefig("Civ5SimOut_Test.png",dpi=300)
        else:
            plt.show()

    def terrainPlot(self,grid,savefig,turnNum):
        """
        Summary:
            This method plots the map without any cities or units. This method
            will only distiguish terrain type.

        Method Arguments:
            grid:       The grid that holds all the info nessesary to visualize
                        the simulation.
            savefig:    Confirms if the image needs to be saved. If so it is
                        saved in the same file as the program.
            turnNum:    The turn number that should be plotted.
        """
        #Create Plot
        fig = plt.figure()
        axes = fig.gca()
        #Iterate through grid creating hexes in plot.
        for i in range(grid.y):
            for j in range(grid.x):
                #Get Points for hexagon
                pointsX = j+N.array([0.5,1,1,0.5,0,0])
                pointsY = grid.y-((i*0.75)+N.array([0,0.25,0.75,1,0.75,0.25]))
                if i%2!=0:
                    pointsX = pointsX+0.5
                #Combine two arrays in one of Nx2 dimensions
                poly = N.column_stack((pointsX,pointsY))
                #Get the terrain and biome type for color

                #Create the polygon
                #Color Stuff goes in here!
                line = plt.Polygon(poly,edgecolor='k',facecolor=ClassLookUp.biome_lookup[grid.tiles[i,j].biome][6])
                #Draw the polygon on the plot
                axes.add_patch(line)

                if grid.tiles[i,j].terrain != 'none':
                    pointsX = j + N.array([0.5,0.9,0.9,0.5,0.1,0.1])
                    pointsY = grid.y - ((i*0.75)+N.array([0.1,0.30,0.7,0.9,0.7,0.30]))
                    if i%2!=0:
                        pointsX = pointsX+0.5
                    poly = N.column_stack((pointsX,pointsY))

                    #line2 = plt.Polygon(poly,edgecolor=Game.terrain_lookup[grid.tiles[i,j].terrain][6],facecolor='none',linewidth=4)
                    line2 = plt.Polygon(poly,facecolor=ClassLookUp.terrain_lookup[grid.tiles[i,j].terrain][6])

                    axes.add_patch(line2)
                elif grid.tiles[i,j].elevation == 'hill':
                    pointsX = j + N.array([0.5,0.9,0.9,0.5,0.1,0.1])
                    pointsY = grid.y - ((i*0.75)+N.array([0.1,0.30,0.7,0.9,0.7,0.30]))
                    if i%2!=0:
                        pointsX = pointsX+0.5
                    poly = N.column_stack((pointsX,pointsY))

                    #line2 = plt.Polygon(poly,edgecolor=Game.terrain_lookup[grid.tiles[i,j].terrain][6],facecolor='none',linewidth=4)
                    line2 = plt.Polygon(poly,facecolor=ClassLookUp.terrain_lookup[grid.tiles[i,j].elevation][6])

                    axes.add_patch(line2)


        #Scale image to fit plot
        axes.autoscale()
        #Set aspect ratio
        axes.set_aspect('equal','datalim')
        #Turn off axes labels
        axes.set_axis_off()

        #Display or save plot
        if savefig:
            fig.savefig("Civ5SimOut_Terrain.png",dpi=300)
        else:
            plt.show()
    def civPlot(self,grid,savefig,numCiv,turnNum):
        """
        Summary:
            This method plots the map with cities and different terrain type.

        Method Arguments:
            grid:       The grid that holds all the info nessesary to visualize
                        the simulation.
            savefig:    Confirms if the image needs to be saved. If so it is
                        saved in the same file as the program.
            turnNum:    The turn number that should be plotted.
        """
        #Check for zero civs
        if numCiv <= 0:
            raise ValueError("Cannot plot civs when there are 0 or less of them")
        #Create Plot
        fig = plt.figure()
        axes = fig.gca()
        #Get CMap and Value array
        cmap = plt.get_cmap('gist_rainbow')
        val = N.arange(0,1,1/numCiv)
        #Iterate through grid creating hexes in plot.
        for i in range(grid.y):
            for j in range(grid.x):

                #Get Points for hexagon
                pointsX = j+N.array([0.5,1,1,0.5,0,0])
                pointsY = grid.y-((i*0.75)+N.array([0,0.25,0.75,1,0.75,0.25]))
                if i%2!=0:
                    pointsX = pointsX+0.5
                #Combine two arrays in one of Nx2 dimensions
                poly = N.column_stack((pointsX,pointsY))

                if grid.tiles[i,j].owner != 'none':
                    #Create a polygon based on owner context
                    if grid.tiles[i,j].has_city == True:
                        line = plt.Polygon(poly,edgecolor='k',facecolor='k')
                    else:
                        color = N.array(cmap(val[grid.tiles[i,j].owner.civNum]))
                        color[3] = 0.7
                        line = plt.Polygon(poly,edgecolor='k',facecolor=color)
                else:
                    #Create a "blank" polygon
                    line = plt.Polygon(poly,edgecolor='k',facecolor='lightgrey')
                #line = plt.Polygon(poly,edgecolor='k',facecolor=Game.biome_lookup[grid.tiles[i,j].biome][6])

                #Draw the polygon on the plot
                axes.add_patch(line)

        #Scale image to fit plot
        axes.autoscale()
        #Set aspect ratio
        axes.set_aspect('equal','datalim')
        #Turn off axes labels
        axes.set_axis_off()

        #Display or save plot
        if savefig:
            fig.savefig("Civ5SimOut_Civs.png",dpi=300)
        else:
            plt.show()


    def allPlot(self,grid,savefig,numCiv,turnNum):
        """
        Summary:
            This method plots the map with cities and different terrain type and
            all units on the grid.

        Method Arguments:
            grid:       The grid that holds all the info nessesary to visualize
                        the simulation.
            savefig:    Confirms if the image needs to be saved. If so it is
                        saved in the same file as the program.
            turnNum:    The turn number that should be plotted.
        """
        #Create Plot
        fig = plt.figure()
        axes = fig.gca()

        #Get CMap and Value array
        cmap = plt.get_cmap('gist_rainbow')
        val = N.arange(0,1,1/numCiv)
        #Iterate through grid creating hexes in plot.
        for i in range(grid.y):
            for j in range(grid.x):
                #Get Points for hexagon
                pointsX = j+N.array([0.5,1,1,0.5,0,0])
                pointsY = grid.y-((i*0.75)+N.array([0,0.25,0.75,1,0.75,0.25]))
                if i%2!=0:
                    pointsX = pointsX+0.5
                #Combine two arrays in one of Nx2 dimensions
                poly = N.column_stack((pointsX,pointsY))
                #Get the terrain and biome type for color

                #Create the polygon
                #Color Stuff goes in here!
                line = plt.Polygon(poly,edgecolor='none',facecolor=ClassLookUp.biome_lookup[grid.tiles[i,j].biome][6])
                #Draw the polygon on the plot
                axes.add_patch(line)

                if grid.tiles[i,j].terrain != 'none':
                    pointsX = j + N.array([0.5,0.9,0.9,0.5,0.1,0.1])
                    pointsY = grid.y - ((i*0.75)+N.array([0.1,0.30,0.7,0.9,0.7,0.30]))
                    if i%2!=0:
                        pointsX = pointsX+0.5
                    poly = N.column_stack((pointsX,pointsY))

                    #line2 = plt.Polygon(poly,edgecolor=Game.terrain_lookup[grid.tiles[i,j].terrain][6],facecolor='none',linewidth=4)
                    line2 = plt.Polygon(poly,facecolor=ClassLookUp.terrain_lookup[grid.tiles[i,j].terrain][6])

                    axes.add_patch(line2)
                elif grid.tiles[i,j].elevation == 'hill':
                    pointsX = j + N.array([0.5,0.9,0.9,0.5,0.1,0.1])
                    pointsY = grid.y - ((i*0.75)+N.array([0.1,0.30,0.7,0.9,0.7,0.30]))
                    if i%2!=0:
                        pointsX = pointsX+0.5
                    poly = N.column_stack((pointsX,pointsY))

                    #line2 = plt.Polygon(poly,edgecolor=Game.terrain_lookup[grid.tiles[i,j].terrain][6],facecolor='none',linewidth=4)
                    line2 = plt.Polygon(poly,facecolor=ClassLookUp.terrain_lookup[grid.tiles[i,j].elevation][6])

                    axes.add_patch(line2)
                if grid.tiles[i,j].owner != None:
                    #Create a polygon based on owner context
                    if grid.tiles[i,j].has_city == True:
                        #line3 = plt.Polygon(poly,edgecolor='none',facecolor=cmap(val[grid.tiles[i,j].owner.civNum]))
                        line3 = plt.Polygon(poly,edgecolor='none',facecolor='k')
                    else:
                        color = N.array(cmap(val[grid.tiles[i,j].owner.civNum]))
                        color[3] = 0.7
                        line3 = plt.Polygon(poly,edgecolor='none',facecolor=color)
                    axes.add_patch(line3)

                #Draw the polygon on the plot

        #Scale image to fit plot
        axes.autoscale()
        #Set aspect ratio
        axes.set_aspect('equal','datalim')
        #Turn off axes labels
        axes.set_axis_off()
        fig.tight_layout()
        #Display or save plot
        if savefig:
            if turnNum != -1:
                fig.savefig("Civ5SimOut_All_"+str(turnNum)+".png",dpi=200)
                plt.close(fig)
            else:
                fig.savefig("Civ5SimOut_All.png",dpi=200)
        else:
            plt.show()
