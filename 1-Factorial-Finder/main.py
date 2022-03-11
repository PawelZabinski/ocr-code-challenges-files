# Loops implementation
def factorialLoops(number):
  assert number >= 0
  
  product = 1
  
  for i in range(1, number + 1):
    product *= i
  
  return product

# Recursion implementation
def factorialRecursive(number):
  assert number >= 0

  if number <= 1: return 1
  return number * factorialRecursive(number - 1)

def main():
  number = int(input('Enter a number: '))
  result = factorialLoops(number)

  print(f'The factorial of {number} is {result}')

if __name__ == '__main__':
  main()