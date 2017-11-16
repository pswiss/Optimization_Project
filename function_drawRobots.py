"""
Draw Robots

ME441: Optimization Project
Author: Petras Swissler

Python Version: 2.7
Required Libraries: N/A

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

def drawRobots(Robots):
    # Set up the plot area
    fig, ax = plt.subplots()
    
    for robot in Robots:
        # Generate the vertices
        trueVert = [robot.xTrue, robot.yTrue]
        guessVert = [robot.xGuess, robot.yGuess]
        verts = [trueVert, guessVert]

        ax.plot([trueVert[0],guessVert[0]], [trueVert[1],guessVert[1]], color = 'r')
        ax.plot(trueVert[0],trueVert[1], 'o')

    plt.xlim(0,200)
    plt.ylim(0,200)
    plt.show()
    time.sleep(0)
    plt.close()
        
    
    return 0
#Not implemented
