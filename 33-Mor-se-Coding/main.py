import os

# Mor-se Coding

# Create a program that allows you to enter a string and encode it into Morse code, using ‘ . ‘ and ‘ - ‘ notation. Spaces between words should be replaced with the “|” (pipe) character.
# Use a normal space for gaps between each character.

MORSE_CODE = {
  'A': '.-', 'B': '-...', 'C': '-.-.',
  'D': '-..', 'E': '.', 'F': '..-.',
  'G': '--.', 'H': '....', 'I': '..',
  'J': '.---', 'K': '-.-', 'L': '.-..',
  'M': '--', 'N': '-.', 'O': '---',
  'P': '.--.', 'Q': '--.-', 'R': '.-.',
  'S': '...', 'T': '-', 'U': '..-',
  'V': '...-', 'W': '.--', 'X': '-..-',
  'Y': '-.--', 'Z': '--..',

  '0': '-----', '1': '.----', '2': '..---',
  '3': '...--', '4': '....-', '5': '.....',
  '6': '-....', '7': '--...', '8': '---..',
  '9': '----.',

  '.': '.-.-.-', ',': '--..--', ':': '---...',
  ';': '-.-.-.', '!': '..--.', '?': '..--..'
}

def clearScreen():
  os.system('clear')
  print('<--------[ MORSE CODE ]------->', end='\n'*2)

def encodeMorsecode(string):
  return ' | '.join([' '.join([MORSE_CODE.get(j, 'c') for j in i]) for i in string.upper().split(' ')])

def decodeMorsecode(string):
  morsecodeDict = { v: k for k, v in MORSE_CODE.items() }
  return ' '.join([''.join([morsecodeDict.get(j, j) for j in i.split(' ')]) for i in string.split('|')])

def main():
  clearScreen()

  for i, j in enumerate(['Alphanumeric to Morsecode', 'Morsecode to Alphanumeric', 'Exit']):
    print(f'[{i}] {j}')
  
  print()

  selection = int(input('Enter a number: '))
  assert 0 <= selection <= 2

  if selection == 2: return

  clearScreen()
  string = input('Enter a string: ')

  if selection == 0:
    print(encodeMorsecode(string))
  elif selection == 1:
    print(decodeMorsecode(string))
  
  input() 
  main()

if __name__ == '__main__':
  main()