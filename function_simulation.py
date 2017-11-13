"""
Localization Simulator

ME441: Optimization Project

Author: Petras Swissler

Python Version: 2.7
Required Libraries: N/A

----------------------------------------------------------------------------------------------------
Revision History:
11/08/2017 (1): Initial creation

----------------------------------------------------------------------------------------------------
TODO:

Create helper functions
Create helper class
Create function to draw robots

----------------------------------------------------------------------------------------------------
"""

###################################################################################################
# Setup
###################################################################################################
import sys
import random
random.seed('Petras Swissler')

import math
import time
###################################################################################################
# Classes
###################################################################################################

###################################################################################################
# Helper Functions
###################################################################################################
from function_drawRobots import *
from function_calcFitness import *
from function_calcError import *

###################################################################################################
# Main Function
###################################################################################################

def simulation(config, comProperties):
    print 'simStart'
    
    fitness = 0                 # Temporary value
    #----------------------------------------------------------------------------------------------
    # Setup
    # Strip out pertinant information from config and comProperties
    numRobots       = config[0]         # Number of robots to simulate
    numCycles       = config[1]         # Number of communication cycles to simulate
    showGraphics    = config[2]         # 0 1 or 2: Defines whether to draw the robots (currently not implemented)
    random.seed(config[3])              # Allows changes to randomness seed
    reportFile      = config[4]

    comRange    =   comProperties[0]    # radius
    comLossRate =   comProperties[1]    # % of time that communication is lost
    comScale    =   comProperties[2]    # Constant scale of range measurements
    comVar      =   comProperties[3]    # variance in individual range measurements
    #comEccen    =   comProperties[4]    # Eccentricity of the communication range measurements (not implemented)
    
    #----------------------------------------------------------------------------------------------
    # Initialize the simulation
    Robots = initRobots(numRobots, comRange, comLossRate, comScale, comVar)

    # Run for n cycles
    for i in range(numCycles):
        print "hi\n"
        # generate the com list (list of all communications being sent O(N)
        comList = 0 #clear the com list
        for robot in Robots:
            comList.append(robot.sendCom())

        for robot in Robots:
            # Robot takes in all communications, decides which ones it will recieve
            robot.recCom(comList)
            # Robot uses this information to localize itself
            robot.localize()

        # Compute position errors
        errors = calcError(Robots)

        # If configured to draw robots in intermediate states (2), draw them
        if showGraphics == 2:
            drawRobots(Robots)

    # Calculate the fitness of the final robot states
    fitness = calcFitness(errors, comProperties)

    # if configured to draw robots in the end (1 or 2), draw them
    if showGraphics != 0:
        drawRobots(Robots)

    return  fitness
    
