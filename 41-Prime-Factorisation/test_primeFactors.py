import unittest
from main import primeFactors

class TestPrimeFactors(unittest.TestCase):

  def test_return_valid_factors_if_value_is_not_a_prime_number(self):
    self.assertEqual(primeFactors(4), [2, 2])
    self.assertEqual(primeFactors(12), [2, 2, 3])
    self.assertEqual(primeFactors(36), [2, 2, 3, 3])
    self.assertEqual(primeFactors(45), [3, 3, 5])
  
  def test_Returns_itself_if_the_value_Is_a_prime_number(self):
    self.assertEqual(primeFactors(29), [29])
    self.assertEqual(primeFactors(17), [17])
    self.assertEqual(primeFactors(2), [2])
    self.assertEqual(primeFactors(101), [101])
  
  def test_raise_ValueError_on_0_or_negative_input(self):
    with self.assertRaises(ValueError):
      primeFactors(0)
    
    with self.assertRaises(ValueError):
      primeFactors(-7)
    
    with self.assertRaises(ValueError):
      primeFactors(-167)

if __name__ == '__main__':
  unittest.main()