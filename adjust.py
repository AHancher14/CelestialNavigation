"""
Created on 2/20/2019
@author: Alan Hancher
"""
from optparse import Values
import math
from math import sqrt, radians
from pip._internal.cli.cmdoptions import pre
from nav.sandbox.sandbox import newVal, height, newAltitude


# This chain of comments is me just listing out the requirements that way, I can keep track of what I'm doing as well as making sure I am
# understanding the project.
# The input for adjust is a dictionary of different values, passed in as Strings
# The first value in the dictionary is the observation value.
# Observation has the following format of xdy.y where
#    the first x value is degree portion of the altitude
#        It is a positive integer and is greater or equal to 0 and less than 90
#    the second value D is used to separate the degrees from the minutes
#    The third value is the y.y, this is Minute portion of the altitude 
#        this is a floating point value
#        It is greater than or equal to 0 and less than 60.0
#
# The second value is height
#    It is greater than 0
#    It also defaults to 0 if it was not provided
#
# The Third value is temperature
#    It is GE -20 and Less than 120
#    Defaults to 72 if missing
#
# The Fourth value is the Pressure
#    It is GE 100 and LT 1100
#    Defaults to 1010 if a value is not present
#
# The Last Value in the dictionary is Horizon
#    It is a string value that is either natural or Artificial
#    Case Sensitive
#    Defaults to Natural if Missing 

#Function for converting farenheight into celsius
def convert_to_celcius(temperature):
    celcius = (float(temperature - 32) * 5) / 9
    return celcius

def adjust(values):
    #We know that values is the dictionary
    #Our next step is to Parse through the dictionary, getting the values that we want.
    
    
    #Checking to see if there is an altitude value in the original dict
    if 'altitude' in values:
        values['error'] = "Invalid Observation value"
        return values
    
    #checking the observation value
    observation = 0
    if 'Observation' in values:
        observation = values['Observation']
    else:
        values['error'] = "Invalid Observation value"
        return values
    
    if not "d" in observation:
        values['error'] = "Invalid Observation value"
        return values
    degree = observation.split("d")[0]
    minute = observation.split("d")[1]
    
    if not "." in minute:
        values['error'] = "Invalid Observation value"
        return values
    
    #Checking the degree in the observation value
    try:
        degree = int(degree)
    except:
        values['error'] = "Invalid Observation value"
        return values
    
    if(degree < 1 or degree >= 90):
        values['error'] = "Invalid Observation value"
        return values
    
    try:
        minute = float(minute)
    except:
        values['error'] = "Invalid Observation value"
        return values
    
    if(minute < 0.0 or minute >= 60.0):
        values['error'] = "Invalid Observation value"
        return values
    
    observation = degree + minute / 60
    
    #Setting height to 0
    # then Checking to see if there is a height value
    height = 0
    if 'height' in values:
        height = values['height']
    try:
        height = float(height)
    except:
        values['error'] = "Invalid Height value"
        return values
    if(height < 0):
        values['error'] = "Invalid Height value"
        return values
    
    #Set pressure value to 1010
    #Testing the conditions that were assigned to pressure
    pressure = 1010
    if 'pressure'  in values:
        pressure = values['pressure']
    try:
        pressure = int(pressure)
    except:
        values['error'] = "Invalid Pressure value"
        return values
    if(pressure < 100 or pressure > 1100):
        values['error'] = "Invalid Pressure value"
        return values
    
    
    #Checks to see if there is a value for temperature
    #If not, sets temperature to 72
    temperature = 72
    if 'temperature' in values:
        temperature = values['temperature']
    try:
        temperature = int(temperature)
    except:
        values['error'] = "Invalid Temperature value"
        return values
    
    if (temperature < -20 or temperature > 120):
        values['error'] = "Invalid Temperature value"
        return values
    #Checks the value for Horizon
    #If there isn't a value, sets horizon equal to Natural
    horizon = "natural"
    if 'horizon'in values:
        horizon = values['horizon']
    if not(horizon in("artificial", "natural")):
        values['error'] = "Invalid Horizon value"
        return values
    
    #Below is the actual equation
    #Step 1, if the horizon is natural, then do the equation
    #if not, dip is equal to 0
    if(horizon == 'natural'):
        dip = 0.0
        dip = (-0.97 * sqrt(height)) / 60
    else:
        dip = 0
    #Step 2
    refraction = (-0.00452 * pressure) / (273 + convert_to_celcius(temperature)) / math.tan(radians(observation))
    
    #step 3
    altitude = observation + dip + refraction
    
    #Step 4
    #Round the nearest altitude to 0.1
    newDegree = (int(altitude))
    newMinute = round((altitude - newDegree)*60,1)
    
    #step 5
    #adding it to the original list
    altitude = (str(newDegree) + "d" + str(newMinute))
    values['Altitude'] = altitude
    
    return values