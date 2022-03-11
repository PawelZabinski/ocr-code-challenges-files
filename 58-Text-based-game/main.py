from enum import Enum
import re

class Colour(Enum):
  System = '\x1b[0;30;44m'
  Normal = '\33[0m'
  Important = '\x1b[0;30;41m'

# Functions class contains numerous static methods which endeavour to ecapsulate business logic from main code 
# Examples include taking input from user, displaying a message etc
class Functions:
  cmd = {
    ':help': lambda: print('''Commands:
* To move to a room, type 'go to {room}'
                           
* To search the current room, type 'search'
* To leave the current room, type 'leave'
                       
* To view inventory, type 'inventory'

Special commands:
* To stop game, type ':exit'
* To get help on commands, type ':help' '''),
':exit': exit
  }

  stdCMD = {
    'move': r'^go to (.+?)( lab)?$',
    'search': r'^search$',
    'leave': r'^leave$',
    'inventory': r'^inventory$'
  }

  def showHeader():
    print(f'<{"-"*7}[ Computer Scientist ]{"-"*7}>', end='\n'*2)
  
  def showMessage(msg):
    print(Colour.System.value, f'SYSTEM: {msg}', Colour.Normal.value)
  
  def showAlert(msg):
    print(Colour.Important.value, msg, Colour.Normal.value)

  def showInfo(msg):
    print(Colour.Important.value, msg, Colour.Normal.value)

  def spacer():
    print()

  @classmethod
  def prompt(cls, msg=''):
    print(msg)
    
    foo = input('> ').lower()

    cls.spacer()

    if foo in cls.cmd:
      cls.command(foo)
      return None

    # For each pattern, check if the input matches the pattern and then act accordingly
    for action, regex in cls.stdCMD.items():
      if (m := re.match(regex, foo)):
        return (action, m.groups())

    return None

  @classmethod
  def next(cls):
    cls.spacer()
    input('Enter To Continue > ')
    cls.spacer()

  @classmethod
  def command(cls, msg=None):
    return cls.cmd[msg or cls.prompt()]()

#
# Player
#
    
class Player:
  def __init__(self, name):
    self.name = name
    self.inventory = []
    self.roomHistory = []

  def pickUp(self, *items):
    for item in items:
      # Prevent duplicates
      if item not in self.inventory:
        self.inventory.append(item)

    # Check if the player owns the unmarked key and metal safe...
    for item in items:
      # If the player has just picked up the item (prevent duplication)
      if item in ('Unmarked Key', 'Metal safe') and 'Unmarked Key' in self.inventory and 'Metal safe' in self.inventory:
        Functions.showMessage('''You've unlocked the metal safe with the unmarked Key. Inside the safe you found another key...
This key is also unmarked, yet before you loose all hope, you remember the locked key box in the reception...''')

        self.pickUp('Unmarked Key 2')
        
  def showInventory(self):
    if len(self.inventory):
      print('Inventory:')
  
      for i in self.inventory:
        print(f'* {i}')

      return

    print('Your inventory is empty.')

  def enter(self, room):
    self.roomHistory.append(room)
    room.start(self)

  def previousRoom(self):
    length = len(self.roomHistory)

    if length >= 2:
      return self.roomHistory[-2]
    elif length == 1:
      return self.roomHistory[-1]

    raise ValueError('Rooms history should not be empty.')
    
#
# Rooms
#

class Room:

  def __init__(self, name, function, requirements):
    self.name = name
    self.function = function
    self.requirements = requirements

  def start(self, protagonist):
    Functions.showInfo(f"You've entered the {self.name}")
    self.function(protagonist, self, isExploring=self not in protagonist.roomHistory[:-1])

# Rooms include Reception, Systems architecture lecture, Memory and storage lecture, Networking lecture, Library (Containing all books required)

def reception(protagonist, room, isExploring=True):
  
  if isExploring:
    Functions.showMessage('''You have managed to brute force your way into the reception through a broken window.
On the counter lies a locked key box, and a large book; there is a corridor to the right containing numerous computer science labs.
All windows and glass have been boarded up, locked away with a bullet-proof padlock
                          
You've scoured through the book - holding information about the department.

The following information about the department was given:
Janitor's Closet: OPEN
Systems architecture lab: Key 2615
Library: Key 6931, Key 2186
                              
To access the main library, containing all the resources you need, you require two seperate keys to bypass the double security lock.
It is your priority to open the library and take all the resources you need, then get out of this campus without anyone noticing.''')

  # Iterate over inputs
  while True:
    # Check if the player has returned to reception after finding the key to the key box
    if 'Unmarked Key 2' in protagonist.inventory: 
      Functions.showMessage('''You've returned to reception and tried the second unmarked key against the key box.
Unsuprisingly, the key worked and you've managed to open the mysterious key box.

Inside it, you found another key, named Key 2186. However, there was also a piece of paper with encoded morse code.

- .-- --- / - .... .-. . . / ..-. .. ...- . / . .. --. .... - ''')

      protagonist.pickUp('Key 2186')
    
    if (action := Functions.prompt()):
      if action[0] == 'search': 
        Functions.showMessage('''After searching for over an hour, you looked in every cupboard, every book, in every crack of the room. Everywhere.

You've managed to find a key labeled "Key 2615" in a secret compartment under the counter.''')

        protagonist.pickUp('Key 2615')
        
      elif action[0] == 'inventory':
        protagonist.showInventory()
        
      elif action[0] == 'move':
        newRoom = action[1][0]

        # In reception, you are using the allRooms list as any room can be reached from here, but in other rooms this will not be possible
        if (room := allRooms.get(newRoom, None)):
          isRequirementsMet = all(i in protagonist.inventory for i in room.requirements)

          if isRequirementsMet:
            protagonist.enter(room)
            Functions.showInfo("You returned to reception")
          else:
            Functions.showAlert("The door is locked and you don't have a sufficient key.")
        else:
          Functions.showAlert(f'Room "{newRoom}" does not exist.')
          
      elif action[0] == 'leave':
        Functions.showAlert("You cannot leave the reception, you must gain knowledge first.") 

