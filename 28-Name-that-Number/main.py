import re

# There have been issues with enchant, so I am optionally importing it
try:
  import enchant
  DICTIONARY = enchant.Dict('en_GB')
except ImportError:
  enchant = None
  DICTIONARY = None

# Name that Number

# Telephone Keypads often have letters associated with each number. This means that 0141 117 2556 could be stored as 0141-CAT-DOOR. Create a program that can convert
# a phone number with “letters” into one that only contains digits.

class PhoneNumberManager:
  @classmethod
  def decrypt(cls, phoneNumber):
    newPhoneNumber = [str(cls.lettersLookupTable().get(i, i)) for i in phoneNumber]
    return ''.join([i for i in newPhoneNumber if i.isdigit()])
  
  @classmethod
  def validate(cls, phoneNumber):
    
    for i in phoneNumber:
      if (not i.isdigit()) and i not in cls.lettersLookupTable() and i not in ('-', ' '):
        return False

    if DICTIONARY:
      words = re.findall(r'[a-zA-Z]+', phoneNumber)

      return all(DICTIONARY.check(word) for word in words)
    
    raise ImportError
  
  def lettersLookupTable():
    return {
      'A': 2, 'B': 2, 'C': 2,
      'D': 3, 'E': 3, 'F': 3,
      'G': 4, 'H': 4, 'I': 4,
      'J': 5, 'K': 5, 'L': 5,
      'M': 6, 'N': 6, 'O': 6,
      'P': 7, 'Q': 7, 'R': 7, 
      'S': 7, 'T': 8, 'U': 8, 
      'V': 8, 'W': 9, 'X': 9,
      'Y': 9, 'Z': 9
    }

def main():
  phoneNumber = input('Enter phone number: ').upper()
  
  try:
    if not PhoneNumberManager.validate(phoneNumber):
      return print('Invalid phone number. Ensure you use only alphanumeric characters and valid English words')

  except ImportError:
    print('Dictionary failed to load, word checking is disabled.')

  newPhoneNumber = PhoneNumberManager.decrypt(phoneNumber)

  print(newPhoneNumber)

if __name__ == '__main__':
  main()