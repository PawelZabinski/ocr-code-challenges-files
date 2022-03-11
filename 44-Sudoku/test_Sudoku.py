import unittest
from main import Sudoku

class TestSudoku(unittest.TestCase):
  def setUp(self):
    self.sudoku = Sudoku([
      [0, 0, 0, 2, 6, 0, 7, 0, 1],
      [6, 8, 0, 0, 7, 0, 0, 9, 0],
      [1, 9, 0, 0, 0, 4, 5, 0, 0],
      [8, 2, 0, 1, 0, 0, 0, 4, 0],
      [0, 0, 4, 6, 0, 2, 9, 0, 0],
      [0, 5, 0, 0, 0, 3, 0, 2, 8],
      [0, 0, 9, 3, 0, 0, 0, 7, 4],
      [0, 4, 0, 0, 5, 0, 0, 3, 6],
      [7, 0, 3, 0, 1, 8, 0, 0, 0]
    ])

    self.sudoku2 = Sudoku([
      [5, 3, 0, 0, 7, 0, 0, 0, 0],
      [6, 0, 0, 1, 9, 5, 0, 0, 0],
      [0, 9, 8, 0, 0, 0, 0, 6, 0],
      [8, 0, 0, 0, 6, 0, 0, 0, 3],
      [4, 0, 0, 8, 0, 3, 0, 0, 1],
      [7, 0, 0, 0, 2, 0, 0, 0, 6],
      [0, 6, 0, 0, 0, 0, 2, 8, 0],
      [0, 0, 0, 4, 1, 9, 0, 0, 5],
      [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ])

  def test_Should_return_true_on_isPossible_method_call_1(self):
    self.assertEqual(True, self.sudoku.isPossible(2, 2, value=7))
  
  def test_Should_return_true_on_isPossible_method_call_2(self):
    self.assertEqual(True, self.sudoku.isPossible(7, 3, value=9))
  
  def test_Should_return_false_on_isPossible_method_call_1(self):
    self.assertEqual(False, self.sudoku.isPossible(3, 5, value=1))
  
  def test_Should_return_false_on_isPossible_method_call_2(self):
    self.assertEqual(False, self.sudoku.isPossible(2, 7, value=2))

  def test_Should_return_false_on_isPossible_method_call_3(self):
    self.assertEqual(False, self.sudoku.isPossible(1, 3, value=1))

  def test_Should_return_solved_sudoku_1(self):
    self.sudoku.solve()

    self.assertEqual(self.sudoku.board, [
      [4, 3, 5, 2, 6, 9, 7, 8, 1], 
      [6, 8, 2, 5, 7, 1, 4, 9, 3], 
      [1, 9, 7, 8, 3, 4, 5, 6, 2], 
      [8, 2, 6, 1, 9, 5, 3, 4, 7], 
      [3, 7, 4, 6, 8, 2, 9, 1, 5], 
      [9, 5, 1, 7, 4, 3, 6, 2, 8], 
      [5, 1, 9, 3, 2, 6, 8, 7, 4], 
      [2, 4, 8, 9, 5, 7, 1, 3, 6], 
      [7, 6, 3, 4, 1, 8, 2, 5, 9]
    ])

  def test_Should_return_solved_sudoku_2(self):
    self.sudoku2.solve()

    self.assertEqual(self.sudoku2.board, [
      [5, 3, 4, 6, 7, 8, 9, 1, 2],
      [6, 7, 2, 1, 9, 5, 3, 4, 8],
      [1, 9, 8, 3, 4, 2, 5, 6, 7],
      [8, 5, 9, 7, 6, 1, 4, 2, 3],
      [4, 2, 6, 8, 5, 3, 7, 9, 1],
      [7, 1, 3, 9, 2, 4, 8, 5, 6],
      [9, 6, 1, 5, 3, 7, 2, 8, 4],
      [2, 8, 7, 4, 1, 9, 6, 3, 5],
      [3, 4, 5, 2, 8, 6, 1, 7, 9]
    ])

if __name__ == '__main__':
  unittest.main()