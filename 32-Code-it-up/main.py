# Code it up

# Create a program that adds 25 to the value of each character of a string that a user enters. This new string should be saved and output.

def addASCIIValue(string, value):
  return ''.join([chr(ord(i)+value) for i in string])

def main():

  string = input('Enter a string: ')
  value = int(input('Enter value to encrypt string: '))
  encryptionType = input('Do you want to Encode or Decode the string? [E/D] ').upper()
  
  newString = addASCIIValue(string, value if encryptionType == 'E' else -value )

  print(f'New string: "{newString}"')

if __name__ == '__main__':
  main()