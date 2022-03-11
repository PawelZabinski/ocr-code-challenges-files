from datetime import datetime, timedelta, date as dateToday
import os

# Events calendar

# Create a menu driven program that allows the user to add or delete events from a list of dates and timings, just like a calendar. The program should warn you if any of the events
# overlap when entering them.

RED = '\33[31m'
ORANGE = '\33[93m'
NORMAL = '\33[0m'

class ConsoleManager:
  def displayDate(date, end='\n'):
    print(date.strftime('%x %I:%M'), end=end)

  def displayEvent(event):
    formattedDuration = ', '.join([f'{event["duration"].get(i[0])} {i[1]}' for i in [('day', 'days'), ('hour', 'hrs'), ('minute', 'min')] if event['duration'].get(i[0], 0) > 0])
    
    # [ Event (15 min) ] 00/00/00 12:30 -> 00/00/00 12:45
    print(f'[ {event["text"]} ({formattedDuration}) ]', end=' ')
    
    ConsoleManager.displayDate(event['date'], end=' -> ')
    ConsoleManager.displayDate(CalendarManager.addDuration(event['date'], event['duration']))

  def displayMenu(options):
    for i, j in enumerate(options):
      print(f'[{i}] {j}')

    print()

    selection = input('Enter a number: ')

    if not selection.isdigit():
      ConsoleManager.error(f'Invalid input. "{selection}" is not a number.')
      ConsoleManager.clearScreen()
      return ConsoleManager.displayMenu(options)
      
    selection = int(selection)
    
    if 0 <= selection < len(options):
      return selection

    ConsoleManager.error(f'Invalid input. "{selection}" is not a valid selection.')
    ConsoleManager.clearScreen()
    return ConsoleManager.displayMenu(options)
    
  
  def warning(message):
    input(f'{ORANGE}WARNING - {message}{NORMAL}')

  def error(message):
    input(f'{RED}ERROR - {message}{NORMAL}')

  def clearScreen():
    os.system('clear')

  def enterToContinue():
    input()

class CalendarManager:
  events = []

  def addDuration(date, duration):
    return date + timedelta(days=duration.get('days', 0), hours=duration.get('hour', 0), minutes=duration.get('minute', 0))

  @classmethod
  def checkDuplicate(cls, text):
    for event in cls.events: 
      if event['text'] == text:
        return True 

    return False
  
  @classmethod
  def isOverlapping(cls, date, duration):
    
    for event in cls.events:
      lowerBandEventDate = event['date']
      eventDuration = event['duration']

      upperBandEventDate = cls.addDuration(lowerBandEventDate, eventDuration)
      upperBandDate = cls.addDuration(date, duration)
      
      # Check if the new event is in bounds of an existing event
      if lowerBandEventDate <= date <= upperBandEventDate or lowerBandEventDate <= upperBandDate <= upperBandEventDate or (lowerBandEventDate > date and upperBandDate > upperBandEventDate) :
        return True

    return False

  @classmethod
  def addEvent(cls, date, duration, text):
    if cls.checkDuplicate(text):
      ConsoleManager.error('The name of two seperate events may not be equal.')
      return;
    
    newDate = datetime(
      date['year'], 
      date['month'], 
      date['day'],
      date['hour'], 
      date['minute']
    )

    if cls.isOverlapping(newDate, duration):
      ConsoleManager.warning('The date entered is overlapping with another event.')

    cls.events.append({ 'date': newDate, 'duration': duration, 'text': text })
    cls.sortEvents()

    print(f'The event "{text}" has been created.')

  @classmethod
  def deleteEvent(cls, text):
    events = cls.events
    cls.events = [i for i in events if i['text'] != text]

    for i in events:
      if i['text'] == text:
        return True

    return False

  @classmethod
  def sortEvents(cls):
    cls.events.sort(key=lambda x: x.get('date', 0))

def mainMenu():
  options = ['Show Events', 'Modify Events', 'Feedback']

  selection = options[ConsoleManager.displayMenu(options)]

  ConsoleManager.clearScreen()

  if selection == 'Show Events':
    
    for event in CalendarManager.events:
      ConsoleManager.displayEvent(event)

    if len(CalendarManager.events) == 0:
      print('There are no events.')
      
  elif selection == 'Modify Events':
    
    modificationType = input('Do you want to Add or Delete an event? ').lower()

    if modificationType in ('ad', 'add'):
      eventName = input('Enter the event title: ')

      year = input('Enter the year of the event: (Optional) ')
      month = input('Enter the month of the event: (Optional) ')
      day = input('Enter the day of the event: (Optional) ')
      
      hour = input('Enter the hour of the event: (Required) ')
      minute = input('Enter the minute of the event: (Required) ')

      print()

      dayDuration = input('Enter the number of days the event is lasting? (Required) ')
      hourDuration = input('Enter the number of hours the event is lasting? (Required) ')
      minuteDuration = input('Enter the number of minutes the event is lasting? (Required) ')

      if year.isdigit():
        year = int(year)
      else:
        year = dateToday.today().year
        
      if month.isdigit():
        month = int(month)
      else:
        month = dateToday.today().month
      
      if day.isdigit():
        day = int(day)
      else:
        day = dateToday.today().day

      if hour.isdigit():
        hour = int(hour)
      else:
        hour = dateToday.today().hour

      if minute.isdigit():
        minute = int(minute)
      else:
        minute = dateToday.today().minute

      # Duration 
      if dayDuration.isdigit():
        dayDuration = int(dayDuration)
      else:
        dayDuration = 0

      if hourDuration.isdigit():
        hourDuration = int(hourDuration)
      else:
        hourDuration = 0

      if minuteDuration.isdigit():
        minuteDuration = int(minuteDuration)
      else:
        minuteDuration = 0

      CalendarManager.addEvent({ 
        'year': year,
        'month': month,
        'day': day,
        'hour': hour,
        'minute': minute
      }, {
        'day': dayDuration,
        'hour': hourDuration,
        'minute': minuteDuration
      }, eventName)
      
      
    elif modificationType in ('remove', 'delete', 'del'):
      eventName = input('Enter the event title: ')

      if CalendarManager.deleteEvent(eventName):
        print('Succesfully removed event.')
      else:
        ConsoleManager.warning('Event not found, no event has been removed')
    else:
      ConsoleManager.error(f'Invalid input. "{modificationType}" is not recognised\n')
    
  elif selection == 'Feedback':
    feedback()


def feedback():
  message = input('Enter Feedback: ')
  name = input('Enter your name: ')

  with open('feedback.txt', 'a') as f:
    f.write(f'"{message}" from {name}\n')

  print('\nYour feedback has been recorded.')

def main():

  while True:
    mainMenu()

    ConsoleManager.enterToContinue()
    ConsoleManager.clearScreen()
    
if __name__ == '__main__':
  main()