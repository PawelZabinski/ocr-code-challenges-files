import unittest
from main import Loan, Intervals

class LoanTest(unittest.TestCase):

  def setUp(self):
    # propertyValue, loanDuration, rate, loanToValue, interval
    self.loan = Loan(1_000_000, 30, .04, .80, Intervals.monthly)
  
  def test_mortgage_deposit(self):
    self.assertAlmostEqual(200_000, self.loan.deposit())

  def test_mortgage_price_per_interval(self):
    self.assertAlmostEqual(2311.11111111, self.loan.costPerInterval())

if __name__ == '__main__':
  unittest.main()