import re
import os

# Complex Numbers

# Have the programme show addition, multiplication, negation, and inversion of complex numbers in separate functions. (Subtraction and division operations can be made
# with pairs of these operations.) Print the results for each operation tested to screen.

#
# DISCLAIMER - I have used the complex conjugate method to divide complex numbers instead of multiplicative inverse
#

class ComplexNumbersCalculator:

  def _format(self, real, imaginary):
    if real % 1 == 0: real = int(real)
    if imaginary % 1 == 0: imaginary = int(imaginary)
    
    return f'{real} {"+" if imaginary >= 0 else "-"} {abs(imaginary) if abs(imaginary) != 1 else ""}i'
  
  def _extractVals(self, complexNumber):
    pattern = '^(-?[0-9]+(?:\.[0-9]+)?) ?([+-]) ?(-?[0-9]+(?:\.[0-9]+)?)?i$'
    
    if (m := re.match(pattern, complexNumber)):
      real = float(m.group(1))

    # Add the implicit coefficient of 1 if string is empty
      if (i := m.group(3)):
        imaginary = float(i)
      else:
        imaginary = 1

      return (real, imaginary if m.group(2) == '+' else -imaginary)
    
    raise ValueError('Invalid Complex Number')

  def addition(self, x, y):
    x = self._extractVals(x)
    y = self._extractVals(y)

    return self._format(real=x[0] + y[0], imaginary=x[1] + y[1])
  
  def multiplication(self, x, y):
    x = self._extractVals(x)
    y = self._extractVals(y)

    real = (x[0] * y[0]) - (x[1] * y[1])
    imaginary = (x[0] * y[1]) + (x[1] * y[0])

    return self._format(real=real, imaginary=imaginary)
  
  def negation(self, x):
    realNumber, imaginaryNumber = self._extractVals(x)

    return self._format(real=-realNumber, imaginary=-imaginaryNumber)

  def subtraction(self, x, y):
    x = self._extractVals(x)
    y = self._extractVals(self.negation(y))

    return self._format(real=x[0] + y[0], imaginary=x[1] + y[1])

  def division(self, x, y):
    x = self._extractVals(x)
    y = self._extractVals(y)

    complexConjugate = (y[0], -y[1])

    numerator = self._extractVals(self.multiplication(self._format(real=x[0], imaginary=x[1]), self._format(real=complexConjugate[0], imaginary=complexConjugate[1])))
    denominator = self._extractVals(self.multiplication(self._format(real=y[0], imaginary=y[1]), self._format(real=complexConjugate[0], imaginary=complexConjugate[1])))[0]

    real = numerator[0] / denominator
    imaginary = numerator[1] / denominator

    return self._format(real=real, imaginary=imaginary)

def newFrame():
  os.system('clear')
  print(f'<{"-"*7}[ COMPLEX NUMBERS ]{"-"*7}>', end='\n'*2)

def main(calculator=ComplexNumbersCalculator()):
  newFrame()

  for i, j in enumerate(['Addition', 'Subtraction', 'Multiplication', 'Division', 'Exit']):
    print(f'[{i}] {j}')
  
  print()

  selection = int(input('Enter a number: '))
  if not 0 <= selection < 4: return 

  print()

  complexNumberOne = input('Enter a complex number: ')
  complexNumberTwo = input('Enter another complex number: ')

  print('\nThe answer is: ', end='')

  if selection == 0:
    print(calculator.addition(complexNumberOne, complexNumberTwo))
  elif selection == 1:
    print(calculator.subtraction(complexNumberOne, complexNumberTwo))
  elif selection == 2:
    print(calculator.multiplication(complexNumberOne, complexNumberTwo))
  elif selection == 3:
    print(calculator.division(complexNumberOne, complexNumberTwo))

  input()
  main()

if __name__ == '__main__':
  main()