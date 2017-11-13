"""
Initialize Robots

ME441: Optimization Project
Author: Petras Swissler

Python Version: 2.7
Required Libraries: N/A

----------------------------------------------------------------------------------------------------
Revision History:
11/12/2017 (1): Creation of file

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

def initRobots(numRobots, comRange, comLossRate, comScale, comVar):
    # This function will create an array of non-overlapping robots

    robotList = []
    
    # First create the seeds
    for i in range(numSeeds):
        robotToAdd = Robot(comRange, comLossRate, comScale, comVar, seedX[i], seedY[i], i+1)
        robotList.append(robotToAdd)

    #Then create the others
    for i in range(numRobots - numSeeds):
        okToAdd = False

        # Search for a location to put the robot
        while ~okToAdd:
            # Assume it will be ok
            okToAdd = True

            xCheck = random() * arenaX
            yCheck = random() * arenaY

            # Check for interference with all robots
            for robot in robotList:
                if roboDiam > calcDistance([xCheck, yCheck],[robot.xTrue, robot.yTrue]):
                    okToAdd = False
                    break
                #
            #
        # Add the robot at the valid coordinate
        robotToAdd = Robot(comRange, comLossRate, comScale, comVar, xCheck, yCheck, 0)
        robotList.append(robotToAdd)
        
    return robotList

