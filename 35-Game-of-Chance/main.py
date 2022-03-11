import functools
import random
import os

# Game of Chance

# A user can bet on any number from 0 to 30. If it’s an even number they 2x their money back. If it’s a multiple of 10 they get 3x their money back. If it’s a prime number they
# get 5x their money back. If the number is below 5 they get a 2x bonus.
# Create a program that allows the user to guess a number. A random number is generated. If the guess == the random number then the user wins and gets a pay-out.
# Combinations of the win scenarios should be catered for.. e.g. 20 wins 2 x 3 bonus = 6x their money.

ORIGINAL_DEPOSIT = 10
MULTIPLIERS = [lambda i: 2 if i % 2 == 0 else 1, lambda i: 3 if i % 10 == 0 else 1, lambda i: 5 if isPrime(i) else 1, lambda i: 2 if i < 5 else 1]

YELLOW = '\33[33m'
NORMAL = '\33[0m'

class ConsoleManager:
  def newFrame(balance):
    os.system('clear')
    print(f'<{"-"*7}[ GAME OF CHANCE ]{"-"*7}>', end='\n'*2)
    ConsoleManager.displayBalance(balance)

  def enterToContinue():
    input()
  
  def formatMoney(money):
    return f'£{money:,.02f}'
  
  def displayBalance(money):
    print(f'BALANCE: {ConsoleManager.formatMoney(money)}', end='\n'*2)
  
  def warn(message):
    input(f'\n{YELLOW}[WARNING] {message}{NORMAL} ')

def isPrime(num):
  if num == 1: return True

  for i in range(2, num//2+1):
    if num % i == 0:
      return False
  
  return True

class Player:
  def __init__(self):
    self.money = ORIGINAL_DEPOSIT
  
  def bet(self, nums):
    guesses = [(*i, Player.betMultiplier(i)) for i in nums]
    randomNum = random.randint(1, 30)

    moneyGained = sum([(i[1]*i[2] if i[0]==randomNum else -i[1]) for i in guesses])
    correctGuesses = [i for i in guesses if i[0] == randomNum]

    ConsoleManager.newFrame(balance=self.money)

    for guess in guesses:
      print(f' - You bet {ConsoleManager.formatMoney(guess[1])} for the number "{guess[0]}", your win multiplier is x{guess[2]}"')

    ConsoleManager.enterToContinue()

    print(f'RANDOM NUMBER: {randomNum}', end='\n'*2)

    if len(correctGuesses):
      if moneyGained > 0:
        print(f'Your guess was correct, {ConsoleManager.formatMoney(moneyGained)} gained.')
      else:
        print(f'Your guess was correct, yet you still lost {ConsoleManager.formatMoney(-moneyGained)}')
    else:
      print(f'Your guess was wrong, you lost {ConsoleManager.formatMoney(-moneyGained)}')

    self.money += moneyGained

  @classmethod
  def generateNumber(cls):
    return random.randint(1, 30)
  
  @classmethod
  def betMultiplier(cls, num):
    return functools.reduce(lambda x, y: x * y, [i(num[0]) for i in MULTIPLIERS])

def main():
  player = Player()

  # Play until the player has lot all money
  while player.money > 0:
    ConsoleManager.newFrame(balance=player.money)

    guessCount = int(input('How many guesses do you wish to make this round? '))
    nums = [(int(input(f'\nNo. {i+1} Guess: ')), float(input(f'No. {i+1} Guess Value: £'))) for i in range(guessCount)]
    
    # Verify that the player bet a valid amount (non-negative)
    invalidNums = [i for i in nums if i[1] < 0]

    if len(invalidNums):
      ConsoleManager.warn(f'You bet an invalid amount of {ConsoleManager.formatMoney(invalidNums[0][1])}')
      continue

    # Verify that the player did not bet more than he can afford
    moneySum = sum([i[1] for i in nums])
    
    if moneySum > player.money:
      ConsoleManager.warn('You bet more money than you can afford.')
      continue

    player.bet(nums)

    ConsoleManager.enterToContinue()
  
  ConsoleManager.newFrame(balance=player.money)
  print('You went bankrupt.')
    

if __name__ == '__main__':
  main()