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

from datetime import datetime
import os
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
from function_placeRobots import *
from config_simulator import *

###################################################################################################
# Main Function
###################################################################################################
# Default run parameters
hopScale = 3.5
numRobots = 50
simCycles = 100
configSimDefault = [numRobots, simCycles,0,"Run"]

# Configure the write location
direct = os.path.dirname(os.path.abspath(__file__))+'\\'+str(datetime.now()).replace(":",".")+'\\'
os.makedirs(direct)
# Start the file
ffile = open(direct+genReportFile,"a")
ffile.write('Run Start: '+str(datetime.now())+'\n')
ffile.write(str(configSimDefault)+'\n')
ffile.close()

# More input prototypes
figProperties = [direct + 'imageTest','Test Title','x axis temp', 'y axis temp']
phenotypeArray = []

# Generate position for the first generationsNumber
robotPositions = placeRobots(numRobots)

# First, create the first generation
for i in range(populationNumber):
	figProperties = [direct + 'imageTest'+str(i),'Test Title','x axis temp', 'y axis temp']
	# All genes scaled 0-1. Scale to guesses
	phenotypeVals = [random(), random(), 0.5*random(), 0.5*random()]

	# Calculate the average fitness for the phenotype
	newFit = []
	for k in range(numSimPerFit):
		# Format the output text file
		configSim = configSimDefault
		configSim[3] = direct+'init'+str(i)+'-'+str(k)+".txt"

		newFit.append(simulation(configSim, phenotypeVals,hopScale,figProperties,robotPositions)[0])
	fitness = sum(newFit) / len(newFit)

	# Append the phenotype and fitness to the overall array
	appendPheno = [phenotypeVals, fitness]
	phenotypeArray.append(appendPheno)

# Loop through all generations
for i in range(generationsNumber):
	# Create robot positions for this generation
	robotPositions = placeRobots(numRobots)

	# Tracking print statement
	print "Generation "+str(i)

	# First step in a generation is to create the new generation based on the fitness of the prior generation
	population = evolve(phenotypeArray,diversityRange,mutationScale,populationNumber,retain_value, random_select, mutate_value)

	# Create the new phenotype array
	phenotypeArray = []

	# Loop through all of the population
	for j, phenotypeVals in enumerate(population):
		# Calculate the average fitness for the phenotype
		newFit = []
		for k in range(numSimPerFit):
			# Configure how the figure looks
			figProps = [direct+"Gen"+str(i)+"Member"+str(j),"Gen"+str(i)+"Member"+str(j)+"-"+str(k),"x","y"]
			# Configure the output text file
			configSim = configSimDefault
			configSim[3] = direct+"Gen"+str(i)+"_Member"+str(j)+"-"+str(k)+".txt"
			configSim[2] = 0

			newFit.append(simulation(configSim, phenotypeVals,hopScale,figProps,robotPositions)[0])
		fitness = sum(newFit) / len(newFit)

		# Add the new phenotype to the overall array
		appendPheno = [phenotypeVals, fitness]
		phenotypeArray.append(appendPheno)

	# Pull out the best performing member of each population and record it
	phenotypeSorted = sorted(phenotypeArray,key=lambda x: x[1])	#population sorted in ascending order
	ffile = open(direct+genReportFile,"a")
	ffile.write('Gen'+str(i)+'Complete at: '+str(datetime.now())+'\n')
	ffile.write(str(phenotypeSorted[-1]))
	ffile.close()

	# Simulate the best performer and export an image
	# Configure how the figure looks
	figProps = [direct+"Gen"+str(i)+"Best","Gen"+str(i)+"Best","x","y"]
	# Configure the output text file
	configSim = configSimDefault
	configSim[3] = direct+"Gen"+str(i)+"Best.txt"
	configSim[2] = 1
	simulation(configSim, phenotypeSorted[-1][0],hopScale,figProps,robotPositions)

# End the file
ffile = open(direct+genReportFile,"a")
ffile.write('Run End: '+str(datetime.now())+'\n')
ffile.close()
