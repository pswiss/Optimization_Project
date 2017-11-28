"""
Place Robots

ME441: Optimization Project
Author: Petras Swissler

Python Version: 2.7
Required Libraries: N/A

----------------------------------------------------------------------------------------------------
Revision History:
11/27/2017: Created
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
def placeRobots(numRobots):
    # This function will create an array of non-overlapping robots

    placementList = []

    #Then create the others
    for i in range(numRobots - numSeeds):
        okToAdd = False

        # Search for a location to put the robot
        while not okToAdd:
            # Generate a random Point in the arena
            xCheck = random() * arenaX
            yCheck = random() * arenaY

            okToAdd = True
            # Check for interference with all robots
            for j, robotPos in enumerate(placementList):
                dist = calcDistance([xCheck, yCheck],[robotPos[0], robotPos[1]])
                # Check that far enough away
                if dist < (roboDiam/2):
                    okToAdd = False
                #
            #
        # Add the robot at the valid coordinate
        positionToAdd = [xCheck,yCheck]
        placementList.append(positionToAdd)

    return placementList
