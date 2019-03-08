'''
Created on Mar 4, 2019

@author: AJ Hancher
'''
import unittest
import nav.predict as nav

class PredictTest(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass

    #Sad Path Tests
    
    #Test 1: MandatoryInformationMissing
    #input: {'op': 'predict'}
    #result: {'error':'mandatory information is missing', 'op': 'predict'}
    def testMandatoryInformationMissing(self):
        actualResult = nav.predict({'op': 'predict'})
        expectedResult = {'error':'mandatory information is missing', 'op': 'predict'}
        self.assertDictEqual(actualResult, expectedResult)
    
    #Test 2: secondsGreaterThan60
    #input: {'op':'predict', 'body': 'Betelgeuse', 'date': '2016-01-17', 'time': '03:15:99'}
    #result = {'op':'predict', 'body': 'Betelgeuse', 'date': '2016-01-17', 'time': '03:15:99', 'error':'invalid time'}
    def testSecondsGreaterThan60(self):
        actualResult = nav.predict({'op':'predict', 'body': 'Betelgeuse', 'date': '2016-01-17', 'time': '03:15:99'})
        expectedResult = {'op':'predict', 'body': 'Betelgeuse', 'date': '2016-01-17', 'time': '03:15:99', 'error':'invalid time'}
        self.assertDictEqual(actualResult, expectedResult)
    
    #Test 3: SecondsLessThan00
    #input: {'op':'predict', 'body': 'Betelgeuse', 'date': '2016-01-17', 'time': '03:15:-01'}
    #result = {'op':'predict', 'body': 'Betelgeuse', 'date': '2016-01-17', 'time': '03:15:-01', 'error':'invalid time'}
    def testSecondsLessThan00(self):
        actualResult = nav.predict({'op':'predict', 'body': 'Betelgeuse', 'date': '2016-01-17', 'time': '03:15:-01'})
        expectedResult = {'op':'predict', 'body': 'Betelgeuse', 'date': '2016-01-17', 'time': '03:15:-01', 'error':'invalid time'}
        self.assertDictEqual(actualResult, expectedResult)
    
    #Test 4: MinutesGreaterThan60
    #input: {'op':'predict', 'body': 'Betelgeuse', 'date': '2016-01-17', 'time': '03:61:10'}
    #result = {'op':'predict', 'body': 'Betelgeuse', 'date': '2016-01-17', 'time': '03:61:10', 'error':'invalid time'}
    def testMinutesGreaterThan60(self):
        actualResult = nav.predict({'op':'predict', 'body': 'Betelgeuse', 'date': '2016-01-17', 'time': '03:61:10'})
        expectedResult = {'op':'predict', 'body': 'Betelgeuse', 'date': '2016-01-17', 'time': '03:61:10', 'error':'invalid time'}
        self.assertDictEqual(actualResult, expectedResult)
    
    #Test 5: MinutesLessThan00
    #input: {'op':'predict', 'body': 'Betelgeuse', 'date': '2016-01-17', 'time': '03:-01:10'}
    #result = {'op':'predict', 'body': 'Betelgeuse', 'date': '2016-01-17', 'time': '03:-01:10', 'error':'invalid time'}
    def testMinutesLessThan00(self):
        actualResult = nav.predict({'op':'predict', 'body': 'Betelgeuse', 'date': '2016-01-17', 'time': '03:-01:10'})
        expectedResult = {'op':'predict', 'body': 'Betelgeuse', 'date': '2016-01-17', 'time': '03:-01:10', 'error':'invalid time'}
        self.assertDictEqual(actualResult, expectedResult)
    
    #Test 6: HourGreaterThan60
    #input: {'op':'predict', 'body': 'Betelgeuse', 'date': '2016-01-17', 'time': '24:59:10'}
    #result = {'op':'predict', 'body': 'Betelgeuse', 'date': '2016-01-17', 'time': '24:59:10', 'error':'invalid time'}
    def testHourGraterThan60(self):
        actualResult = nav.predict({'op':'predict', 'body': 'Betelgeuse', 'date': '2016-01-17', 'time': '24:59:10'})
        expectedResult = {'op':'predict', 'body': 'Betelgeuse', 'date': '2016-01-17', 'time': '24:59:10', 'error':'invalid time'}
        self.assertDictEqual(actualResult, expectedResult)
    
    #Test 7: HourLessThan00
    #input: {'op':'predict', 'body': 'Betelgeuse', 'date': '2016-01-17', 'time': '-01:59:10'}
    #result = {'op':'predict', 'body': 'Betelgeuse', 'date': '2016-01-17', 'time': '-01:59:10', 'error':'invalid time'}
    def testHourLessThan00(self):
        actualResult = nav.predict({'op':'predict', 'body': 'Betelgeuse', 'date': '2016-01-17', 'time': '-01:59:10'})
        expectedResult = {'op':'predict', 'body': 'Betelgeuse', 'date': '2016-01-17', 'time': '-01:59:10', 'error':'invalid time'}
        self.assertDictEqual(actualResult, expectedResult)
    
    #Test 8: Month Greater than 12
    #input: {'op':'predict', 'body': 'Betelgeuse', 'date': '2016-99-17', 'time': '03:15:42'}
    #result = {'op':'predict', 'body': 'Betelgeuse', 'date': '2016-99-17', 'time': '03:15:42', 'error':'invalid date'}
    def testMonthGreaterThan12(self):
        actualResult = nav.predict({'op':'predict', 'body': 'Betelgeuse', 'date': '2016-99-17', 'time': '03:15:42'})
        expectedResult = {'op':'predict', 'body': 'Betelgeuse', 'date': '2016-99-17', 'time': '03:15:42', 'error':'invalid date'}
        self.assertDictEqual(actualResult, expectedResult)
    
    #Test 9: Month Less than 01
    #input: {'op':'predict', 'body': 'Betelgeuse', 'date': '2016-00-17', 'time': '03:15:42'}
    #result = {'op':'predict', 'body': 'Betelgeuse', 'date': '2016-00-17', 'time': '03:15:42', 'error':'invalid date'}
    def testMonthLessThan01(self):
        actualResult = nav.predict({'op':'predict', 'body': 'Betelgeuse', 'date': '2016-00-17', 'time': '03:15:42'})
        expectedResult = {'op':'predict', 'body': 'Betelgeuse', 'date': '2016-00-17', 'time': '03:15:42', 'error':'invalid date'}
        self.assertDictEqual(actualResult, expectedResult)
    
    #Test 10: Year Greater than 2100
    #input: {'op':'predict', 'body': 'Betelgeuse', 'date': '2101-01-17', 'time': '03:15:42'}
    #result = {'op':'predict', 'body': 'Betelgeuse', 'date': '2101-01-17', 'time': '03:15:42', 'error':'invalid date'}
    def testYearGreaterThan2100(self):
        actualResult= nav.predict({'op':'predict', 'body': 'Betelgeuse', 'date': '2101-01-17', 'time': '03:15:42'})
        expectedResult = {'op':'predict', 'body': 'Betelgeuse', 'date': '2101-01-17', 'time': '03:15:42', 'error':'invalid date'}
        self.assertDictEqual(actualResult, expectedResult)
    
    #Test 11: Year Less than 2001
    #input: {'op':'predict', 'body': 'Betelgeuse', 'date': '2000-01-15', 'time': '03:15:42'}
    #result = {'op':'predict', 'body': 'Betelgeuse', 'date': '2000-01-15', 'time': '03:15:42', 'error':'invalid date'}
    def testYearLessThan2001(self):
        actualResult = nav.predict({'op':'predict', 'body': 'Betelgeuse', 'date': '2000-01-15', 'time': '03:15:42'})
        expectedReuslt = {'op':'predict', 'body': 'Betelgeuse', 'date': '2000-01-15', 'time': '03:15:42', 'error':'invalid date'}
        self.assertDictEqual(actualResult, expectedReuslt)
    
    #Test 12: Day greater than 31
    #input: {'op':'predict', 'body': 'Betelgeuse', 'date': '2016-01-35', 'time': '03:15:42'}
    #result = {'op':'predict', 'body': 'Betelgeuse', 'date': '2016-01-35', 'time': '03:15:42', 'error':'invalid date'}
    def testDayGreaterThan31(self):
        actualResult = nav.predict({'op':'predict', 'body': 'Betelgeuse', 'date': '2016-01-35', 'time': '03:15:42'})
        expectedResult = {'op':'predict', 'body': 'Betelgeuse', 'date': '2016-01-35', 'time': '03:15:42', 'error':'invalid date'}
        self.assertDictEqual(actualResult, expectedResult)
    
    #Test 13: Day Less than 00
    #input: {'op':'predict', 'body': 'Betelgeuse', 'date': '2001-01-00', 'time': '03:15:42'}
    #result = {'op':'predict', 'body': 'Betelgeuse', 'date': '2001-01-00', 'time': '03:15:42', 'error':'invalid date'}
    def testDayLessThan01(self):
        actualResult = nav.predict({'op':'predict', 'body': 'Betelgeuse', 'date': '2001-01-00', 'time': '03:15:42'})
        expectedResult = {'op':'predict', 'body': 'Betelgeuse', 'date': '2001-01-00', 'time': '03:15:42', 'error':'invalid date'}
        self.assertDictEqual(actualResult, expectedResult)
       
    #Test 14: Body Not in Catalog
    #input: {'op':'predict', 'body': 'abcd', 'date': '2016-01-17', 'time': '03:15:42'}
    #result = {'op':'predict', 'body': 'abcd', 'date': '2016-01-17', 'time': '03:15:42', 'error':'star not in catalog'}
    def testBodyNotInCatalog(self):
        actualResult = nav.predict({'op':'predict', 'body': 'abcd', 'date': '2016-01-17', 'time': '03:15:42'})
        expectedResult = {'op':'predict', 'body': 'abcd', 'date': '2016-01-17', 'time': '03:15:42', 'error':'star not in catalog'}
        self.assertDictEqual(actualResult, expectedResult)
    
    #Test 15: invalid body type
    #input: {'op':'predict', 'body': 12, 'date': '2016-01-17', 'time': '03:15:42'}
    #result: {'op':'predict', 'body': 12, 'date': '2016-01-17', 'time': '03:15:42', 'error':'star not in catalog'}
    def testInvalidBodyType(self):
        actualResult = nav.predict({'op':'predict', 'body': 12, 'date': '2016-01-17', 'time': '03:15:42'})
        expectedResult = {'op':'predict', 'body': 12, 'date': '2016-01-17', 'time': '03:15:42', 'error':'star not in catalog'}
        self.assertDictEqual(actualResult, expectedResult)
    
    #Test 16: missingBody
    #input: {'op':'predict', 'date': '2016-01-17', 'time': '03:15:42'}
    #result = {'op':'predict', 'date': '2016-01-17', 'time': '03:15:42', 'error':'star not in catalog'}
    def testMissingBody(self):
        actualResult = nav.predict({'op':'predict', 'date': '2016-01-17', 'time': '03:15:42'})
        expectedResult = {'op':'predict', 'date': '2016-01-17', 'time': '03:15:42', 'error':'mandatory information missing'}
        self.assertDictEqual(actualResult, expectedResult)
    
    
    
     
    ###END OF SAD PATH TESTS
    ###NOW ON TO THE HAPPY PATH
    
    #Test 17: firstHappyPath
    #input: {'op':'predict', 'body': 'Aldebaran', 'date': '2016-01-17', 'time': '03:15:42'}
    #result = {'op':'predict', 'body': 'Aldebaran', 'date': '2016-01-17', 'time': '03:15:42', 'long':'95d53.6', 'lat':'16d32.3'}
    def testFirstHappyPath(self):
        actualResult = nav.predict({'op':'predict', 'body': 'Aldebaran', 'date': '2016-01-17', 'time': '03:15:42'})
        expectedResult = {'op':'predict', 'body': 'Aldebaran', 'date': '2016-01-17', 'time': '03:15:42', 'long':'95d41.6', 'lat':'16d32.3'}
        self.assertDictEqual(actualResult, expectedResult)
    
    #Test 18: HappyPathTest2
    #input: {'op':'predict', 'body': 'Betelgeuse', 'date': '2016-01-17', 'time': '03:15:42'}
    #{'op':'predict', 'body': 'Betelgeuse', 'date': '2016-01-17', 'time': '03:15:42', 'long':'75d53.6', 'lat':'7d24.3'}
    def testHappyPath2(self):
        actualResult = nav.predict({'op':'predict', 'body': 'Betelgeuse', 'date': '2016-01-17', 'time': '03:15:42'})
        expectedResult = {'op':'predict', 'body': 'Betelgeuse', 'date': '2016-01-17', 'time': '03:15:42', 'long':'75d53.6', 'lat':'7d24.3'}
        self.assertDictEqual(actualResult, expectedResult)
    
    
    #Test 19: HappyPathTest3
    #Input: {'op':'predict', 'body': 'Gacrux', 'date': '2017-04-10', 'time': '14:22:36'}
    #result: {'op':'predict', 'body': 'Gacrux', 'date': '2017-04-10', 'time': '14:22:36', 'long':'226d37.2', 'lat':'-57d11.9'}
    def testHappyPathTest3(self):
        actualResult = nav.predict({'op':'predict', 'body': 'Gacrux', 'date': '2017-04-10', 'time': '14:22:36'})
        expectedResult = {'op':'predict', 'body': 'Gacrux', 'date': '2017-04-10', 'time': '14:22:36', 'long':'226d37.2', 'lat':'-57d11.9'}
        self.assertDictEqual(actualResult, expectedResult)
    
    #Test 20: Feburary 29
    #input: {'op':'predict', 'body': 'Betelgeuse', 'date': '2016-02-29', 'time': '03:15:42'}
    #result = {'op':'predict', 'body': 'Betelgeuse', 'date': '2016-02-29', 'time': '03:15:42', 'long':'87d43.3','lat':'7d24.3'}
    def testForValidFeburaryDay(self):
        actualResult = nav.predict({'op':'predict', 'body': 'Betelgeuse', 'date': '2016-02-29', 'time': '03:15:42'})
        expectedResult = {'op':'predict', 'body': 'Betelgeuse', 'date': '2016-02-29', 'time': '03:15:42', 'long':'118d16.5','lat':'7d24.3'}
        self.assertDictEqual(actualResult, expectedResult)
    