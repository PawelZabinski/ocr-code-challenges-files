import os

# Fizz Buzz

# Create a program that replicates the famous game Fizz Buzz. The program will take an input, e.g. 20, and then print out the list of Fizz Buzz up to and including that number, where:
# • Any multiple of 3 is replaced by the word ‘Fizz’
# • Any multiple of 5 is replaced by the word ‘Buzz’
# • Any multiple of both 3 and 5 is replaced by the word ‘FizzBuzz’

def newFrame():
  os.system('clear')
  print(f'<{"-"*7}[ FIZZ BUZZ ]{"-"*7}>', end='\n'*2)

def isPrime(num):
  if num == 1:
    return False 

  for i in range(2, num//2+1):
    if num % i == 0:
      return False
  
  return True

def fizzBuzzNum(num, baseA, baseB):
  if isPrime(num):
    return 'OOPS!'
  elif num % (baseA*baseB) == 0:
    return 'FizzBuzz'
  elif num % baseA == 0:
    return 'Fizz'
  elif num % baseB == 0:
    return 'Buzz'
  
  return str(num)

def main():
  newFrame()

  numCount = int(input('FizzBuzz length:  '))
  baseA = int(input('Base Number A: '))
  baseB = int(input('Base Number B: '))

  newFrame()

  fizzBuzz = [fizzBuzzNum(i, baseA, baseB) for i in range(1, numCount+1)]

  for i in fizzBuzz:
    print(i)

if __name__ == '__main__':
  main()