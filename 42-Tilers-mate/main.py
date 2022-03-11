# Tilers mate

# Have the user enter the Width and Length of the floor and have the program calculate the total cost of tiles it would take to cover a floor plan using a cost entered by the user (per tile or metre2).
TILES = [('Ceramic', 20), ('Porcelain', 25), ('Mosaic', 30), ('Limestone', 35), ('Marble', 45)]

LABOUR = 50
GROUT_AND_ADHESIVE = 10

def tilingCost(width, length, cost):
  if width <= 0: raise ValueError('Width cannot be zero or less.')
  elif length <= 0: raise ValueError('Length cannot be zero or less.')

  area = width * length

  totalCost = sum([area * i for i in [cost, LABOUR, GROUT_AND_ADHESIVE]])
  return totalCost


def main():
  width = int(input('Enter the width (in metres): '))
  length = int(input('Enter the length (in metres): '))

  # Skip a line
  print()

  for i, j in enumerate(TILES):
    print(f'[{i}] {j[0]} Tiles')
  
  # Skip a line
  print()

  selection = int(input('Enter a number: '))
  assert 0 <= selection < len(TILES)

  # Skip a line
  print()

  cost = tilingCost(width, length, TILES[selection][1])
  print(f'Estimated cost of tiling is £{cost * 1.2:,.02f} (with VAT) and £{cost:,.02f} (without VAT)')


if __name__ == '__main__':
  main()