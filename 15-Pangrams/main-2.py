# Pangrams

# ”The quick brown fox jumps over the lazy dog”; note how all 26 English-language letters are used in the sentence.
# Your goal is to implement a program that takes a series of strings (one per line) and prints either True (the given string is a pangram), or False if it is not.

ALPHABET = list('abcdefghijklmnopqrstuvwxyz')

def isPangram(text):
  character_count = dict()

  for char in text:
    if character_count.get(char, 0) > 0:
      character_count[char] += 1
    else:
      character_count[char] = 1

  for char in ALPHABET:
    if character_count.get(char, 0) == 0:
      return False

  return True

text = input('Enter a phrase: ')
print(isPangram(text))