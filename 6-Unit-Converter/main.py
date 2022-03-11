# Unit Converter

# Converts various units between one another. The user enters the type of unit being entered, the type of unit they want to convert to and then the value. The program
# will then make the conversion.

def get_converter_func(convert_from, convert_to):
  funcs = {
    # Temperature
    ('Celsius', 'Fahrenheit'): lambda x: (x * 9/5) + 32,
    ('Celsius', 'Kelvin'): lambda x: x + 273.15,

    ('Fahrenheit', 'Celsius'): lambda x: (x - 32) * 5/9,
    ('Fahrenheit', 'Kelvin'): lambda x: (x - 32) * 5/9 + 273.15,

    ('Kelvin', 'Celsius'): lambda x: x -  273.15,
    ('Kelvin', 'Fahrenheit'): lambda x: ((x - 273.15) * 9/5) + 32,

    # Currency
    ('GBP', 'USD'): lambda x: x * 1.32,
    ('USD', 'GBP'): lambda x: x / 1.32,

    # Length
    ('milimetre', 'centimetre'): lambda x: x / 10,
    ('milimetre', 'metre'): lambda x: x / 1_000,
    ('milimetre', 'kilometre'): lambda x: x / 1_000_000,

    ('centimetre', 'milimetre'): lambda x: x * 10,
    ('centimetre', 'metre'): lambda x: x / 100,
    ('centimetre', 'kilometre'): lambda x: x / 100_000,

    ('metre', 'centimetre'): lambda x: x * 100,
    ('metre', 'milimetre'): lambda x: x * 1_000,
    ('metre', 'kilometre'): lambda x: x / 1_000,

    ('kilometre', 'metre'): lambda x: x * 1_000,
    ('kilometre', 'centimetre'): lambda x: x * 100_000,
    ('kilometre', 'milimetre'): lambda x: x * 1_000_000
  }

  return funcs.get((convert_from, convert_to))

def main():
  print('<-----[ UNIT CONVERTER ]----->')

  print('''
Available Units:
  - Temperature
    - Celsius
    - Fahrenheit
    - Kelvin
  - Currency
    - GBP
    - USD
  - Length
    - milimetre
    - centimetre
    - metre
    - kilometre
  ''')

  convert_from = input('Enter the unit to convert from ')
  convert_to = input('Enter the unit to convert to   ')

  value = int(input('Enter the value '))

  converter_func = get_converter_func(convert_from, convert_to)

  if converter_func is None:
    return print('\nInvalid Combination Given.')

  new_value = converter_func(value)
  print(f'Converted value = {new_value}')

if __name__ == '__main__':
  main()