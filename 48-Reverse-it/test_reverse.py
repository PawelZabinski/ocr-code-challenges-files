import unittest
import main

class TestReverse(unittest.TestCase):

  def test_Reverse_a_string(self):
    self.assertEqual(main.reverse('hello'), 'olleh')
  
  def test_Reverse_empty_string(self):
    self.assertEqual(main.reverse(''), '')
  
  def test_Count_chars(self):
    self.assertEqual(main.countChars('hello', ['a', 'e', 'i', 'o', 'u']), 2)
  
if __name__ == '__main__':
  unittest.main()