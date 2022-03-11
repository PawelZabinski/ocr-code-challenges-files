import unittest
from main import tilingCost

class TestTiles(unittest.TestCase):

  def test_Cost_of_tiles_1(self):
    self.assertEqual(1_700, tilingCost(4, 5, cost=25))
  
  def test_Cost_of_tiles_2(self):
    self.assertEqual(2_100, tilingCost(3, 7, cost=40))
  
  def test_Cost_of_tiles_3(self):
    self.assertEqual(1_680, tilingCost(4, 4, cost=45))
  
  def test_Raise_ValueError_on_zero_width(self):
    with self.assertRaises(ValueError):
      tilingCost(0, 4, cost=25)
  
  def test_Raise_ValueError_on_zero_length(self):
    with self.assertRaises(ValueError):
      tilingCost(4, 0, cost=25)

if __name__ == '__main__':
  unittest.main()