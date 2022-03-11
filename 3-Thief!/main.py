# Thief!

# A thief has managed to find out the four digits for an online PIN code, but doesn’t know the correct sequence needed to hack into the account.
# Design and write a program that displays all the possible combinations for any four numerical digits entered by the user. The program should avoid displaying the same
# combination more than once.

def permutations(elements):
  if len(elements) <= 1:
    yield elements
  else:
    for perm in permutations(elements[1:]):
      for i in range(len(elements)):
        yield perm[:i] + elements[0:1] + perm[i:]

pin = input('Enter the integers in the pin: ')
numbers = list(pin)

allPermutations = [''.join(i) for i in permutations(numbers)]
allPermutations = list(dict.fromkeys(allPermutations))

print('\nAll the possible permutations:')

for permutation in allPermutations:
  print(permutation)