"""
Robot Class

ME441: Optimization Project

Author: Petras Swissler

Python Version: 2.7
Required Libraries: N/A

----------------------------------------------------------------------------------------------------
Revision History:
11/08/2017 (1): Initial creation
11/10/2017 (1): Added recCom function

----------------------------------------------------------------------------------------------------
TODO:

Implement Localization
Implement Calculate Error Function

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

        # Hop Count Variables
        self.hop1 = 0
        self.hop2 = 0

        # Known seed locations
        self.hop1x = -1
        self.hop1y = -1
        self.hop2x = -1
        self.hop2y = -1

        # If am a seed, I know my true position
        if self.amSeed != 0:
            self.xGuess = self.xTrue
            self.yGuess = self.yTrue
            # And I therefore know the true position of the seed
            if self.amSeed == 1:
                self.hop1x = self.xTrue
                self.hop1y = self.yTrue
            else:
                self.hop2x = self.xTrue
                self.hop2y = self.yTrue
        # Otherwise I do not
        else:
            self.xGuess = 0
            self.yGuess = 0

        # Timer variables
        self.hopLocalizeTimer = 0

        

    ################################################################################################
    # Send communication function
    # This function packages the message the robot wants to send
    def sendCom(self):
        # Create array I want to send
        comOut = [self.hop1, self.hop2, self.xGuess, self.yGuess, self.xTrue, self.yTrue, self.hop1x, self.hop1y, self.hop2x, self.hop2y]

        return comOut

    ################################################################################################
    # Recieve communication function
    # This function recieves the global communication array and determines which ones it can see
    def recCom(self, globalComArray):
        
        # Clear all recieved communications
        self.recievedComs = []

        for message in globalComArray:
            
            # Calculate the true distance between the two robots
            xDelta = abs(message[5] - self.xTrue)
            yDelta = abs(message[6] - self.yTrue)
            distance = sqrt(xDelta^2 + yDelta^2)
            # Check if within range
            if distance > self.comRange:
                recieveCom = False
            else:
                # Check if message is randomly lost
                if random() < self.comLossRate:
                    recieveCom = False
                else:
                    recieveCom = True

            # If message is recieved, append it to the recieved Coms List
            if recieveCom == True:
                self.recievedComs.append(message)

        # All recieved messages have been added. This function does not pass any values
        return

    ################################################################################################
    # Calculate error function
    # This function returns the distance error from its estimated position and its true position
    def calcError(self):
        # Calculate the true distance between the two robots
        xDelta = abs(self.xGuess - self.xTrue)
        yDelta = abs(self.yGuess - self.yTrue)
        distanceError = sqrt(xDelta^2 + yDelta^2)

        # return the error
        return distanceError
        
    ################################################################################################
    # Localization function
    # This function has two modes: 1) Hop count localization 2) Triangulation Localization. Both use Newton Raphson
    def localize(self):
        # Decrement hop localization timer

        # Check each message for updated hop seed locations

        # If hop count
        # Check what the lowest hopcount of any message I see is for hop1 and hop2
        # Update to that number + 1

        # If hop done, use triangulation
        # Create two gradient eval points
        # Calculate the position error for each of the three points (guess + grads)
        # Sum the Errors

        # Run n iterations of Newton Raphson to get new guess positions

        # Assign new guess

        return
        






















        
