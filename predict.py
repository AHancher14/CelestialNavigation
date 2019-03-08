'''
Created on Mar 4, 2019

@author: AJ Hancher
'''

import xlrd
import datetime
import math

#Returns the Number Of Leap Years Between 2001 and what ever year is specified
def returnNumberOfLeapYears(year):
    year = int(year)
    leapYear = year - 2001
    leapYear = leapYear / 4
    return leapYear

#Returns the answer in the string form
def getStringFormat(answer):
    remainder = answer / 60
    remainder = math.floor(remainder)
    multiplyRemainder = remainder * 60
    subtraction = answer - multiplyRemainder
    subtraction = round(subtraction, 1)
    finalAnswer = str(remainder) + "d" + str(subtraction)
    return finalAnswer

#Converts the string to an integer and then performs the calculations
def getNumberFromString(number):
    num1 = number.split("d")[0]
    num2 = number.split("d")[1]
    num1 = float(num1)
    num2 = float(num2)
    num1 = num1*60
    num3 = num1 + num2
    return num3

#Finds the seconds in the minute
def findSecondsInMinute(minute):
    minute = minute * 60
    return minute
#Finds seconds in an hour
def findSecondsInHour(hour):
    secondsInHour = 3600
    secondsInHour = secondsInHour * hour
    return secondsInHour
#Finds seconds in a day
def findSecondsInDay(day):
    secondsINDay = 86400
    numOfSeconds = day * secondsINDay
    return numOfSeconds
#Finds seconds in months
def findSecondsInMonth(month):
    numberOfDaysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month = month - 1
    numberOfDays = 0
    numberOfSecondsInMonth = 0
    if(month >= 0):
        while month >= 0:
            numberOfDays = numberOfDaysInMonth[month] + numberOfDays
            month = month - 1
            numberOfSecondsInMonth = numberOfDays * 86400
        
    
    return numberOfSecondsInMonth

