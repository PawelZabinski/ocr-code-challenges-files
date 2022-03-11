import json
import os

# Data Entry

# Create a program that retrieves the membership details for a Rock Climbing Club. The program should take a range of details and then repeat them back, with headings, for
# confirmation. Once confirmed, the program stores these details; else it clears them and allows a new input.

clearScreen = lambda: os.system('clear')

class Membership:
  def __init__(self, data={}):
    self.name = data.get('name', 'None')
    self.surname = data.get('surname', 'None')
    self.gender = data.get('gender', 'None')
    
    self.medicalInfo = data.get('medicalInfo', 'None')
    self.experience = data.get('experience', 'None')
    self.type = data.get('type', 'None')

  def __repr__(self):
    return f'''First Name - {self.name}
Surname: {self.surname}
Gender: {self.gender}
Medical Information: {self.medicalInfo}
Experience Level: {self.experience}
Membership Type: {self.type}
'''

  def dict(self):
    return {
      'name': self.name,
      'surname': self.surname,
      'gender': self.gender,
      'medicalInfo': self.medicalInfo,
      'experience': self.experience,
      'type': self.type
    }

  def getInputs(self):
    name = input('First Name: ')
    surname = input('Surname: ')
    gender = input('Gender: ')
    medicalInfo = input('Medical Information: ')
    experience = input('Experience Level [Begginer, Intermediate, Expert]: ')
    type = input('Membership Type [Basic, Premium]: ')

    self.name = name if name != '' else 'None'
    self.surname = surname if surname != '' else 'None'
    self.gender = gender if gender != '' else 'None'
    self.medicalInfo = medicalInfo if medicalInfo != '' else 'None'
    self.experience = experience if experience != '' else 'None'
    self.type = type if type != '' else 'None'

  def confirm(self):
    print(self)

    selection = input('Are these details correct? [Y/N] ').lower()

    if selection in ('y', 'ye', 'yes', 'yeah'):
      return True
    elif selection in ('n', 'no', 'nope'):
      return False

    return self.confirm()

  @classmethod
  def newMembership(cls):
    membership = cls()

    while True:
      membership.getInputs()
      clearScreen()

      if membership.confirm(): break
        
    DataManager.addMembership(membership)
      
        
class DataManager:
  memberships = []

  @classmethod
  def fetchMemberships(cls):
    with open('memberships.json', 'r') as f:
      cls.memberships = [Membership(i) for i in json.loads(f.read())]

  @classmethod 
  def addMembership(cls, membership):
    cls.memberships.append(membership)

    cls.storeMemberships()

  @classmethod
  def storeMemberships(cls):
    with open('memberships.json', 'w') as f:
      f.write(json.dumps([i.dict() for i in cls.memberships], indent=2))

def search():
  fullName = input('Enter full name of user: ')
  
  print()
  
  for membership in DataManager.memberships:
    if fullName == f'{membership.name} {membership.surname}':
      print(membership)
      break
  else:
    print('User not found.')

def main():
  DataManager.fetchMemberships()

  while True:
    clearScreen()
    
    for i, j in enumerate(['Search', 'New Membership', 'View Memberships']):
      print(f'[{i}] {j}')

    selection = int(input('\nEnter a number: '))

    clearScreen()
    
    if selection == 0:
      search()
    elif selection == 1:
      Membership.newMembership()
    elif selection == 2:
      for membership in DataManager.memberships:
        print(f'{membership.name} {membership.surname} - {membership.type} Membership')

    input()

if __name__ == '__main__':
  main()