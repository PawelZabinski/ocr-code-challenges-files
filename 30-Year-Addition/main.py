# Year Addition

# Create a program that accepts a year in the format ####, e.g. 2015. The program then adds each digit of the year together and outputs the answer. E.g. 2015 becomes the output 8.
def guess():
  print('<-------[ Year Addition Guesser ]------->\n')

  for _ in range(3):
    guess = input('Enter you guess: ')
    guessSum = sum([int(i) for i in guess])
    result = int(guess) % guessSum

    if result == 0:
      return print('Well done! The MOD Division resulted in 0.')
    
    print(f'Incorrect Guess. The result was {result}\n')

  print('You were unable to guess the correct integer to get a MOD division of 0.')


def main():
  print('<-------[ Year Addition ]------->\n')

  year = input('Enter a year: ')
  yearSum = sum([int(i) for i in year])

  print(f'The digit sum of the year {year} is {yearSum}')

if __name__ == '__main__':
  main()
  # guess()