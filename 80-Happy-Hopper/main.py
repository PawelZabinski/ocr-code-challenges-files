# Happy Hopper

# A sequence of n > 0 integers is called a happy hopper if the absolute values of the differences between successive elements take on all possible values 1 through n - 1. E.g 1 4 2 3
# is a happy hopper because the absolute differences are 3, 2, and 1, respectively. The definition implies that any sequence of a single integer is a happy hopper. Write a program to
# determine whether each of a number of sequences is a happy hopper.

def isHappyHopper(sequence):
  differences = [abs(sequence[i] - sequence[i + 1]) for i in range(len(sequence) - 1)]
  
  for i in range(1, len(sequence)):
    if i not in differences: return False
  
  return True

def main():
  print('Please enter your sequence of numbers by adding a ", " between each subsequent integer')
  sequence = [int(i) for i in input('Enter a sequence of integers: ').split(', ')]

  if isHappyHopper(sequence):
    print('Yes, the sequence is a happy hopper.')
  else:
    print('No, the sequence is not a happy hopper.')

if __name__ == '__main__':
  main()