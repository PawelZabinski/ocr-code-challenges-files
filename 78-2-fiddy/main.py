import itertools

# 2 fiddy

# It is possible to make £2.50 in the following way:
# 1×£1 + 2×50p + 2×20p + 1×5p + 1×2p + 3×1p
# Write a programme that works out all the different ways £2.50 can be made using any number of coins.

#
# DISCLAIMER: THIS PROGRAM IS FULLY FUNCTIONAL YET IT IS VERY COMPUTATIONALLY EXPENSIVE HENCE A LARGE AMOUNT OF TIME AND COMPUTING POWER IS REQUIRED FOR THIS ALGORITHM
#

def main():
  value = 2.50
  
  amounts = [2, 1, 0.50, 0.20, 0.10, 0.05, 0.02, 0.01]

  # This line adds the maximum number of duplicates of each element and then flattens the list.
  amounts = [j for i in amounts for j in [i for _ in range(int(value // i))]]
  
  pastCombinations = set()

  # Finds all combinations of the amounts list of different lengths from 2 to 250 and flatten the list
  allCombinations = (i for r in range(2, int(value // amounts[-1]) + 1) for i in itertools.combinations(amounts, r))

  # Verifies all of the combinations to make sure they sum to 2.50 and makes sure it's not a duplicate. Lastly, if it passes the condition, it adds it to the pastCombinations set.
  validCombinations = (i for i in allCombinations if sum(i) == value and i not in pastCombinations and not pastCombinations.add(i))

  for combination in validCombinations:
    print(combination)

if __name__ == "__main__":
  main()