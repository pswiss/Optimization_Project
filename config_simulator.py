"""
Configuration file for the simulator
"""

# Number of cycles to do hop count localization
cyclesForHop = 20

# Number of Newton-Raphson iterations to run for each localization Cycle
numIterNR = 5

# Scale of the gradient points
gradScale = 0.1

# Bonus weight for seeds when calculating gradient
seedWeight = 5

# Arena Properties
arenaX = 75
arenaY = 75

# Seed properties
numSeeds = 2
seedX = [0, arenaX]
seedY = [0, 0]

# Robot Dimensions
roboDiam = 10

# Communication Scaling
comRangeScale = 100

# Fitness variables
fitnessRatio = 0.5

normDistFit = 35
normCostFit = 7

costRange = 1.15
costLossRate = 4.31
costScale = 1.15
costVar = 2.38
