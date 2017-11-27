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

import numpy as np
from random import random
###################################################################################################
# Classes
###################################################################################################

###################################################################################################
# Helper Functions
###################################################################################################
from function_simulation import*
from genetic_algorithm import *
from function_initRobots import *
from arbiter import *

###################################################################################################
# Main Function
###################################################################################################
figProperties = ['imageTest','Test Title','x axis temp', 'y axis temp']
configSim = [75, 100,1,"Run"]
phenotypeArray = []

for i in range(populationNumber):
	phenotypeVals = [random(), random(), random(), random()]
	
	configSimi = configSim
	configSimi[3] = configSimi[3]+str(i)+".txt"



	fitness = simulation(configSimi, phenotypeVals,1.5,figProperties)

	appendPheno = [phenotypeVals, fitness[0]]

	phenotypeArray.append(appendPheno)

for i in range(generationsNumber):
	print "Generation "+str(i)
	population = evolve(phenotypeArray,diversityRange,mutationScale,populationNumber,retain_value, random_select, mutate_value)

	phenotypeArray = []

	for j in range(len(population)):

		
		figProps = ["Gen"+str(i)+"Member"+str(j),"Gen"+str(i)+"Member"+str(j),"x","y"]

		phenotypeVals = population[j]
				
		configSimi = configSim
		configSimi[3] = "Gen"+str(j)+"_Member"+str(i)+".txt"

		fitness = simulation(configSimi, phenotypeVals,1.5,figProps)

		appendPheno = [phenotypeVals, fitness[0]]

		phenotypeArray.append(appendPheno)





