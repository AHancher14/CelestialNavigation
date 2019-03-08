"""
adjustTest 
@author: Alan Hancher
Created on 2/20/2019
"""
from copy import deepcopy

"""
The purpose of this file is to test the adjust definition
First I will test red light tests, then I will test them for green light tests
"""

import unittest
import nav.adjust as nav

class adjustTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass
    
    #Testing that should return a dictionary that says
    #Error, input missing"
    def testForInformationIsMissing(self):
        actualResult = nav.adjust({'op': 'adjust'})
        expectedResult = dict({'error' :'Invalid Observation value', 'op': 'adjust'})
        self.assertEqual(actualResult, expectedResult)
    

    #testing for an invalid Height Value
    def testForInvalidHeight(self):
        acutalResult = nav.adjust({'Observation':'45d15.2', 'height':'a', 'pressure':'1010', 'horizon':'natural', 'op':'adjust','temperature':'71'})
        expectedResult = dict({'Observation':'45d15.2', 'height':'a', 'pressure':'1010', 'horizon':'natural', 'op':'adjust','temperature':'71','error':'Invalid Height value'})
        self.assertEqual(expectedResult, acutalResult)
    
    #Testing with an invalid Horizon value
    def testForInvalidHorizon(self):
        acutalResult = nav.adjust({'Observation':'45d15.2', 'height':'10', 'pressure':'1010', 'horizon':' ', 'op':'adjust','temperature':'71'})
        expectedResult = dict({'Observation':'45d15.2', 'height':'10', 'pressure':'1010', 'horizon':' ', 'op':'adjust','temperature':'71','error':'Invalid Horizon value'})
        self.assertEqual(expectedResult, acutalResult)
    #Test for a negative height value
    def testForNegativeHeightValue(self):
        acutalResult = nav.adjust({'Observation':'45d15.2', 'height':'-3', 'pressure':'1010', 'horizon':'natural', 'op':'adjust','temperature':'71'})
        expectedResult = dict({'Observation':'45d15.2', 'height':'-3', 'pressure':'1010', 'horizon':'natural', 'op':'adjust','temperature':'71','error':'Invalid Height value'})
        self.assertEqual(expectedResult, acutalResult)
        
    #Testing for a value that is less than -21
    def testForNegativeTemperature(self):
        acutalResult = nav.adjust({'Observation':'45d15.2', 'height':'10', 'pressure':'1010', 'horizon':'natural', 'op':'adjust','temperature':'-30'})
        expectedResult = dict({'Observation':'45d15.2', 'height':'10', 'pressure':'1010', 'horizon':'natural', 'op':'adjust','temperature':'-30','error':'Invalid Temperature value'})
        self.assertEqual(expectedResult, acutalResult)
    
    def testForInvalidTemperature(self):
        acutalResult = nav.adjust({'Observation':'45d15.2', 'height':'10', 'pressure':'1010', 'horizon':'natural', 'op':'adjust','temperature':'a'})
        expectedResult = dict({'Observation':'45d15.2', 'height':'10', 'pressure':'1010', 'horizon':'natural', 'op':'adjust','temperature':'a','error':'Invalid Temperature value'})
        self.assertEqual(expectedResult, acutalResult)
    
    def testForNegativePressure(self):
        acutalResult = nav.adjust({'Observation':'45d15.2', 'height':'10', 'pressure':'95', 'horizon':'natural', 'op':'adjust','temperature':'72'})
        expectedResult = dict({'Observation':'45d15.2', 'height':'10', 'pressure':'95', 'horizon':'natural', 'op':'adjust','temperature':'72','error':'Invalid Pressure value'})
        self.assertEqual(expectedResult, acutalResult)
    
    def testForInvalidPressure(self):
        acutalResult = nav.adjust({'Observation':'45d15.2', 'height':'10', 'pressure':'a', 'horizon':'natural', 'op':'adjust','temperature':'72'})
        expectedResult = dict({'Observation':'45d15.2', 'height':'10', 'pressure':'a', 'horizon':'natural', 'op':'adjust','temperature':'72','error':'Invalid Pressure value'})
        self.assertEqual(expectedResult, acutalResult)
    
    def testForInvalidAltitude(self):
        acutalResult = nav.adjust({'Observation':'ad15.2', 'height':'10', 'pressure':'150', 'horizon':'natural', 'op':'adjust','temperature':'72'})
        expectedResult = dict({'Observation':'ad15.2', 'height':'10', 'pressure':'150', 'horizon':'natural', 'op':'adjust','temperature':'72','error':'Invalid Observation value'})
        self.assertEqual(expectedResult, acutalResult)
        
    def testForNegativeAltitude(self):
        acutalResult = nav.adjust({'Observation':'-20d15.2', 'height':'10', 'pressure':'150', 'horizon':'natural', 'op':'adjust','temperature':'72'})
        expectedResult = dict({'Observation':'-20d15.2', 'height':'10', 'pressure':'150', 'horizon':'natural', 'op':'adjust','temperature':'72','error':'Invalid Observation value'})
        self.assertEqual(expectedResult, acutalResult)
    
    def testForNegativeTime(self):
        acutalResult = nav.adjust({'Observation':'45d-15.2', 'height':'10', 'pressure':'150', 'horizon':'natural', 'op':'adjust','temperature':'72'})
        expectedResult = dict({'Observation':'45d-15.2', 'height':'10', 'pressure':'150', 'horizon':'natural', 'op':'adjust','temperature':'72','error':'Invalid Observation value'})
        self.assertEqual(expectedResult, acutalResult)
    def testForInvalidTime(self):
        acutalResult = nav.adjust({'Observation':'45da', 'height':'10', 'pressure':'150', 'horizon':'natural', 'op':'adjust','temperature':'72'})
        expectedResult = dict({'Observation':'45da', 'height':'10', 'pressure':'150', 'horizon':'natural', 'op':'adjust','temperature':'72','error':'Invalid Observation value'})
        self.assertEqual(expectedResult, acutalResult)
    
    #Happy Path
    def testFirstTestToPass(self):
        acutalResult = nav.adjust({'Observation':'13d51.6', 'height':'33', 'pressure':'1010', 'horizon':'natural', 'op':'adjust','temperature':'72'})
        expectedResult = dict({'Altitude': '13d42.3', 'Observation':'13d51.6', 'height':'33', 'pressure':'1010', 'horizon':'natural', 'op':'adjust','temperature':'72'})
        self.assertDictEqual(expectedResult, acutalResult)