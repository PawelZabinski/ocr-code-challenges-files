import random

# Of mice and men

# Have the programme allow a user to play the “mice and men” game. The game works like this:
# Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the user guessed correctly in the correct place, they have a “mouse”. For every
# digit the user guessed correctly in the wrong place is a “man” Every time the user makes a guess, tell them how many “mice” and “men” they have.
# Once the user guesses the correct number, the game is over. Keep track of the number of guesses the user makes throughout the game and tell the user at the end.

class Player:
  def __init__(self):
    self.guesses = 0

    self.randomNumber = Player.randomNumber(digits=4)

  def prompt(self):
    self.guesses += 1
  
    guess = input('Enter your four digit number guess > ')
    assert len(guess) == 4

    if guess == self.randomNumber:
      return True

    mice = 0
    men = 0

    for i in range(4):
      # Check if number is correct and in the right place
      if self.randomNumber[i] == guess[i]:
        mice += 1
      # Check if number is correct but not in the right place
      elif guess[i] in self.randomNumber:
        men += 1

    print(f'This round you had {formatQuantities(mice, "mouse", "mice")} and {formatQuantities(men, "man", "men")}', end='\n'*2)
      
  @staticmethod
  def randomNumber(digits):
    return ''.join([str(random.randint(0, 9)) for _ in range(digits)])

def formatQuantities(magnitude, singularNoun, pluralNoun):
  if magnitude == 1:
    return f'{magnitude} {singularNoun}'

  return f'{magnitude} {pluralNoun}'

def main():
  player = Player()

  while True:
    didGuessCorrectly = player.prompt()

    if didGuessCorrectly:
      print(f'Well done! You have guessed the number in {formatQuantities(player.guesses, "attempt", "attempts")}')
      break
  
if __name__ == '__main__':
  main()