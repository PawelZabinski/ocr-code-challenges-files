import csv 

# CSV File Utility

# Have the programme read a .CSV file of records, sort them, and then write them back to the file. Allow the user to choose various sorting algorithms based on a chosen field.

class FileUtility:

  @staticmethod
  def read(fileName):
    with open(f'{fileName}.csv', 'r') as file:
      reader = csv.DictReader(file)

      return [row for row in reader]

  @staticmethod
  def write(fileName, data):
    assert len(data) >= 1
    
    with open(f'{fileName}.csv', 'w') as file:
      writer = csv.DictWriter(file, data[0].keys())

      writer.writeheader()
      writer.writerows(data)

class SortAlgorithms:

  @classmethod
  def all(cls):
    return {
      'bubble': cls.bubble,
      'merge': cls.merge,
      'insertion': cls.insertion
    }

  @staticmethod
  def bubble(lst, key=None):
    isSorted = False

    while not isSorted:
      isSorted = True

      for i in range(len(lst) - 1):
        isGreater = lst[i][key] > lst[i + 1][key] if key else lst[i] > lst[i + 1]
        
        if isGreater:
          lst[i], lst[i + 1] = lst[i + 1], lst[i]
          isSorted = False

  @classmethod
  def merge(cls, lst, key=None):
    if len(lst) <= 1: return

    left = lst[:len(lst) // 2]
    right = lst[len(lst) // 2:]

    cls.merge(left, key)
    cls.merge(right, key)

    i = j = k = 0

    while i < len(left) and j < len(right):
      isGreater = left[i][key] < right[j][key] if key else left[i] < right[j]
      
      if isGreater:
        lst[k] = left[i]
        i += 1
      else:
        lst[k] = right[j]
        j += 1

      k += 1

    while i < len(left):
      lst[k] = left[i]
      
      i += 1
      k += 1

    while j < len(right):
      lst[k] = right[j]
      
      j += 1
      k += 1

  @staticmethod
  def insertion(lst, key=None):
    for i in range(1, len(lst)):
      ref = lst[i]

      ii = i - 1

      while ii >= 0 and (ref[key] < lst[ii][key] if key else ref < lst[ii]):
        lst[ii + 1] = lst[ii]
        ii -= 1

      lst[ii + 1] = ref

def main():
  fileName = input('Enter the file name: ')
  rows = FileUtility.read(fileName)

  print('\nSorting Algorithms:')
  
  for i in SortAlgorithms.all().keys():
    print(f'* {i}')

  sortingAlgorithm = input('\nEnter the name of the sorting algorithm: ')
  sortingAlgorithm = SortAlgorithms.all()[sortingAlgorithm]

  key = input('\nEnter the key used to sort csv rows: ')

  sortingAlgorithm(rows, key=key)

  FileUtility.write(f'new{fileName.title()}', rows)

if __name__ == '__main__':
  main()