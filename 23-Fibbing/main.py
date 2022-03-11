import itertools

# Fibbing

# Create a program that will calculate the Fibonacci Sequence to 10 places.

def fibonacci():
  a, b = 0, 1

  while True:
    yield a
    a, b = b, a + b

def main():
  fibonacciNumsCount = int(input('Number of fibonacci numbers: '))
  isReverse = input('Reverse the order? [Y/N] ').lower()

  fibonacciNums = [i for i in itertools.islice(fibonacci(), fibonacciNumsCount)]
  strFibonacciNums = [str(i) for i in fibonacciNums]

  print()

  if isReverse in ('y', 'ye', 'yes', 'yeah'):
    print(', '.join(strFibonacciNums[::-1]))
  elif isReverse in ('n', 'no', 'nope', 'nah'):
    print(', '.join(strFibonacciNums))
  else:
    raise ValueError(f'Invalid input: "{isReverse}" is not recognised')
  
  total = sum(fibonacciNums)

  print(f'\nThe total is {total}')

if __name__ == '__main__':
  main()