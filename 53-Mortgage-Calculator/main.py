from enum import Enum

# Mortgage Calculator

# Have the programme calculate the monthly payments of a fixed term mortgage over given Nth terms at a given interest rate. Also figure out how long it will take the user to pay
# back the loan.

# DISCLAIMER - My knowledge on mortgages is rather limited, and so the output produced by this algorithm may not be fully correct.

# Mortgage magnitude the amount of money borrowed from the bank (money)
# Interest rate the percentage of the loan the bank takes (fixed)
# Mortgage term is the length of time that the mortgage has legal effect
# Loan to value refers to the amount of deposit paid and the ratio of the property value compared to the loan amount

class Intervals(Enum):
  annually = 1
  monthly = 12
  weekly = 52
  daily = 365

  def input(i):
    allCases = {
      'annually': Intervals.annually,
      'monthly': Intervals.monthly,
      'weekly': Intervals.weekly,
      'daily': Intervals.daily
    }

    return allCases[i]

class Loan:
  def __init__(self, propertyValue, loanDuration, rate, loanToValue, interval):
    self.propertyValue = propertyValue
    self.loanDuration = loanDuration
    self.rate = rate
    self.loanToValue = loanToValue
    self.interval = interval
  
  def costPerInterval(self):
    return self.simpleInterest() / (self.interval.value * self.loanDuration)

  def simpleInterest(self):
    return (1 + self.rate) * (self.propertyValue - self.deposit())

  def deposit(self):
    return -(self.propertyValue * (self.loanToValue - 1))

def main():
  propertyValue = float(input('Enter property value: £'))
  loanDuration = float(input('Enter quantity of years the mortgage spans: '))

  intervalType = input('Enter an interval for payments: ').lower()
  interval = Intervals.input(intervalType)

  rate = float(input('Enter loan interest rate: (in %) ')) / 100

  loanToValue = float(input('Enter loan-to-value: (in %) ')) / 100

  loan = Loan(propertyValue, loanDuration, rate, loanToValue, interval)
   
  print(f'\nOriginal Deposit for property is £{loan.deposit():,.02f}')
  print(f'{intervalType.title()} payments = £{loan.costPerInterval():,.02f}')
  
if __name__ == '__main__':
  main()