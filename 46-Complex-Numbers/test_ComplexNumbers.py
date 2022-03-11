import unittest
from main import ComplexNumbersCalculator

class TestComplexNumbers(unittest.TestCase):
  def setUp(self):
    self.calculator = ComplexNumbersCalculator()
  
  # Formatting
  def test_Formatting_on_imaginary_and_real_number(self):
    self.assertEqual('7 + 3i', self.calculator._format(imaginary=3, real=7))
  
  def test_Formatting_on_imaginary_and_negative_real_number(self):
    self.assertEqual('-7 + 3i', self.calculator._format(imaginary=3, real=-7))
  
  def test_Formatting_on_negative_imaginary_and_real_number(self):
    self.assertEqual('7 - 3i', self.calculator._format(imaginary=-3, real=7))
  
  def test_Formatting_on_negative_imaginary_without_coefficient_and_negative_number(self):
    self.assertEqual('-7 - i', self.calculator._format(imaginary=-1, real=-7))
  
  def test_Formatting_on_imaginary_with_coefficient_of_1(self):
    self.assertEqual('3 + i', self.calculator._format(imaginary=1, real=3))

  # Extract values
  def test_Extract_positive_complex_numbers(self):
    self.assertEqual(self.calculator._extractVals('5 + 2i'), (5, 2))
  
  def test_Extract_negative_complex_numbers(self):
    self.assertEqual(self.calculator._extractVals('-9 - 2i'), (-9, -2))
  
  def test_Extract_positive_complex_numbers_without_coefficient(self):
    self.assertEqual(self.calculator._extractVals('3 + i'), (3, 1))
  
  def test_Extract_function_should_raise_ValueError_on_invalid_missing_real_number(self):
    with self.assertRaises(ValueError):
      self.calculator._extractVals('2i')
  
  def test_Extract_function_should_raise_ValueError_on_invalid_missing_imaginary_number(self):
    with self.assertRaises(ValueError):
      self.calculator._extractVals('6')
  
  # Addition
  def test_Addition_of_two_complex_numbers(self):
    self.assertEqual('4 + 6i', self.calculator.addition('1 + 4i', '3 + 2i'))
  
  def test_Addition_of_two_complex_number_equal_to_zero(self):
    self.assertEqual('0 + 0i', self.calculator.addition('3 - 4i', '-3 + 4i'))

  def test_Addition_of_two_complex_numbers_without_coefficient(self):
    self.assertEqual('6 + 2i', self.calculator.addition('2 + i', '4 + i'))
  
  # Subtraction
  def test_Subtraction_of_two_complex_numbers(self):
    self.assertEqual('3 - 2i', self.calculator.subtraction('5 + i', '2 + 3i'))
  
  def test_Subtraction_of_two_complex_numbers_without_coefficient_and_double_negative(self):
    self.assertEqual('3 + 3i', self.calculator.subtraction('5 + 2i', '2 - i'))

  # Multiplication
  def test_Multiplication_of_two_complex_numbers(self):
    self.assertEqual('-11 + 23i', self.calculator.multiplication('3 + 2i', '1 + 7i'))

  def test_Multiplication_of_two_complex_numbers_with_no_coefficient(self):
    self.assertEqual('0 + 2i', self.calculator.multiplication('1 + i', '1 + i'))

  # Division
  def test_Division_of_two_complex_numbers(self):
    self.assertEqual('8 - 5i', self.calculator.division('14 - 31i', '3 - 2i'))
  
  def test_Division_of_two_complex_numbers_with_decimals(self):
    self.assertEqual('0.17647058823529413 + 1.2941176470588236i', self.calculator.division('2 + 5i', '4 - i'))

  # Negation
  def test_Negation_of_a_complex_number(self):
    self.assertEqual('3 - 2i', self.calculator.negation('-3 + 2i'))
  
  def test_Negation_of_a_complex_number_with_no_coefficient(self):
    self.assertEqual('-6 + i', self.calculator.negation('6 - i'))

if __name__ == '__main__':
  unittest.main()