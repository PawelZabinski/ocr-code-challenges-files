import os
import time

# The meaning of life

# Have the program make an animation of the game of life (https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life).

'''
[
  [DEAD, DEAD, DEAD, DEAD, DEAD, DEAD],
  [DEAD, DEAD, DEAD, DEAD, DEAD, DEAD],
  [DEAD, DEAD, ALIVE, ALIVE, ALIVE, DEAD],
  [DEAD, ALIVE, ALIVE, ALIVE, DEAD, DEAD],
  [DEAD, DEAD, DEAD, DEAD, DEAD, DEAD],
  [DEAD, DEAD, DEAD, DEAD, DEAD, DEAD]
]

[
  [DEAD, DEAD, ALIVE, DEAD, DEAD, DEAD, DEAD],
  [ALIVE, DEAD, ALIVE, DEAD, DEAD, DEAD, DEAD],
  [DEAD, ALIVE, ALIVE, DEAD, DEAD, DEAD, DEAD],
  [DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD],
  [DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD],
  [DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD],
  [DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD]
]
'''

ALIVE = '⬜️'
DEAD = '⬛️'

TICK_DURATION = .5


class OptionalList(list):
  def __getitem__(self, index):
    if 0 <= index < len(self):
      return list.__getitem__(self, index)
    
    return OptionalList()

def newFrame():
  os.system('clear')
  print(f'<{"-"*7}[ GAME OF LIFE ]{"-"*7}>', end='\n'*2)

def arrayGrid(array):
  if len(array) == 0:
    raise ValueError('Array shall not be empty')
    
  rows = ['| ' + ''.join(i) + ' |'  for i in array]

  length = len(rows[0]) - 2

  output = [
    f'/{"-" * length}\\',
    *rows,
    f'\{"-" * length}/'
  ]

  return '\n'.join(output)

def main():
  newFrame()

  columns = int(input('Enter the number of columns: '))
  rows = int(input('Enter the number of rows: '))

  newFrame()

  print('INSTRUCTIONS - A value of "1" means the cell is alive, "0" means the cell is dead. Make sure to add a single space between each column.')

  input()
  newFrame()

  grid = [input(f'Row {i + 1}: ').strip().split(' ') for i in range(rows)]
  grid = [[(ALIVE if j == '1' else DEAD) for j in i] for i in grid]

  # Verify inputs
  assert len(grid) == rows

  for i in grid:
    assert len(i) == columns
  
  configuration = OptionalList([OptionalList(i) for i in grid])

  # Checks if there are at least one alive
  while True:
    newFrame()

    print(arrayGrid(configuration))

    newConfiguration = OptionalList([OptionalList([j for j in i]) for i in configuration])

    for y in range(len(configuration)):
      for x in range(len(configuration[y])):
        availablePixels = [
          configuration[y - 1][x - 1],
          configuration[y - 1][x],
          configuration[y - 1][x + 1],

          configuration[y][x - 1],
          configuration[y][x + 1],

          configuration[y + 1][x - 1],
          configuration[y + 1][x],
          configuration[y + 1][x + 1]
        ]

        count = len([i for i in availablePixels if i == ALIVE])

        # Any live cell with two or three live neighbours lives on to the next generation.

        if configuration[y][x] == ALIVE:
          # Any live cell with fewer than two live neighbours dies, as if by underpopulation.
          # Any live cell with more than three live neighbours dies, as if by overpopulation.
          if 4 <= count or count < 2:
            newConfiguration[y][x] = DEAD
        elif configuration[y][x] == DEAD:
          # Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
          if count == 3:
            newConfiguration[y][x] = ALIVE
    
    if configuration == newConfiguration:
      break
      
    configuration = newConfiguration
    
    time.sleep(TICK_DURATION)
  

if __name__ == '__main__':
  main()