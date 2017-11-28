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
11/12/2017 (1): First attempt complete
11/15/2017 (1): Syntactical Bugs Fixed

----------------------------------------------------------------------------------------------------
TODO:

Work on localizationmethod

----------------------------------------------------------------------------------------------------
"""

###################################################################################################
# Setup
###################################################################################################
# import the configuration variables
from config_simulator import *
from random import *
import time

###################################################################################################
# Classes
###################################################################################################

###################################################################################################
# Helper Functions
###################################################################################################
from function_calcDistance import *
from function_newtonRaphson import *

###################################################################################################
# Main Class
###################################################################################################
class Robot(object):
    ###############################################################################################
    # Constructor Function
    def __init__(self,comRange, comLossRate, comScale, comVar, xpos, ypos, isSeed, hopScale):
        self.comRange = comRange
        self.comLossRate = comLossRate
        self.comVar = comVar
        # Calculate the linear scale of the communication
        self.comScale = 1+comScale*(2*random()-1)

        self.hopScale = hopScale*roboDiam

        self.xTrue = xpos
        self.yTrue = ypos

        self.amSeed = isSeed

        # Hop Count Variables
        self.hop1 = 5000
        self.hop2 = 5000

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
                self.hop1 = 0
                self.hop1x = self.xTrue
                self.hop1y = self.yTrue
            if self.amSeed == 2:
                self.hop2 = 0
                self.hop2x = self.xTrue
                self.hop2y = self.yTrue
        # Otherwise I do not
        else:
            self.xGuess = random()*arenaX
            self.yGuess = random()*arenaY

        # Timer variables
        self.hopLocalizeTimer = cyclesForHop

    ###############################################################################################
    # Send communication function
    # This function packages the message the robot wants to send
    def sendCom(self):
        # Create array I want to send
        #           0           1           2           3           4           5           6           7           8           9
        comOut = [self.hop1, self.hop2, self.xGuess, self.yGuess, self.xTrue, self.yTrue, self.hop1x, self.hop1y, self.hop2x, self.hop2y]

        return comOut

    ###############################################################################################
    # Recieve communication function
    # This function recieves the global communication array and determines which ones it can see
    def recCom(self, globalComArray):

        # Clear all recieved communications
        self.recievedComs = []
        self.rangeMeasurements = []

        # Check to see if recieve communication messages
        for message in globalComArray:

            # Calculate the true distance between the two robots
            distance = calcDistance([self.xTrue, self.yTrue],[message[4], message[5]])

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
                # Calculate the range measurements
                rangeMeas = max(0,distance * self.comScale + normalvariate(0,pow(self.comVar,0.5)))

                self.recievedComs.append([message,rangeMeas])

        # All recieved messages have been added. This function does not pass any values

        return

    ###############################################################################################
    # Calculate error function
    # This function returns the distance error from its estimated position and its true position
    def calcError(self):
        # Calculate the true distance between robot's expected and true position
        distanceError = calcDistance([self.xTrue, self.yTrue],[self.xGuess, self.yGuess])

        # return the error
        return distanceError

    ###############################################################################################
    # Localization function
    # This function has two modes: 1) Hop count localization 2) Triangulation Localization. Both use Newton Raphson
    def localize(self):
        # Check what the lowest hopcount of any message I see is for hop1 and hop2
        # Update to that number + 1
        # Check each message for updated hop seed locations

        hop1average = 0;
        hop2average = 0;
        msgcnt = 0

        for msg in self.recievedComs:
            msgcnt = msgcnt + 1

            hop1average = ((msgcnt -1)*hop1average + msg[0][0])/(msgcnt+.001)
            hop2average = ((msgcnt -1)*hop2average + msg[0][1])/(msgcnt+.001)

            if (self.hop1 > (msg[0][0]+1)):
                # Update my hop count information
                self.hop1 = msg[0][0] + 1
                self.hop1x = msg[0][6]
                self.hop1y = msg[0][7]

            if (self.hop2 > (msg[0][1]+1)):
                # Update my hop count information
                self.hop2 = msg[0][1] + 1
                self.hop2x = msg[0][8]
                self.hop2y = msg[0][9]

        # Decrement hop localization timer
        self.hopLocalizeTimer = max(0,self.hopLocalizeTimer-1)

        # If hop count timer hasn't expired, localize based on hop-count
        if self.hopLocalizeTimer > 0:
            # Estimate how far I am from the the seeds
            hop1dist = hop1average * (self.hopScale ) + 0.01
            hop2dist = hop2average * (self.hopScale ) + 0.01

            # Assign new guess if not a seed
            if self.amSeed == 0:
                # Assume up against wall, seed is only in x
                # Derived using geometry
                #self.yGuess = pow( (pow(hop1dist,2)-pow(hop2dist,2))/((pow(hop1dist,2)/pow(hop2dist,2)+.001)-(pow(hop2dist,2)/pow(hop1dist,2)+.01)+.001),0.5)
                #self.xGuess = pow( pow(hop1dist,2)-pow(self.yGuess,2),0.5)
                L = abs(self.hop2x - self.hop1x)

                self.xGuess = (L*L+hop1dist*hop1dist-hop2dist*hop2dist)/(2*L+0.00001)
                self.yGuess =   pow(abs(((L + hop1dist + hop2dist)*(L + hop1dist - hop2dist)*(L - hop1dist + hop2dist)*(hop1dist - L + hop2dist))),0.5)/(2*L+0.001)

            else:
                self.xGuess = self.xTrue
                self.yGuess = self.yTrue

        else:
            # If hop done, use triangulation
            # Run n iterations of Newton Raphson to get new guess positions
            for i in range(numIterNR):

                # Create current point and two gradient eval points
                currentGuess = [self.xGuess, self.yGuess]

                gradStepX = gradScale
                gradStepY = gradScale

                xGradEval = [self.xGuess+gradStepX, self.yGuess]
                yGradEval = [self.xGuess, self.yGuess+gradStepY]

                # Calculate the position error for each of the three points (guess + grads)
                currentError = 0
                xGradError = 0
                yGradError = 0

                # Iterate through each recieved message and sum the Errors

                for msg in self.recievedComs:
                    reportedPoint = [msg[0][2],msg[0][3]]
                    # special case for if message is a seed: Weight higher
                    if (msg[0][0] == 0) or (msg[0][1] == 0):
                        currentError = currentError + pow(seedWeight*abs(msg[1] - calcDistance(currentGuess, reportedPoint)),2)
                        xGradError = xGradError + pow(seedWeight*abs(msg[1] - calcDistance(xGradEval, reportedPoint)),2)
                        yGradError = yGradError + pow(seedWeight*abs(msg[1] - calcDistance(yGradEval, reportedPoint)),2)

                    else:
                        currentError = currentError + pow(abs(msg[1] - calcDistance(currentGuess, reportedPoint)),2)
                        xGradError = xGradError + pow(abs(msg[1] - calcDistance(xGradEval, reportedPoint)),2)
                        yGradError = yGradError + pow(abs(msg[1] - calcDistance(yGradEval, reportedPoint)),2)


                # Calculate the gradient
                xGrad = (xGradError-currentError)/(gradStepX+.001)
                yGrad = (yGradError-currentError)/(gradStepY+.001)

                #if self.hopLocalizeTimer == 0:
                    #print [xGrad, yGrad, currentError, xGradError, yGradError, gradStepX, gradStepY]

                # Assign new guess if not a seed
                if self.amSeed == 0:
                    #self.xGuess = newtonRaphson(self.xGuess, currentError/1000.0, -xGrad)
                    #self.yGuess = newtonRaphson(self.yGuess, currentError/1000.0, -yGrad)
                    if xGradError < currentError:
                        self.xGuess = self.xGuess+gradStepX/2.0
                    else:
                        self.xGuess = self.xGuess-gradStepX/2.0

                    if yGradError < currentError:
                        self.yGuess = self.yGuess+gradStepY/2.0
                    else:
                        self.yGuess = self.yGuess-gradStepY/2.0

                    # Error Recovery:
                    if self.xGuess < 0:
                        self.xGuess = 1
                    if self.yGuess < 0:
                        self.yGuess = 1

                    """if self.xGuess > arenaX:
                        self.xGuess = arenaX - 0.5
                    if self.yGuess > arenaY:
                        self.yGuess = arenaY - 0.5"""

                else:
                    self.xGuess = self.xTrue
                    self.yGuess = self.yTrue
                #
            #
        #
        return
    #
#
