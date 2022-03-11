# Number Table

# Write a program that takes a symbol (+,-,* or /) and a natural number (>0) and makes a table like below for the operation from 0 to n

def table(symbol, number):
  funcs = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y
  }

  func = funcs[symbol]
  
  print(f'{symbol} | {" ".join([str(i) for i in range(number + 1)])}')
  print('-'*(4 + (number + 1) * 2))

  for i in range(number + 1):
    print(f'{i} | {" ".join([str(func(j, i)) for j in range(number + 1)])}')

inputs = input('Enter your combination: ')

symbol = inputs[0]
number = int(inputs[1:])

table(symbol, number)
