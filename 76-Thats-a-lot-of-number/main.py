# That’s a lot of number
# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

def main():
  with open('number.txt', 'r') as file:
    numbers = [int(i) for i in file.readlines()]

  result = sum(numbers)
  firstTenDigits = str(result)[:10]

  print(firstTenDigits)

if __name__ == '__main__':
  main()