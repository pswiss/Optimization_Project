"""
Robot Class

ME441: Optimization Project

Author: Petras Swissler

Python Version: 2.7
Required Libraries: N/A

----------------------------------------------------------------------------------------------------
Revision History:
11/08/2017 (1): Initial creation

----------------------------------------------------------------------------------------------------
TODO:

Implement

----------------------------------------------------------------------------------------------------
"""

# import the configuration variables
from config_simulator import *

class Robot(object):
    ################################################################################################
    # Constructor Function
    def __init__(self,comRange, comLossRate, comScale, comVar, xpos, ypos, isSeed):
        self.comRange = comRange
        self.comLossRate = comLossRate
        self.comVar = comVar
        # Calculate the linear scale of the communication
        self.comScale = 1+comScale*(2*random()-1)

        self.xTrue = xpos
        self.yTrue = ypos

        self.amSeed = isSeed

        # If am a seed, I know my true position
        if self.amSeed != 0:
            self.xGuess = xTrue
            self.yGuess = yTrue
            
        # Otherwise I do not
        else:
            self.xGuess = 0
            self.yGuess = 0

        # Timer variables
        self.hopLocalizeTimer = 0

        # Hop Count Variables
        self.hop1 = 0
        self.hop2 = 0

        
        

    ################################################################################################
    # Send communication function
    # This function packages the message the robot wants to send
    def sendCom(self):
        # Create array I want to send
        comOut = [self.hop1, self.hop2, self.xGuess, self.yGuess, self.xTrue, self.yTrue]

        return comOut

    ################################################################################################
    # Recieve communication function
    # This function recieves the global communication array and determines which ones it can see
    def recCom(self, globalComArray):

        for com in globalComArray:
            # Calculate the true distance between the two robots
            distance = 
            
        
        
        