def systemsArchitecture(protagonist, room, isExploring=True):

  if isExploring:
    Functions.showMessage('''You've managed to gain access to the Systems Architecture lab;
  There were a plethora of aged motherboards and untouched computer units in the room.''')
  
    Functions.next()
  
    Functions.showMessage('''You've checked the radiation metre and it was overflowing, you must hurry as the gamma radiation present in this chamber is damaging to your body cells.
  
You've picked up some of the motherboards and other materials, to craft the technology required to save civilisation.
Now you mustn't stop there, you need access to the library in order to obtain the guides needed to put together this machinery''')
  
    protagonist.pickUp('Motherboards', 'RAM', 'CPU', 'SSD', 'Tool kit')

  # Iterate over inputs
  while True:
    if (action := Functions.prompt()):
      if action[0] == 'search': 
        Functions.showMessage('''After examining the room, you've found a medium-sized metal alloy safe.
After many unsuccefull atempts on opening the safe, you've concluded that another key is required.''')

        protagonist.pickUp('Metal safe')
        
      elif action[0] == 'inventory':
        protagonist.showInventory()
        
      elif action[0] == 'move':
        if action[1][0] == 'reception':
          return
          
        Functions.showAlert(f'From the {room.name}, you can only go back to the reception.')
      elif action[0] == 'leave':
        return

def janitorsCloset(protagonist, room, isExploring=True):
  if isExploring:
    Functions.showMessage('''You've opened the janitor's closet door and found many redundant cleaning supplies that you don't need.
You take a brief look around and don't find anything worth your time.''')

    # Iterate over inputs
  while True:
    if (action := Functions.prompt()):
      if action[0] == 'search': 
        Functions.showMessage('''The innocence of the room drove you crazy and you convinced yourself that there was something worthwhile here.
You've opened all of the cleaning products, including the bleach, sprays, mops etc.''')

        Functions.next()

        Functions.showMessage("Thankfully, your instincts were right, you've found two keys: Key 6931 and an unmarked key")

        protagonist.pickUp('Key 6931', 'Unmarked Key')
        
      elif action[0] == 'inventory':
        protagonist.showInventory()
        
      elif action[0] == 'move':
        if action[1][0] == 'reception':
          return
          
        Functions.showAlert(f'From the {room.name}, you can only go back to the reception.')
      elif action[0] == 'leave':
        return

def library(protagonist, room, isExploring=True):
  if isExploring:
    Functions.showMessage("You've opened the front door, yet the library is obstructed by another gate, this time with a passcode.")

    # Keep on taking input until user gets passcode correct
    while True:
      attempt = input('Enter passcode > ')

      if attempt == '2358':
        Functions.showMessage('Correct. You\'ve managed to open the gate and get access to the library!')
        break

    Functions.next()

    Functions.showMessage('''In the library, there are many books and research papers that will be necessary in your endeavour against this deadly virus.
You picked up as many texts as you could fit in your carry bag and rushed out of the campus, removing any trace of your break-in.

You are now ready to save the world.''')

    Functions.showAlert(f"You've completed the game! Well done {protagonist.name}; also I would like to apologise for the cheesy storyline, it's the best I could come up with ;)")
    exit()

allRooms = {
  'reception': Room('Reception', reception, []),
  'systems architecture': Room('Systems Architecture Lab', systemsArchitecture, ['Key 2615']),
  "janitor's closet": Room("Janitor's closet", janitorsCloset, []),
  'library': Room('Library', library, ['Key 6931', 'Key 2186'])
}

#
# Main Function
#

def main():
  Functions.showHeader()

  print('What is your name?')
  name = input('> ')
  
  protagonist = Player(name)

  Functions.spacer()
  Functions.showAlert('Type :help for guidance on entering commands.')
  Functions.spacer()
  
  # Introduction
  Functions.showMessage(
  '''University of Cambridge

Due to a global viral outbreak, the Great University of Cambridge was deserted.
Many of the greatest lecturers have fallen victim to the virus and to salvage the fate of civilisation, new technology must be invented to combat the spread of the virus.

You do not possess any computer science knowledge, the internet was shut down and all libraries have ceased to exist.
In order to continue in your endeavour you decided to break into the campus and get access to the computer science books, and computer hardware units.''')

  Functions.next()

  protagonist.enter(allRooms['reception'])

if __name__ == '__main__':
  main()