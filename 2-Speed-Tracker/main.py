from math import ceil
import json
import re

# Speed Tracker

# Create a program that takes a time for a car going past a speed camera, the time going past the next one and the distance between them to calculate the average speed for
# the car in mph.

def calculateHours(time):
  regexPattern = '^([0-9]{1,2}):([0-9]{2})$'
  assert re.match(regexPattern, time)
  
  regexMatch = re.search(regexPattern, time)
  hours = int(regexMatch.group(1)) + int(regexMatch.group(2)) / 60

  return hours

def calculateMPH(distance, time1, time2):
  timeOne = calculateHours(time1)
  timeTwo = calculateHours(time2)

  time = timeTwo - timeOne
  assert time > 0

  speed = distance / time
  return speed

def isValidNumberPlate(numberPlate):
  regexPattern = '^[a-zA-Z]{2}[0-9]{2} ?[a-zA-Z]{3}$'
  return re.match(regexPattern, numberPlate) is not None

# Program to take input and display the speed and validate number plate
try:
  numberPlate = input('Number plate of the vehicle: ')

  if isValidNumberPlate(numberPlate):
    print('Valid Number Plate')
  else:
    print('Invalid Number Plate Entered')
  
  
  timeOne = input('Time for a vehicle going past a speed camera: ')
  timeTwo = input('Time for a vehicle going past the next speed camera: ')
  
  distance = float(input('Distance of the two speed cameras (in miles): '))

  speed = calculateMPH(distance, timeOne, timeTwo)

  print(f'The speed is {speed} mph')
except AssertionError:
  print('Invalid Input, Please provide valid input in the correct format.')
except:
  print('An error occured in the program...It\'s probably your fault though...')


# Program to read the contents of an external file and determine which vehicle went over the speed limit and validates the number plate
'''
vehicles = []

distance = 5 # in miles

with open('vehicles.json', 'r') as f:
  jsonData = f.read()
  vehicles = json.loads(jsonData)

for vehicle in vehicles:
  numberPlate = vehicle['numberPlate']
  
  if isValidNumberPlate(vehicle['numberPlate']):
    print(f'Vehicle \'{numberPlate}\' has a valid number plate')
  else:
    print(f'Vehicle \'{numberPlate}\' has an invalid number plate')

  speed = calculateMPH(distance, vehicle['firstSpeedCamera'], vehicle['secondSpeedCamera'])

  if speed > 70:
    print(f'Vehicle {numberPlate} has broken the speed limit at {ceil(speed)} mph')
  else:
    print(f'Vehicle {numberPlate} has been obedient and did not break the speed limit.')

  print()
'''