import itertools

# Goldbach

# Goldbach’s conjecture says that every positive even number greater than 2 is the sum of two prime numbers. Example: 28 = 5 + 23. It is one of the most famous facts in number
# theory that has not been proved to be correct in the general case. It has been numerically confirmed up to very large.
# Write a predicate to find the two prime numbers that sum up to a given even integer.

def isPrime(num):
  if num <= 1: 
    return False

  for i in range(2, num // 2 + 1):
    if num % i == 0:
      return False

  return True

def primes():
  for i in itertools.count(2):
    if isPrime(i): yield i

def goldbach(num):
  for i in primes():
    if isPrime(num - i):
      return [i, num - i]

def main():
  evenInteger = int(input('Enter positive even integer > '))
  assert evenInteger > 0 and evenInteger % 2 == 0
  
  nums = goldbach(evenInteger)

  # For visual purposes only
  nums.sort(reverse=True)

  print(f'The two primes are {nums[0]} and {nums[1]}')

if __name__ == '__main__':
  main()