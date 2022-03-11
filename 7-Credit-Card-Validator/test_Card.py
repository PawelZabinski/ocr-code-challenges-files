import unittest
from main import validate_card

class TestValidateCard(unittest.TestCase):

  def test_Validate_correct_card_number(self):
    self.assertEqual(True, validate_card("4586820597171037"))

  def test_Invalidate_incorrect_card_number(self):
    self.assertEqual(False, validate_card("4916932196037053"))

if __name__ == "__main__":
  unittest.main()