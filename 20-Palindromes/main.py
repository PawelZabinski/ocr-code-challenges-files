# Palindromes
# Write a program that checks if a string entered by the user is a palindrome. A palindrome is a word that reads the same forwards as backwards like “racecar”

def isPalindrome(string):
  return string == string[::-1]

string = input('Enter a string: ').lower()

if isPalindrome(string):
  print('The string is a palindrome.')
else:
  print('The string is not a palindrome.')