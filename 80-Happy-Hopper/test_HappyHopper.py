import unittest
from main import isHappyHopper

class TestIsHappyHopper(unittest.TestCase):
  def test_1_Should_return_True(self):
    self.assertEqual(isHappyHopper([1, 4, 2, 3]), True)
  
  def test_2_Should_return_False(self):
    self.assertEqual(isHappyHopper([1, 4, 3, 2]), False)
  
  def test_3_Should_return_True(self):
    self.assertEqual(isHappyHopper([5, 1, 4, 2, 3]), True)

if __name__ == '__main__':
  unittest.main()