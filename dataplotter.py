#

#Import Statements
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as N
from classlookup import ClassLookUp


class Dataplotter(object):
    """
    """
    def __init__ (self,grid, savefig = False, plotType=["Test"], numCiv=0):
        """
        """
        #If multiple plot types passed in
        for item in plotType:
            if item == "Test":
                self.testPlot(grid,savefig)
            elif item == "Terrain":
                self.terrainPlot(grid,savefig)
            elif item == "Civ":
                self.civPlot(grid,savefig,numCiv)
        
    def testPlot(self,grid,savefig):
        """
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
    
    def terrainPlot(self,grid,savefig):
        """
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
                
                if grid.tiles[i,j].terrain != None:
                    pointsX = j + N.array([0.5,0.9,0.9,0.5,0.1,0.1])
                    pointsY = grid.y - ((i*0.75)+N.array([0.1,0.30,0.7,0.9,0.7,0.30]))
                    if i%2!=0:
                        pointsX = pointsX+0.5
                    poly = N.column_stack((pointsX,pointsY))
                    
                    #line2 = plt.Polygon(poly,edgecolor=Game.terrain_lookup[grid.tiles[i,j].terrain][6],facecolor='none',linewidth=4)
                    line2 = plt.Polygon(poly,facecolor=ClassLookUp.terrain_lookup[grid.tiles[i,j].terrain][6])
                    
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
    def civPlot(self,grid,savefig,numCiv):
        """
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
                
                if grid.tiles[i,j].owner != None:
                    #Create a polygon based on owner context
                    if grid.tiles[i,j].has_city == True:
                        line = plt.Polygon(poly,edgecolor='k',facecolor=cmap(val[grid.tiles[i,j].owner.civNum]))
                    else:
                        color = N.array(cmap(val[grid.tiles[i,j].owner.civNum]))                      
                        color[3] = 0.5
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
        