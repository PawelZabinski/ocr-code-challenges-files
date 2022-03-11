import unittest
from main import encodeMorsecode, decodeMorsecode

class TestMorseCode(unittest.TestCase):

  def test_plain_text_to_morse(self):
    self.assertEqual('- .... .. ... | .. ... | - .... . | ..-. .. .-. ... - | - . ... - | -.-. .- ... . .-.-.-', encodeMorsecode('This is the first test case.'))

  def test_morse_to_plain_text(self):
    self.assertEqual('NOW TESTING THE DECODE FUNCTIONALITY, TEST NUMBER 2.', decodeMorsecode('-. --- .-- | - . ... - .. -. --. | - .... . | -.. . -.-. --- -.. . | ..-. ..- -. -.-. - .. --- -. .- .-.. .. - -.-- --..-- | - . ... - | -. ..- -- -... . .-. | ..--- .-.-.-'))

  def test_handle_special_characters(self):
    self.assertEqual('.... . .-.. .-.. --- --..-- | .-- --- .-. .-.. -.. | .-... | .--. . --- .--. .-.. . -.-.--', encodeMorsecode('Hello, world & people!'))

if __name__ == '__main__':
  unittest.main()