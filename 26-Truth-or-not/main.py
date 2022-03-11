# Truth or not

# Create a program that would take the number of inputs in a logic circuit and works out the number of output lines are needed for the truth table. Have it draw the truth table
# on screen, using Columns for Inputs (A, B, C etc) and rows for the 1’s and 0’s.

HORIZONTAL_PADDING = 2
VERTICAL_PADDING = 1

PADDING = (' '*(HORIZONTAL_PADDING)) + '|' + (' '*(HORIZONTAL_PADDING))

class ConsoleManager:
  def formatBinary(binary, count):
    return f'{int(bin(binary)[2:]):0{count}}'

  def truthTable(inputLinesCount):
    return [PADDING.join([j for j in ConsoleManager.formatBinary(i, inputLinesCount)]) for i in range(2 ** inputLinesCount)]

def main():
  inputLinesCount = int(input('Enter number of inputs: '))
  print()

  lines = [f'|{" "*HORIZONTAL_PADDING}{i}{" "*HORIZONTAL_PADDING}|' for i in ConsoleManager.truthTable(inputLinesCount)]
  bottomBorder = '-'*len(lines[0])

  alphabet = [char for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']

  func = lambda i: alphabet.pop(0) if lines[0][i].isdigit() else '-'
  topBorder = ''.join([func(i) for i in range(len(lines[0]))])

  print(topBorder)
  print(('\n'*VERTICAL_PADDING).join(lines))
  print(bottomBorder)

if __name__ == '__main__':
  main()