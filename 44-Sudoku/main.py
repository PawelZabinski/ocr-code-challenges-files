import time
import os

# Sudoku

# Have the program solve a Sudoku (https://en.wikipedia.org/wiki/Sudoku).

TICK_DURATION = 0

class Sudoku:
  def __init__(self, board):
    self.board = board
  
  def isPossible(self, y, x, value):
    # Check if cell is empty
    if self.board[y][x] != 0:
      return False

    # Horizontal Check
    if value in self.board[y]:
      return False

    # Vertical Check
    if value in [i[x] for i in self.board]:
      return False

    # Sub Grid Check
    for i in range(3):
      for j in range(3):
        if self.board[(y // 3) * 3 + i][(x // 3) * 3 + j] == value:
          return False
    
    return True
  
  def solve(self):
    time.sleep(TICK_DURATION)

    for y in range(9):
      for x in range(9):

        # Check if cell is empty
        if self.board[y][x] == 0:
          for value in range(1, 10):
            
            # Check if its possible to set the cell to the value
            if self.isPossible(y, x, value):
              # Back tracking, assign the value, call itself but if the call comes back, return the value to its original value
              self.board[y][x] = value

              # Display the change
              newFrame()
              displayMatrix(self.board)

              self.solve()

              # If the board is not yet solved, backtrack
              if 0 in [i for j in self.board for i in j]:
                self.board[y][x] = 0
          
          return
    
def newFrame():
  os.system('clear')
  print(f'<{"-" * 11}[ SUDOKU ]{"-" * 11}>', end='\n' * 2)

def displayMatrix(matrix):
  for i in matrix:
    print(' | '.join([str(x) for x in i]))

def main():
  newFrame()

  print('INSTRUCTIONS - Write each cell as a number, if it is missing, replace it with a zero. Add a space to write the next cell. So it would look like this: "Enter Row 1: 0 7 4 2 1 0 0 0 0"')
  input()

  newFrame()

  sudoku = Sudoku([[int(x) for x in input(f'Enter Row {i + 1}: ').split(' ')] for i in range(9)])
  newFrame()
  
  sudoku.solve()


if __name__ == '__main__':
  main()