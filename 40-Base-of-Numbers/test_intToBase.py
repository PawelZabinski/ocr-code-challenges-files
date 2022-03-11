import unittest
from utils import intToBase

class TestIntToBase(unittest.TestCase):

  def test_raisesValueErrorOnInvalidInput(self):
    with self.assertRaises(ValueError):
      intToBase(34, 1)
    
    with self.assertRaises(ValueError):
      intToBase(23, 40)
  
  def test_returns0WhenInputValueIsZero(self):
    self.assertEqual(intToBase(0, 2), '0')
    self.assertEqual(intToBase(0, 16), '0')
    self.assertEqual(intToBase(0, 36), '0')
  
  def test_denaryToBase2(self):
    self.assertEqual(intToBase(30, 2), '11110')
    self.assertEqual(intToBase(255, 2), '11111111')
  
  def test_denaryToBase16(self):
    self.assertEqual(intToBase(30, 16), '1E')
    self.assertEqual(intToBase(255, 16), 'FF')
    self.assertEqual(intToBase(32, 16), '20')
  
  def test_denaryToBase32(self):
    self.assertEqual(intToBase(31, 32), 'V')
    self.assertEqual(intToBase(25, 32), 'P')
    self.assertEqual(intToBase(4, 32), '4')

if __name__ == '__main__':
  unittest.main()