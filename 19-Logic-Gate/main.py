# Logic Gate

# Write a program that will give the students the answer to logic gate questions
# For example:
# Enter logic gate : OR
# Enter first input : 1
# Enter second input : 0
# Result = 1
# It should work for the logic gates OR, AND, XOR, NAND and NOR

logicGatesFunc = {
  'OR': lambda i, j: i | j,
  'AND': lambda i, j: i & j,
  'XOR': lambda i, j: i ^ j,
  'NAND': lambda i, j: not (i & j),
  'NOR': lambda i, j: not i and not j
}

def evaluateLogicGate(gate, first, second):
  func = logicGatesFunc[gate]

  result = func(first, second)

  if type(result) is bool:
    return 1 if result else 0

  return result

gate = input('Enter the logic gate: ')
first = int(input('Enter the first input: '))
second = int(input('Enter the second input: '))

print(evaluateLogicGate(gate, first, second))