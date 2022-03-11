# Reverse it

# Have the programme allow a user to enter some text and then the programme will reverse it and print it back to the screen.

VOWELS = ['a', 'e', 'i', 'o', 'u']
CONSONANTS = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

def reverse(string):
  return string[::-1]

def countChars(string, chars):
  return len([i for i in string if i.lower() in chars])

def main():
  string = input('Enter some text: ')
  newString = reverse(string)

  print('\nOUTPUT:')
  print(f' - The reversed string is "{newString}"')
  print(f' - The vowel count is {countChars(string, VOWELS)}')
  print(f' - The consonants count is {countChars(string, CONSONANTS)}')
  print(f' - The string is{"" if string == newString else " not"} a palindrome')

if __name__ == '__main__':
  main()