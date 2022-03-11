CHARS = [i for i in '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ']

def intToBase(value, base):
  if not 36 >= base >= 2:
    raise ValueError('Invalid base')

  if value <= 0:
    return '0'
  
  digits = list()

  while value:
    digits.append(CHARS[value%base])

    value //= base
  
  return ''.join([str(i) for i in digits[::-1]])