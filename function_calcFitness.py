"""
Calculate Fitness

ME441: Optimization Project

Author: Petras Swissler

Python Version: 2.7
Required Libraries: N/A

----------------------------------------------------------------------------------------------------
Revision History:
11/08/2017 (1): Initial creation
11/15/2017 (1): Wrote bulk of program

----------------------------------------------------------------------------------------------------
TODO:

Create

----------------------------------------------------------------------------------------------------
"""

###################################################################################################
# Setup
###################################################################################################
from config_simulator import *

###################################################################################################
# Classes
###################################################################################################

###################################################################################################
# Helper Functions
###################################################################################################
from function_calcDistance import *

###################################################################################################
# Main Function
###################################################################################################
def calcFitness(errors, comProperties):
    fitness = 0

    # Calculate the portion of the fitness due to position errors
    sumSqError = 0
    for err in errors:
        sumSqError = sumSqError + err
    
    fitnessPositionError = len(errors) / sumSqError

    # Calculate the portion of the fitness due to part cost
    #                               Range                           Loss Rate                               Scaling                         Variance
    componentCost = costRange*comProperties[0] + costLossRate*(1-comProperties[1]) + costScale*(2*abs(0.5-comProperties[2])) + costVar * comProperties[3]

    fitnessCost = 1/componentCost
    
    # Calculate the overall cost

    fitness = fitnessRatio * fitnessPositionError + (1-fitnessRatio)*fitnessCost
    
    return [fitness, fitnessPositionError, fitnessCost]
