"""
Configuration file for the simulator
"""

# Number of cycles to do hop count localization
cyclesForHop = 20

# Number of Newton-Raphson iterations to run for each localization Cycle
numIterNR = 5

# For hopcount localization, estimate where the message is coming from
hopScale = 0.3

# Scale of the gradient points
gradScale = 0.01

# Bonus weight for seeds when calculating gradient
seedWeight = 20

# Seed properties
numSeeds = 2
seedX = [0, 100]
seedY = [0, 0]

# Arena Properties
arenaX = 150
arenaY = 150

# Robot Dimensions
roboDiam = 10

