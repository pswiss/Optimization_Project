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

class Robot(object):

    def__init__(self,comRange, comLossRate, comScale, comVar, xpos, ypos):
        self.comRange = comRange
        self.comLossRate = comLossRate
        self.comScale = 1+abs(1-comScale)*random()
        self.comVar = comVar

        self.xtrue = xpos
        self.ytrue = ypos
        
