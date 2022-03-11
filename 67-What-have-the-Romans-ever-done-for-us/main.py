# What have the Romans ever done for us?

# Have the user enter a number and print it out in Roman numerals.

def toRomanNumeral(integer):
  int2rom = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

  roman = []

  while integer > 0:
    for i, rom in int2rom:
      while integer >= i:
        roman += rom
        integer -= i

  return ''.join(roman)

def main():
  integer = int(input('Enter an integer > '))
  romanNumeral = toRomanNumeral(integer)

  print(f'Roman Numeral: {romanNumeral}')

if __name__ == '__main__':
  main()