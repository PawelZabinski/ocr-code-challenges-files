import itertools

# String permutation
# Given two strings x and y, print the longest string a of letters such that there is a permutation of a that is a subsequence of x and there is a permutation of a that is a subsequence of y.

def permutationSubsequence(x, y):
  z = min(x, y, key=lambda i: len(i))
  allCombinations = sorted({ j for i in range(1, len(z) + 1) for j in itertools.combinations(z, i) }, key=lambda i: len(i), reverse=True)
  
  for combination in allCombinations:
    # Check if there is a permutation of it that matches the other string
    other = x if z == y else y

    for permutation in itertools.permutations(combination):
      if (a := ''.join(permutation)) in other:
        return a

  return ''

def main():
  x = input('Enter first string > ')
  y = input('Enter second string > ')

  a = permutationSubsequence(x, y)

  print(a)

if __name__ == '__main__':
  main()