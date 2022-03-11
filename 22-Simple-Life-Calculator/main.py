import os

# Simple Life Calculator

# Create a program that has 3 simple calculators within it, e.g. VAT, Tax and Times table. Allow users to choose which calculator they want to use and then carry out that calculation.

def formatMoney(money):
  return '£{:,.2f}'.format(money)

def clearScreen():
  os.system('clear')
  print(f'<-------[ Life Calculator ]------->', end='\n'*2)

class LifeCalculator:
  def vat(money, rate=20):
    return f'VAT amount is {formatMoney(money * .2)}, bringing the total to {formatMoney(money * 1.2)}'

  def incomeTax(money):
    # Tax Brackets 2022
    # Personal Allowance   Up to £12,570          0%
    # Basic rate           £12,571 to £50,270   	20%
    # Higher rate          £50,271 to £150,000  	40%
    # Additional rate      over £150,000          45%

    PERSONAL_ALLOWANCE = (0, 0)
    BASIC_RATE = (12_570, .2)
    HIGHER_RATE = (50_270, .4)
    ADDITIONAL_RATE = (150_000, .45)

    BRACKETS = [PERSONAL_ALLOWANCE, BASIC_RATE, HIGHER_RATE, ADDITIONAL_RATE]
    
    standingTotal = money
    taxTotal = 0

    for rate in BRACKETS[::-1]:
      if standingTotal > rate[0]:
        standingTotal -= rate[0]

        taxTotal += standingTotal * rate[1]

    return f'Income tax total is {formatMoney(taxTotal)}, reducing your income to {formatMoney(money - taxTotal)}'

  def timesTable(number, columns=12):
    return '\n'.join([f'{number} x {i} = {number*i}' for i in range(1, columns+1)])

def main():
  while True:
    clearScreen()
    
    for i, j in enumerate(['VAT', 'Income Tax', 'Times Table']):
      print(f'[{i}] {j}')
      
    print()
    
    selection = int(input('Enter a number: '))
    result: str

    clearScreen()

    if selection == 0:
      money = int(input('Amount of money: '))
      result = LifeCalculator.vat(money)
    elif selection == 1:
      money = int(input('Amount of money earned: '))
      result = LifeCalculator.incomeTax(money)
    elif selection == 2:
      number = int(input('Time table column: '))
      result = LifeCalculator.timesTable(number)

    clearScreen()
    print(result)

    input()
    

if __name__ == '__main__':
  main()