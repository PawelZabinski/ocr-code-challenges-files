import unittest
from main import isPrime

class TestIsPrime(unittest.TestCase):

  def test_primeNumbers(self):
    self.assertEqual(isPrime(2), True)
    self.assertEqual(isPrime(7), True)
    self.assertEqual(isPrime(13), True)
    self.assertEqual(isPrime(31), True)
    self.assertEqual(isPrime(101), True)
  
  def test_nonPrimeNumbers(self):
    self.assertEqual(isPrime(1), False)
    self.assertEqual(isPrime(4), False)
    self.assertEqual(isPrime(6), False)
    self.assertEqual(isPrime(9), False)
    self.assertEqual(isPrime(28), False)
    self.assertEqual(isPrime(49), False)
  
  def test_negativeNumbersNonPrimeNumbers(self):
    self.assertEqual(isPrime(-2), False)
    self.assertEqual(isPrime(-101), False)
    self.assertEqual(isPrime(-7), False)
    self.assertEqual(isPrime(-4671), False)

if __name__ == '__main__':
  unittest.main()