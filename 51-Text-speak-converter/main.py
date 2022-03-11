import json
import re
import os

class Dictionary:
  conversionLookUp = []

  @classmethod
  def load(cls):
    with open('dictionary.json', 'r') as f:
      cls.conversionLookUp = json.load(f)

  @classmethod
  def save(cls):
    with open('dictionary.json', 'w') as f:
      f.write(json.dumps(cls.conversionLookUp, indent=2))
  
  @classmethod
  def addTerm(cls, term, meaning):
    cls.conversionLookUp[term] = meaning
    cls.save()

  @classmethod
  def convert(cls, text):
    words = [cls.conversionLookUp.get(i, i) for i in re.split('|'.join(map(re.escape, [' ', ',', '.'])), text)]

    return ' '.join(words)

def main():
  os.system('clear')
  print(f'<{"-"*7}[ TEXT-SPEAK CONVERTER ]{"-"*7}>', end='\n' * 2)
  Dictionary.load()

  text: str

  with open('text.txt', 'r') as f:
    text = f.read()
  
  newText = Dictionary.convert(text)
  print(newText)

  if input('\nDo you want to add a new term to the dictionary? ') in ('y', 'ye', 'yes', 'yeah'):
    term = input('Enter your term: ')
    meaning = input(f'Enter meaning for "{term}": ')

    Dictionary.addTerm(term, meaning)
    print('\nSuccesfully added term')
  
  # Ask if user wants to restart program
  if input('\nDo you want to run the program again? ') in ('y', 'ye', 'yes', 'yeah'):
    main()

if __name__ == '__main__':
  main()