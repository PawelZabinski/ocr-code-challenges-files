import unittest
from main import toRomanNumeral

class TestRomanNumerals(unittest.TestCase):
 
  def test_convert_integer_under_3(self):
    self.assertEqual(toRomanNumeral(1), 'I')
    self.assertEqual(toRomanNumeral(2), 'II')
    self.assertEqual(toRomanNumeral(3), 'III')

  def test_convert_integer_under_8(self):
    self.assertEqual(toRomanNumeral(4), 'IV')
    self.assertEqual(toRomanNumeral(5), 'V')
    self.assertEqual(toRomanNumeral(8), 'VIII')

  def test_convert_integer_under_13(self):
    self.assertEqual(toRomanNumeral(9), 'IX')
    self.assertEqual(toRomanNumeral(12), 'XII')

  def test_convert_integer_under_100(self):
    self.assertEqual(toRomanNumeral(43), 'XLIII')
    self.assertEqual(toRomanNumeral(97), 'XCVII')

if __name__ == '__main__':
  unittest.main()