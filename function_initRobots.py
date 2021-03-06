"""
Initialize Robots

ME441: Optimization Project
Author: Petras Swissler

Python Version: 2.7
Required Libraries: N/A

----------------------------------------------------------------------------------------------------
Revision History:
11/12/2017 (1): Creation of file
11/15/2017 (1): Fixed infinite Loop bug

----------------------------------------------------------------------------------------------------
TODO:

Implement

----------------------------------------------------------------------------------------------------
"""
###################################################################################################
# Setup
###################################################################################################


###################################################################################################
# Classes
###################################################################################################
from class_robot import *

###################################################################################################
# Helper Functions
###################################################################################################
from function_calcDistance import *
from random import *

###################################################################################################
# Main Function
###################################################################################################

def initRobots(numRobots, comRange, comLossRate, comScale, comVar, hopScale, robotPlacement):
    # This function will create an array of non-overlapping robots

    robotList = []

    # First create the seeds
    for i in range(numSeeds):
        robotToAdd = Robot(comRange, comLossRate, comScale, comVar, seedX[i], seedY[i], i+1,hopScale)
        robotList.append(robotToAdd)

    #Then create the others
    for position in robotPlacement:
        xAdd = position[0]
        yAdd = position[1]

        # Add the robot at the valid coordinate
        robotToAdd = Robot(comRange, comLossRate, comScale, comVar, xAdd, yAdd, 0, hopScale)
        robotList.append(robotToAdd)

    return robotList
