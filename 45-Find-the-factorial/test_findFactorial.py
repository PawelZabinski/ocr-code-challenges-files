import unittest
from main import findFactorial

class TestFactorial(unittest.TestCase):

  def test_Should_return_a_valid_integer_1(self):
    self.assertEqual(4, findFactorial(24))
  
  def test_Should_return_a_valid_integer_2(self):
    self.assertEqual(9, findFactorial(362880))
  
  def test_Should_raise_ValueError_on_negative_input(self):
    with self.assertRaises(ValueError):
      findFactorial(-4)
  
  def test_Should_raise_ValueError_on_invalid_input(self):
    with self.assertRaises(ValueError):
      findFactorial(8)

if __name__ == '__main__':
  unittest.main()