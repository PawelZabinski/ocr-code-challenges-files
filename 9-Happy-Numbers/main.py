import functools
import itertools

ITERATION_LIMIT = 10_000

# Happy Numbers

# A happy number is defined by the following process:
# Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops
# endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers, while those that do not end in 1 are unhappy numbers.
# Display an example of your output here. Find the first eight happy numbers.

def evaluate_positive_integer(integer):
  return functools.reduce(lambda x, y: x + y, [int(i) ** 2 for i in str(integer)])

def main():
  for i in itertools.count():
    new_integer = i
    
    iteration_count = 0 
    while not new_integer == 1:
      iteration_count += 1
      
      if iteration_count > ITERATION_LIMIT:
        break
      
      new_integer = evaluate_positive_integer(new_integer)
    else:
      print(f'{i} is a happy number!')
    
if __name__ == '__main__':
  main()