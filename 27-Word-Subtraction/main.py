# Word Subtraction

# Create a program that takes two strings/words. Then then converts this to an ASCII value and subtracts the values from each other.

def subtractASCII(wordOne, wordTwo):
  wordOneASCII = [ord(i) for i in wordOne]
  wordTwoASCII = [ord(i) for i in wordTwo]

  for i, j in enumerate(wordTwoASCII):
    if len(wordOneASCII) > i:
      wordOneASCII[i] -= j
  
  return wordOneASCII

def letterSubtraction(wordOne, wordTwo):
  newWordOne = ''.join([i for i in wordOne if i not in wordTwo])
  newWordTwo = ''.join([i for i in wordTwo if i not in wordOne])

  return (newWordOne, newWordTwo)

def main():
  wordOne = input('First word: ')
  wordTwo = input('Second word: ')

  result = letterSubtraction(wordOne, wordTwo)
  print(result)

if __name__ == '__main__':
  main()