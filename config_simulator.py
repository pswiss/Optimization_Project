"""
Configuration file for the simulator
"""

# Number of cycles to do hop count localization
cyclesForHop = 20

# Number of Newton-Raphson iterations to run for each localization Cycle
numIterNR = 5

# Scale of the gradient points
gradScale = 0.05

# Bonus weight for seeds when calculating gradient
seedWeight = 1

# Seed properties
numSeeds = 2
seedX = [0, 100]
seedY = [0, 0]

# Arena Properties
arenaX = 100
arenaY = 100

# Robot Dimensions
roboDiam = 10

# Communication Scaling
comRangeScale = 100

# Fitness variables
fitnessRatio = 0.5

costRange = 1
costLossRate = 1
costScale = 1
costVar = 1


# For hopcount localization, estimate where the message is coming from
hopScale = 2*roboDiam

