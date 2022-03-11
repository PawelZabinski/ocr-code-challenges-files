from enum import Enum

# Checkmate checker

# Create a programme that checks whether a King is in check in a given chess game configuration.
# There will be an arbitrary number of board configurations in the input, each consisting of eight lines of eight characters each. A ``.’’ denotes an empty square, while upper- and lowercase letters represent the pieces as defined above. There will be no invalid characters and no configurations where both kings are in check. You must read until you find an empty board consisting only of ``.’’ characters, which should not be processed. There will be an empty line between each pair of board configurations. All boards, except for the empty one, will contain exactly one white king and one black king.

INSTRUCTIONS = '''Chess Pieces:
* Pawn: 'p'
* Castle: 'c'
* Bishop: 'b'
* Queen: 'q'
* King: 'k'
* Knight: 'n'

# White: Upper case
# Black: Lower case

// Black Pieces should be at the top of the board
// White Pieces should be at the bottom of the board

!! Include a space character ' ' between each chess piece
'''

class Colour(Enum):
  white = 'white'
  black = 'black'

class ChessPiece:
  def __init__(self, name, letter, movements):
    self.name = name
    self.letter = letter
    self.movements = movements

    # Flatten the movements list and remove duplicates and invalid values
    for key in self.movements.keys():
      self.movements[key] = [i for internalList in self.movements[key] for i in internalList]
      self.movements[key] = list(dict.fromkeys(self.movements[key]))
      self.movements[key] = [i for i in self.movements[key] if i != (0, 0)]

  def possiblePositions(self, x, y, colour=None):
    movements = self.movements.get('.', self.movements.get(colour))
    return [(newX, newY) for i in movements if (newX := x + i[0]) in range(0, 8) and (newY := y - i[1]) in range(0, 8)]

  # Used to visualise the available movements of a chess piece
  def visualiseMovements(self, position=(3, 3), colour=None):
    board = [['-' for _ in range(8)] for _ in range(8)]
    board[position[1]][position[0]] = '#'
    
    movements = self.possiblePositions(x=position[0], y=position[1], colour=colour)

    for movement in movements:
      board[movement[1]][movement[0]] = '$'

    print(colour.value.title(), self.name)
    print('\n'.join([' '.join(row) for row in board]))

MOVEMENT_RANGE = range(-7, 8)
    
class ChessPieces(Enum):
  pawn = ChessPiece('Pawn', 'p', { Colour.white: [[(-1, 1), (1, 1)]], Colour.black: [[(-1, -1), (1, -1)]] })
  castle = ChessPiece('Castle', 'c', { '.': [[(0, i), (i, 0)] for i in MOVEMENT_RANGE] })
  bishop = ChessPiece('Bishop', 'b', { '.': [[(i, i), (i, -i), (-i, i)] for i in MOVEMENT_RANGE] })
  queen = ChessPiece('Queen', 'q', { '.': [[(0, i), (i, 0), (i, i), (i, -i), (-i, i)] for i in MOVEMENT_RANGE] })
  king = ChessPiece('King', 'k', { '.': [[(i, i), (-i, i), (0, i), (i, 0)] for i in range(-1, 2)] })
  knight = ChessPiece('Knight', 'n', { '.': [[(i, 3 - abs(i)), (i, -(3 - abs(i)))] for i in range(-2, 3) if i != 0] })

def ordinalSuffix(num):
  
  # Numbers 10 to 20 behave differently to the pattern.
  if num % 100 in range(10, 20):
    return "th"

  conversions = {
    1: "st",
    2: "nd",
    3: "rd"
  }

  return conversions.get(num % 10, "th")

def inputMatrix(length=8):
  matrix = [input(f"Enter {i}{ordinalSuffix(i)} row > ") for i in range(1, length + 1)]
  matrix = [i.split(" ") for i in matrix]

  gap()
  
  return matrix

def check(board):
  letter2chessPiece = { i.value.letter: i.value for i in ChessPieces }
  
  for y in range(8):
    for x in range(8):
      letter = board[y][x]
      
      piece = letter2chessPiece.get(letter.lower())
      if piece is None: continue

      colour = Colour.black if letter.islower() else Colour.white

      # Iterate over all potential movements and check if one of them lands on the king
      for movement in piece.possiblePositions(x=x, y=y, colour=colour):
        newLetter = board[movement[1]][movement[0]]

        # Check if newLetter is the opposition king
        oppositionKing = 'K' if colour == Colour.black else 'k'
        oppositionColour = Colour.white if colour == Colour.black else Colour.black

        if newLetter == oppositionKing:
          return f'{oppositionColour.value.title()} king is in check'
  
  return 'No king is in check'

def gap(): print()

def recursiveBoardInput():
  # Receive board input from the user until an empty board is received
  while True:
    board = inputMatrix()

    # If the board is empty, stop receiving input
    if board == [['.' for _ in range(8)] for _ in range(8)]:
      break

    yield board

def main():
  # Show instructions and introduction
  print(INSTRUCTIONS)

  for piece in [i.value for i in ChessPieces]:
    piece.visualiseMovements(colour=Colour.black)

  gap()
  
  boards = [board for board in recursiveBoardInput()]
  
  gap()
  
  results = [check(board) for board in boards]

  for d, result in enumerate(results):
    print(f'Game {d + 1}: {result}')

if __name__ == "__main__":
  main()