"""
Simulator Test Cases

ME441: Optimization Project

Author: Petras Swissler

Python Version: 2.7
Required Libraries: N/A

----------------------------------------------------------------------------------------------------
Revision History:
11/08/2017 (1): Initial creation

----------------------------------------------------------------------------------------------------
TODO:

Make easy to configure

----------------------------------------------------------------------------------------------------
"""

###################################################################################################
# Setup
###################################################################################################
import sys
import random

import math
import time
###################################################################################################
# Classes
###################################################################################################

###################################################################################################
# Helper Functions
###################################################################################################
from function_simulation import*

###################################################################################################
# Main Function
###################################################################################################

config =        [100, 100, 0, "testRun.txt"]
comProperties = [.2, .1, .1, .1, 1.5]
figProperties = ['imageTest','Test Tile','x axis temp', 'y axis temp']


sumOverallFit = 0
sumDistFit = 0
sumCostFit = 0
k = 0

fit = simulation(config, comProperties, figProperties)

print fit

"""for i in range(2):
    fit = simulation(config, comProperties, figProperties)
    k = k+1
    sumOverallFit = sumOverallFit + fit[0]
    sumDistFit = sumDistFit + fit[1]
    sumCostFit = sumCostFit + fit[2]
avgOverall = sumOverallFit / k
avgDist = sumDistFit / k
avgCost = sumCostFit / k

print [avgOverall, avgDist, avgCost]"""