def predict(values):
    
    #Check to make sure that the information is there
    time = "00-00-00"
    if 'time' in values:
        time = values['time']
    else:
        values['error'] = 'mandatory information is missing'
        return values
    #Split the time values with the : to get the individual values
    hour = time.split(":")[0]
    minute = time.split(":")[1]
    seconds = time.split(":")[2]
    
    #Checking the seconds value first to make sure that it is in the bounds given
    try:
        seconds = int(seconds)
    except:
        values['error'] = "invalid time"
        return values
    if(seconds <= 00 or seconds > 60):
        values['error'] = "invalid time"
        return values
    
    #Checking the minutes values to see if they are within the bounds that were given
    try:
        minute = int(minute)
    except:
        values['error'] = "invalid time"
        return values
    if(minute < 00 or minute > 60):
        values['error'] = "invalid time"
        return values
    
    #Checking to see if the hour value is within the constraints
    try:
        hour = int(hour)
    except:
        values['error'] = "invalid time"
        return values
    if(hour <= 00 or hour >= 24):
        values['error'] = "invalid time"
        return values
    
    #Next we have to split the date into its different parts of:
    #YYYY - year
    #MM - month
    #DD - Day
    #The date gets set to 2001-01-01 if there is not a date value in the input
    date = "2001-01-01"
    if 'date' in values:
        date = values['date']
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
    except:
        values['error'] = "invalid date"
        return values
    year = date.split("-")[0]
    month = date.split("-")[1]
    day = date.split("-")[2]
    
    #Testing the Month Value
    try:
        month = int(month)
    except:
        values['error'] = "invalid date"
        return values
    if(month < 1 or month > 12):
        values['error'] = "invalid date"
        return values
    
    #Testing the Year Value
    try:
        year = int(year)
    except:
        values['error'] = "invalid date"
        return values
    if(year < 2001 or year > 2100):
        values['error'] = "invalid date"
        return values
    
    #Testing the Day Value
    #I've set the number of days to 31 to start testing
    try:
        day = int(day)
    except:
        values['error'] = "invalid date"
        return values
    if(day < 01 or day > 31):
        values['error'] = "invalid date"
        return values
    
    #Testing the body values
    #Check to see if their is a body value
    #If not, return an error since its mandatory
    if 'body' in values:
        body = values['body']
    else:
        values['error'] = "mandatory information missing"
        return values
    
    #I will use lists to hold the individual values and then index them
    #First list will be for the star name
    starList = []
    starAngle = []
    starDeclination = []
    #The next step is to open the spreadsheet using a function provided by the xlrd 
    #Source: https://www.geeksforgeeks.org/reading-excel-file-using-python/
    fileLocation = "starData.xlsx"
    #Open the worksheet
    star = xlrd.open_workbook(fileLocation)
    
    starData = star.sheet_by_index(0)
    starData.cell_value(0, 0)
    
    #All this for loop is doing is adding the names of the stars to the list
    for i in range(2, starData.nrows):
        starName = starData.cell_value(i, 0)
        starList.append(starName)
    
    #Test to make sure the body input is a string
    try:
        body = str(body)
    except:
        values['error'] = "star not in catalog"
        return values
    #Next we check to see if the body value is in the list
    if(body in starList):
        index = starList.index(body)
    else:
        values['error'] = "star not in catalog"
        return values
    
    #Next we need to populate the starAngle list
    for j in range(2, starData.nrows):
        ang = starData.cell_value(j, 1)
        starAngle.append(ang)
    
    #Lastly we need to populate the starDeclination list
    for k in range(2, starData.nrows):
        dec = starData.cell_value(k, 2)
        starDeclination.append(dec)
    
    declination = starDeclination[index]
    hourAngle = starAngle[index]
    
    ariesDate = "2001-01-01"
    
    ghaAries = "100d42.6"
    ariesYear = ariesDate.split("-")[0]
    ariesYear = int(ariesYear)
    year = int(year)
    difference = year - ariesYear
    ghaAriesDecrease = "-0d14.31667"
    ghaAriesTime = ghaAriesDecrease.split("d")[1]
    ghaAriesTime = float(ghaAriesTime)


    ghaAriesTry = ghaAriesTime * difference
    ghaAriesTry = float(ghaAriesTry)
    

    divideBy60 = ghaAriesTry / 60
    divideBy60 = int(divideBy60)


    multiplyBy60 = divideBy60 * (60)
    divideBy60 = 0 - divideBy60
    firstPart =  ghaAriesTry - multiplyBy60
    firstPart = 0 - firstPart
    firstPart = round(firstPart, 1)
    
    cumulativeProgression = str(divideBy60) + "d" + str(firstPart)
    
    leapYear = returnNumberOfLeapYears(year)
    
    #Part B
    amountOfDailyRotation = "0d59.0"
    amountOfDailyRotation = amountOfDailyRotation.split("d")[1]
    amountOfDailyRotation = float(amountOfDailyRotation)
    leapProgressionStr = amountOfDailyRotation * leapYear
    leapProgression = getStringFormat(leapProgressionStr)
     
    #Part C
    #GHAAries = GHAAries + Cumulative Progression + LeapProgression
    newAriesGHA = getNumberFromString(ghaAries)
    cumProgression = getNumberFromString(cumulativeProgression)
    leapProgression = getNumberFromString(leapProgression)
    
    ghaAriesNew = newAriesGHA + cumProgression + leapProgression
    
    ghaAriesNew = getStringFormat(ghaAriesNew)
    
    
    #Part D
    #Calculate the Number of rotations since the beginning of the observation
    month = int(month)
    observationMonth = "01"
    observationMonth = int(observationMonth)
    monthDifference = month - observationMonth
    
    day = int(day)
    observationDay = "01"
    observationDay = int(observationDay)
    dayDifference = day - observationDay
    
    #Check to see if the year is a leap year
    #If it is, it adds a day to account for Feburary 29th
    #IF not in continues on
    checkYear = 2000
    while(checkYear <= 2100):
        if(year == checkYear):
            if(month > 2):
                dayDifference = dayDifference + 1
        checkYear = checkYear + 4
    
    
    
    
    hour = int(hour)
    minute = int(minute)
    seconds = int(seconds)
    
    hour = findSecondsInHour(hour)
    minute = findSecondsInMinute(minute)
    secondsDay = findSecondsInDay(dayDifference)
    secondsInMonth = findSecondsInMonth(monthDifference)
    
    numberOfSecondsBetween = hour + minute + secondsDay + secondsInMonth + seconds
    
    earthRotationPeriod = 86164.1
    fraction1 = (numberOfSecondsBetween / earthRotationPeriod * 360) % 360
    fraction1 = fraction1 * 60
    fraction1 = getStringFormat(fraction1)
    
    
    
    #Calculating the total
    num = getNumberFromString(fraction1) + getNumberFromString(ghaAriesNew)
    total = getStringFormat(num)
    
    #Find the GHA of the star
    numOfGHA = getNumberFromString(total)
    numOfStar = getNumberFromString(hourAngle)
    answer = numOfGHA + numOfStar
    GHAstar = getStringFormat(answer)
    
    longitude = GHAstar.split("d")[0]
    longitude = float(longitude)
    longitude = longitude - 360
    longitude = int(longitude)
    secondLong = GHAstar.split("d")[1]
    newGHA = str(longitude) + "d" + secondLong
    
    values['long'] = str(newGHA)
    values['lat'] = declination
    return values