# Forwards and Backwards

# Create a program that is able to detect if an input is the same as the reverse of the same input – i.e. a Palindrome

def isPalindrome(string):
  return string == string[::-1]

def main():
  string = input('Enter a string: ')

  if isPalindrome(string):
    print('The string and the reversed string are the same.')
  else:
    print('The string and the reversed string are NOT the same.')

if __name__ == '__main__':
  main()