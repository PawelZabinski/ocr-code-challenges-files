import random

# Lists

# Create a list containing all integers within a given range. Insert an element at a given position into a list. Extract a given number of randomly selected elements from a list
# and create a list of lists. Sort the list of lists according to the length of sublists.

def main():
  # Create a list of integers within range
  lowerBound = int(input("Enter the range lower bound > "))
  upperBound = int(input("Enter the range upper bound (inclusive) > "))
  
  lst = [i for i in range(lowerBound, upperBound + 1)]

  # Insert element at given position
  element = int(input("Enter an element to insert > "))
  index = int(input("Enter the index in which to insert element > "))

  lst.insert(index, element)

  # Extract random numbers from list and make list of lists
  matrix = []

  listCount = int(input("Enter the number of lists in matrix > "))

  for i in range(listCount):
    elementsCount = int(input(f"Enter the number of random elements to extract for list {i} > "))

    randomElements = [random.choice(lst) for _ in range(elementsCount)]
    matrix.append(randomElements)
      
  # Sort the matrix
  matrix.sort(key=lambda x: len(x))

  # Display Matrix
  print("\nMatrix:")
  for i, j in enumerate(matrix):
    print(f"[{i}] {j}")

if __name__ == '__main__':
  main()