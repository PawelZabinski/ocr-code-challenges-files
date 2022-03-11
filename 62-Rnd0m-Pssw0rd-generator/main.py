import random

# R@nd0m P@ssw0rd generator

# Have the programme create random strong passwords mixing upper and lower case, symbols and numbers.

letters = 'abcdefghijklmnopqrstuvwxyz'
numbers = '0123456789'
symbols = '''~`!@#$%^&*()_-+={[}]|\:;"'<,>.?/'''

def createPassword(length=16):
  availableChars = letters + letters.upper() + numbers + symbols
  chars = [random.choice(availableChars) for _ in range(length)]

  return ''.join(chars)

def main():
  length = int(input('Enter length of password > '))
  password = createPassword(length)

  print(f'Your password is "{password}"')

  with open('entries.txt', 'a') as file:
    file.write(password + '\n')

if __name__ == '__main__':
  main()