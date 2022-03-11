import itertools
import os

# Prime Factorisation

# Have the user enter a number and find all Prime Factors (if there are any) and display them.

def newFrame():
  os.system('clear')
  print(f'<{"-"*7}[ PRIME FACTORISATION ]{"-"*7}>', end='\n'*2)

def isPrime(num):
  if num <= 1:
    return False
  
  for i in range(2, num//2+1):
    if num % i == 0:
      return False
  
  return True

def primes():
  for i in itertools.count(1):
    if isPrime(i):
      yield i

def primeFactors(num):
  if num == 1: return [1]
  elif num <= 0: raise ValueError('Value may not be negative as it will lead to infinite solutions')

  for i in primes():
    if num % i == 0:
      return [x for x in [i] + primeFactors(num//i) if x != 1]

def main():
  newFrame()

  for i, j in enumerate(['Prime Factors', 'All Primes', 'Exit']):
    print(f'[{i}] {j}')

  selection = int(input('\nEnter a number: '))

  newFrame()

  if selection == 0:
    num = int(input('Enter a number: '))
    factors = primeFactors(num)

    print(f'Prime Factors: {factors}')
  elif selection == 1:
    for i in primes():
      if input().lower() in ('exit', ':q'):
        break

      print(f'\033[1A{i}')
  elif selection == 2:
    return

  input('\nPress Enter to Return: ')
  main()

if __name__ == '__main__':
  main()