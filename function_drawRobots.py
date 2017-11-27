"""
Draw Robots

ME441: Optimization Project
Author: Petras Swissler

Python Version: 2.7
Required Libraries: matplotlib, numpy

----------------------------------------------------------------------------------------------------
Revision History:
11/08/2017 (1): Initial creation of dummy file
11/16/2017 (1): Added bulk of program

----------------------------------------------------------------------------------------------------
TODO:

Implement

----------------------------------------------------------------------------------------------------
"""
###################################################################################################
# Setup
###################################################################################################
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

import time

###################################################################################################
# Classes
###################################################################################################

###################################################################################################
# Helper Functions
###################################################################################################

###################################################################################################
# Main Function
###################################################################################################

def drawRobots(Robots, xaxis, yaxis, title, fileName):
    # Set up the plot area
    fig, ax = plt.subplots()
    
    for robot in Robots:
        # Generate the vertices
        trueVert = [robot.xTrue, robot.yTrue]
        guessVert = [robot.xGuess, robot.yGuess]
        verts = [trueVert, guessVert]

        ax.plot([trueVert[0],guessVert[0]], [trueVert[1],guessVert[1]], color = 'r')
        ax.plot(trueVert[0],trueVert[1], 'o')

    plt.xlim(0,100)
    plt.ylim(0,100)

    plt.title(title)
    plt.xlabel(xaxis)
    plt.ylabel(yaxis)

    ax.set_aspect('equal')
    fig.savefig(fileName,bbox_inches='tight')
    
    #plt.show()
    #time.sleep(0)
    #plt.close()
    plt.close()
        
    return 0
#Not implemented
