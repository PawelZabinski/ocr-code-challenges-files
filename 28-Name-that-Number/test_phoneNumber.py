import unittest
from main import PhoneNumberManager

class TestPhoneNumber(unittest.TestCase):
 
  def setUp(self):
    self.decrypt = PhoneNumberManager.decrypt
    self.validate = PhoneNumberManager.validate

  # Test Decrypt Method
  def test_decrypt_digits_and_letters(self):
    self.assertEqual('073899123', self.decrypt('07-FUZZ-123'))
  
  def test_decrypt_just_letters(self):
    self.assertEqual('72935', self.decrypt('PAWEL'))
  
  def test_decrypt_just_digits(self):
    self.assertEqual('07456329', self.decrypt('07456329'))

  # Test Validate Method
  def test_validate_correct_number_with_digits_and_letters(self):
    self.assertEqual(True, self.validate('07-AND-56-SAD'))
    self.assertEqual(True, self.validate('055INTEREST6-SAD'))
  
  def test_validate_incorrect_number_with_digits_and_letters(self):
    self.assertEqual(False, self.validate('07-ADNP-56-SAD'))
  
  def test_validate_incorrect_number_with_digits_and_letters_and_invalid_symbols(self):
    self.assertEqual(False, self.validate('07-AND-%56-SAD&'))

if __name__ == '__main__':
  unittest.main()