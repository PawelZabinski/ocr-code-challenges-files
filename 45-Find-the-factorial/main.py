import itertools

# Find the factorial

# The Factorial of a positive integer, n, is defined as the product of the sequence n, n-1, n-2, ...1 and the factorial of zero, 0, is defined as being 1. Solve this using both loops
# and recursion.

#
#
# DISCLAIMER - This is *identical* to Challenge 1 so I am guessing I'm supposed to do the inverse, find the input, given the output
#
#

def findFactorial(output):
  # Begin with the running product at 1 as multiplying by 1 is idempotent
  product = 1

  # Iterate from 1 to infinity (until the output is found or invalidated)
  for i in itertools.count(1):
    product *= i

    if product == output:
      return i
    elif product > output:
      raise ValueError('No valid solution')

def findFactorialRecursive(output, val=1, i=1):
  # Handle base cases and errors
  if output == 1: return 1
  elif output < 1: raise ValueError('Invalid input')
  elif val > output: raise ValueError('No valid solution.')

  # Check if the current factorial value is equal to the desired output
  if output == val: return i

  return findFactorial(output, val * (i + 1), i + 1)

def main():
  try:
    number = int(input('Enter the result of the factorial operation: '))
    factorialInput = findFactorial(number)

    print(f'The factorial input is {factorialInput}')
  except ValueError as err:
    print(err)

if __name__ == '__main__':
  main()