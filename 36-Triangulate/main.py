import math
import os

# Triangulate

# Create a program that accepts 3 sides of a triangle. It then works out if these sides form a triangle, and if so, what type of triangle (e.g. Scalene, Isosceles, Right-Angle....)

def newFrame():
  os.system('clear')
  print(f'<{"-"*7}[ TRIANGULATE ]{"-"*7}>', end='\n'*2)

class TriangleManager:
  def isTriangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
      return True
    
    return False
  
  def triangleType(a, b, c):
    sides = [a, b, c]
    sides.sort()

    if a == b == c: return 'Equilateral'
    if a == b or a == c or b == c: return 'Isosceles'
    if sides[0]**2 + sides[1]**2 == sides[2]**2: return 'Right-angle'

    return 'Scalene'

def missingSideLength():
  a = float(input('Side A: '))
  b = float(input('Side B: '))
  angle = float(input('Angle: '))

  print()

  # Law of Cosines 
  c = (a**2 + b**2 - (2 * a * b * math.cos(math.radians(angle)))) ** 0.5

  print(f'The missing side length is {c}')


def triangleType():
  a = float(input('Side A: '))
  b = float(input('Side B: '))
  c = float(input('Side C: '))

  print()

  if TriangleManager.isTriangle(a, b, c):
    triangleType = TriangleManager.triangleType(a, b, c)
    
    print(f'This is a {triangleType} triangle')

    return
  
  print('Not a triangle.')

def main():
  newFrame()

  for i, j in enumerate(['Triangle Type', 'Missing Side', 'Exit']):
    print(f'[{i}] {j}')

  print()
  
  selection = int(input('Enter a number: '))

  if not 0 <= selection < 3:
    main()
    return

  if selection == 2:
    return

  newFrame()

  if selection == 0:
    triangleType()
  elif selection == 1:
    missingSideLength()
  
  input()
  
  main()

if __name__ == '__main__':
  main()