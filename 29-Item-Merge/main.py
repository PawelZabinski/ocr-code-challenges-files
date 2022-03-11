# Item Merge

# Create a program that will compare two shopping lists from “Week A” and “Week B”. It will return any unique items contained on the list.

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def flatMap(arr, func=lambda x: x):
  return [func(j) for i in arr for j in i]

def main():
  getList = lambda x: input(f'{x} Shopping List: ').lower().split(', ')

  shoppingListsCount = int(input('Number of shopping lists: '))
  shoppingLists = flatMap([getList(f'Week {ALPHABET[i%26]}') for i in range(shoppingListsCount)])

  unique = [i for i in shoppingLists if shoppingLists.count(i) == 1]
  
  count = [(i, shoppingLists.count(i)) for i in shoppingLists]
  count = list(dict.fromkeys(count))
  count.sort(key=lambda x: x[1], reverse=True)

  print()

  print(f'Unique Items: {", ".join(unique)}')
  print(f'3 Most popular items: {", ".join([i[0] for i in count[:3]])}')

if __name__ == '__main__':
  main()