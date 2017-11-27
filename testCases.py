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

###################################################################################################
# Main Function
###################################################################################################
# Configure the write location
direct = os.path.dirname(os.path.abspath(__file__))+'\\'+str(datetime.now()).replace(":",".")+'\\'
os.makedirs(direct)
# Start the file
ffile = open(direct+genReportFile,"a")
ffile.write('Run Start: '+str(datetime.now())+'\n')
ffile.close()

# Input prototypes
figProperties = [direct + 'imageTest','Test Title','x axis temp', 'y axis temp']
configSimDefault = [75, 100,1,"Run"]
phenotypeArray = []

# First, create the first generation
for i in range(populationNumber):
	# All genes scaled 0-1. Assume no information regarding the genes
	phenotypeVals = [random(), random(), random(), random()]

	# Calculate the average fitness for the phenotype
	newFit = []
	for k in range(numSimPerFit):
		# Format the output text file
		configSim = configSimDefault
		configSim[3] = direct+'init'+str(i)+'-'+str(k)+".txt"

		newFit.append(simulation(configSim, phenotypeVals,1.5,figProperties)[0])
	fitness = sum(newFit) / len(newFit)

	# Append the phenotype and fitness to the overall array
	appendPheno = [phenotypeVals, fitness]
	phenotypeArray.append(appendPheno)

# Loop through all generations
for i in range(generationsNumber):
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

			newFit.append(simulation(configSim, phenotypeVals,1.5,figProperties)[0])
		fitness = sum(newFit) / len(newFit)

		# Add the new phenotype to the overall array
		appendPheno = [phenotypeVals, fitness]
		phenotypeArray.append(appendPheno)

	# Pull out the best performing member of each population and record it
	phenotypeSorted = sorted(phenotypeArray,key=lambda x: x[1])	#population sorted in ascending order
	ffile = open(direct+genReportFile,"a")
	ffile.write('Gen'+str(i)+'Complete at: '+str(datetime.now())+'\n')
	ffile.write(str(phenotypeSorted[len(phenotypeSorted)]))
	ffile.close()

	# Simulate the best performer and export an image
	# Configure how the figure looks
	figProps = [direct+"Gen"+str(i)+"Best","Gen"+str(i)+"Best","x","y"]
	# Configure the output text file
	configSim = configSimDefault
	configSim[3] = direct+"Gen"+str(j)+"Best.txt"
	configSim[2] = 1
	simulation(configSim, phenotypeSorted[len(phenotypeSorted)],1.5,figProperties)

# End the file
ffile = open(direct+genReportFile,"a")
ffile.write('Run Start: '+str(datetime.now())+'\n')
ffile.close()
