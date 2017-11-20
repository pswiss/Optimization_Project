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
from random import setstate

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
from function_initRobots import *

###################################################################################################
# Main Function
###################################################################################################

def simulation(config, comProperties, figProperties):
    # Inputs:
    #   config: general simulation configuration
    #               0: Number of robots in the simulation
    #               1: number of cycles to simulate
    #               2: Draw behavior: 0 = never draw, 1 = draw @ end, 2 = draw after every cycle
    #               3: Filename for the report file
    #   comProperties: characteristics of robot communication, all quantities are scaled 0-1
    #               0: radius (0-comRangeScale)
    #               1: loss rate (% of time that communication is lost)
    #               2: Constant scale of range measurements (0-2) (randomized)
    #               3: variance in individual range measurements
    #               4: Hop count scaling factor
    #   figProperties: configuration for output figure
    #               0: Filename for the output figure (.png extension will be added)
    #               1: Title of the figure
    #               2: X axis Label
    #               3: Y axis Label

    
    #setState(config[5])
    
    print 'simStart'
    
    fitness = 0                 # Temporary value
    #----------------------------------------------------------------------------------------------
    # Setup
    # Strip out pertinant information from config and comProperties
    numRobots       = config[0]         # Number of robots to simulate
    numCycles       = config[1]         # Number of communication cycles to simulate
    showGraphics    = config[2]         # 0 1 or 2: Defines whether to draw the robots (currently not implemented)
    reportFile      = config[3]
    #random.seed(config[3])              # Allows changes to randomness seed

    # Com properties are passed as 0-1: Some require attenuation

    comRange    =   comProperties[0]*comRangeScale  # radius (0-comRangeScale)
    comLossRate =   comProperties[1]                # % of time that communication is lost
    comScale    =   comProperties[2]        # Constant scale of range measurements (0-2)
    comVar      =   comProperties[3]*comRange       # variance in individual range measurements
    hopScale    =   comProperties[4] # Assumed distance between robots
        
    #----------------------------------------------------------------------------------------------
    # Initialize the simulation
    Robots = initRobots(numRobots, comRange, comLossRate, comScale, comVar, hopScale)

    print 'Robots Initialized'

    ffile = open(reportFile,"a")

    # Run for n cycles
    for i in range(numCycles):
        # generate the com list (list of all communications being sent O(N)
        comList = [] #clear the com list
        for robot in Robots:
            comList.append(robot.sendCom())
        
        for robot in Robots:
            # Robot takes in all communications, decides which ones it will recieve
            robot.recCom(comList)
            # Robot uses this information to localize itself
            robot.localize()

        # Compute position errors
        errors = calcError(Robots)
        # Write the errors to the file
        reportString = ''
        for k, error in enumerate(errors):
            if k==0:
                reportString = str(error)
            else:
                reportString = reportString+', '+str(error)
        reportString = reportString+';\n'
        
        ffile.write(reportString)
        
        # If configured to draw robots in intermediate states (2), draw them
        imageString = figProperties[0]+'_'+str(i)+'.png'
        title = figProperties[1]+' Run '+str(i)
        if showGraphics == 2:
            drawRobots(Robots, figProperties[2], figProperties[3], title,imageString)

        #print sum(errors)/len(errors)
            
    ffile.close()
    # Calculate the fitness of the final robot states
    fitness = calcFitness(errors, comProperties)
    
    #print fitness
    

    # if configured to draw robots in the end (1 or 2), draw them
    imageString = figProperties[0]+'_final.png'
    title = figProperties[1]+' Final'
    if showGraphics != 0:
        drawRobots(Robots, figProperties[2], figProperties[3], title,imageString)

    return  fitness
    
