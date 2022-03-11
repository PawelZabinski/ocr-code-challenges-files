import math

# I like Pi

# Have the programme calculate pi to at least 30 decimal places.

def main():
  # Pi = x * sin(180 / x)
  
  x = 1_000_000_000
  
  print(f'{x * math.sin(math.radians(180 / x)):.48f}')

if __name__ == '__main__':
  main()