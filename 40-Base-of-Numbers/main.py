from utils import intToBase

# Base of Numbers

# Create a program that converts a denary number into its hexadecimal equivalent.

def main():
  value = int(input('Enter denary number: '))
  base = int(input('Enter the base of the number system: '))

  newValue = intToBase(value, base)
  print(f'New value: {newValue}')

if __name__ == '__main__':
  main()