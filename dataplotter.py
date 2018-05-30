#-------------Import Statements--------------------------
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as N
from classlookup import ClassLookUp
#---------------------------------------------------------

class Dataplotter(object):
    """Creates a hexagonal grid displaying a map of data contained inside the inputted grid.

    Summary:
        When constructed, looks for strings listed in plot type variable and runs methods according to that.
        In those methods, creates the figure, iterates through grid creating data for the output. Then displays the grid or saves it.
    """
    def __init__ (self,grid, savefig = False, plotType=["Test"], numCiv=0, turnNum=-1):
        """Constructor for the dataplotter class.

        Summary:
            Calls methods based on method parameters and kargs.

        Method Arguments:
            grid*: The grid containing the data to be displayed.
            savefig*: Flag for saving the figure or showing it.
            plotType*: List of strings containing words used for determining which plot types to output
                        Usable Tags: "Test", "Terrain", "Civ", "All"
            numCiv*: The number of civilizations on the Grid.
            turnNum*: The current turn number, alters allPlot method only.
        """
        #If multiple plot types passed in
        for item in plotType:
            if item == "Test":
                self.testPlot(grid,savefig)
            elif item == "Terrain":
                self.terrainPlot(grid,savefig)
            elif item == "Civ":
                self.civPlot(grid,savefig,numCiv)
            elif item == "All":
                self.allPlot(grid,savefig,numCiv,turnNum)

    def testPlot(self,grid,savefig):
        """Test plot that only shows grid dimensions and no other details

        Summary:
            Creates a figure, gets current Axes, iterates through grid getting postional information
            for hexagon generation. Creates the hexagon, moves to the next grid position.
            Once all hexagons have been created, scales the plot, sets the aspect ratio, turns off the axes,
            and either saves or shows the plot.

        Method Arguments:
            grid*: the grid to be rendered
            savefig*: flag indicating whether image should be saved or shown.

        Output: if savefig is set to true, outputs an image as Civ5SimOut_Test.png
        """
        #Create Plot
        fig = plt.figure()
        #Get axes object
        axes = fig.gca()
        #Iterate through grid creating hexes in plot.
        for i in range(grid.y):
            for j in range(grid.x):
                #Get Points for hexagon
                pointsX = j+N.array([0.5,1,1,0.5,0,0])
                pointsY = grid.y-((i*0.75)+N.array([0,0.25,0.75,1,0.75,0.25]))
                #Check for row offset
                if i%2!=0:
                    pointsX = pointsX+0.5
                #Combine two arrays in one of Nx2 dimensions
                poly = N.column_stack((pointsX,pointsY))
                #Create the polygon
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

    def terrainPlot(self,grid,savefig):
        """Plots a terrain plot based off of grid data

        Summary:
            creates figure, iterates through grid creating hexagons based off of grid data, plots hexagons, adjusts figure, saves of shows image.

        Method Arguments:
            grid*: Grid class containing data to be used in generation.
            savefig*: Flag indicating if figure should be saved or shown.

        Output: if savefig is set to true, outputs an image as "Civ5SimOut_Terrain.png"
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
                #Check for row offset
                if i%2!=0:
                    pointsX = pointsX+0.5
                #Combine two arrays in one of Nx2 dimensions
                poly = N.column_stack((pointsX,pointsY))
                #Get the terrain and biome type for color
                #Create the polygon
                #Grabs biome data from the grid and runs it through the class lookup table for biome
                line = plt.Polygon(poly,edgecolor='k',facecolor=ClassLookUp.biome_lookup[grid.tiles[i,j].biome][6])
                #Draw the polygon on the plot
                axes.add_patch(line)
                #Check for terrain
                if grid.tiles[i,j].terrain != 'none':
                    #Get a smaller hexagon in the same location
                    pointsX = j + N.array([0.5,0.9,0.9,0.5,0.1,0.1])
                    pointsY = grid.y - ((i*0.75)+N.array([0.1,0.30,0.7,0.9,0.7,0.30]))
                    #Check for row offset
                    if i%2!=0:
                        pointsX = pointsX+0.5
                    #Combine the two arrays into points
                    poly = N.column_stack((pointsX,pointsY))

                    line2 = plt.Polygon(poly,facecolor=ClassLookUp.terrain_lookup[grid.tiles[i,j].terrain][6])

                    axes.add_patch(line2)
                #Check if there is a hill here and plot this polygon instead
                elif grid.tiles[i,j].elevation == 'hill':
                    pointsX = j + N.array([0.5,0.9,0.9,0.5,0.1,0.1])
                    pointsY = grid.y - ((i*0.75)+N.array([0.1,0.30,0.7,0.9,0.7,0.30]))
                    if i%2!=0:
                        pointsX = pointsX+0.5
                    poly = N.column_stack((pointsX,pointsY))

                    line2 = plt.Polygon(poly,facecolor=ClassLookUp.terrain_lookup[grid.tiles[i,j].elevation][6])

                    axes.add_patch(line2)


        #Scale image to fit plot
        axes.autoscale()
        #Set aspect ratio
        axes.set_aspect('equal','datalim')
        #Turn off axes labels
        axes.set_axis_off()

        #save or display plot
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
                #Check for row offset
                if i%2!=0:
                    pointsX = pointsX+0.5
                #Combine two arrays in one of Nx2 dimensions
                poly = N.column_stack((pointsX,pointsY))
                #Get the terrain and biome type for color

                #Create the polygon
                #Grabs biome data from the grid and runs it through the class lookup table for biome
                line = plt.Polygon(poly,edgecolor='none',facecolor=ClassLookUp.biome_lookup[grid.tiles[i,j].biome][6])
                #Draw the polygon on the plot
                axes.add_patch(line)

                #Check for terrain on the grid point
                if grid.tiles[i,j].terrain != 'none':
                    #Get smaller polygon points at same location
                    pointsX = j + N.array([0.5,0.9,0.9,0.5,0.1,0.1])
                    pointsY = grid.y - ((i*0.75)+N.array([0.1,0.30,0.7,0.9,0.7,0.30]))
                    #Check for row offset
                    if i%2!=0:
                        pointsX = pointsX+0.5
                    #Combine two arrays into points
                    poly = N.column_stack((pointsX,pointsY))

                    #create terrain hexagon
                    line2 = plt.Polygon(poly,facecolor=ClassLookUp.terrain_lookup[grid.tiles[i,j].terrain][6])
                    #Add terrain hexagon to the plot
                    axes.add_patch(line2)
                #Check for hill on spot
                elif grid.tiles[i,j].elevation == 'hill':
                    #Get smaller polygon points at same location
                    pointsX = j + N.array([0.5,0.9,0.9,0.5,0.1,0.1])
                    pointsY = grid.y - ((i*0.75)+N.array([0.1,0.30,0.7,0.9,0.7,0.30]))
                    #Check for row offset
                    if i%2!=0:
                        pointsX = pointsX+0.5
                    #Combine two arrays into points
                    poly = N.column_stack((pointsX,pointsY))
                    #Create the hexagon
                    line2 = plt.Polygon(poly,facecolor=ClassLookUp.terrain_lookup[grid.tiles[i,j].elevation][6])
                    #Add it to the plot
                    axes.add_patch(line2)
                #Check for an owner of the tile
                if grid.tiles[i,j].owner != None:
                    #Create a polygon based on owner context
                    if grid.tiles[i,j].has_city == True:
                        #Create a black hexagon to show a city
                        line3 = plt.Polygon(poly,edgecolor='none',facecolor='k')
                    else:
                        #Get the color of that civ
                        color = N.array(cmap(val[grid.tiles[i,j].owner.civNum]))
                        #Decrease opacity to let terrain show through
                        color[3] = 0.7
                        #Creat hexagon based off that color data
                        line3 = plt.Polygon(poly,edgecolor='none',facecolor=color)
                    #Add the hexagon to the plot
                    axes.add_patch(line3)

        #Scale image to fit plot
        axes.autoscale()
        #Set aspect ratio
        axes.set_aspect('equal','datalim')
        #Turn off axes labels
        axes.set_axis_off()
        #Fit the image to the figure
        fig.tight_layout()
        #Display or save plot
        if savefig:
            #Check for turn_num 
            if turnNum != -1:
                fig.savefig("Civ5SimOut_All_"+str(turnNum)+".png",dpi=200)
                #Close the figure to prevent having 500 figures open
                plt.close(fig)
            else:
                fig.savefig("Civ5SimOut_All.png",dpi=200)
        else:
            plt.show()
