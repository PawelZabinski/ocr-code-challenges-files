from int_to_str import int_to_str

# 1 LINER!!!
def singAlongOneLiner():
  for i in range(10, 0, -1): print(f'{["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"][i].title()} green bottles hanging on the wall,\n'*2+'And if one green bottle should accidentally fall,\n'+f'There\'ll be {["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"][i-1]} green bottles hanging on the wall.', end='\n'*2)

# 2 LINES!!!!
def singAlongShortestSolution():
  NUMS = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
  for i in range(10, 0, -1): print(f'{NUMS[i].title()} green bottles hanging on the wall,\n'*2+'And if one green bottle should accidentally fall,\n'+f'There\'ll be {NUMS[i-1]} green bottles hanging on the wall.', end='\n'*2)

def singAlongStartingNumberInput():
  startingNumber = int(input('Starting Number: '))
  NUMS = [int_to_str(i) for i in range(startingNumber+1)]

  for i in range(startingNumber, 0, -1):
    print(f'{NUMS[i].title()} green bottles hanging on the wall,\n'*2, end='')
    print('And if one green bottle should accidentally fall,')
    print(f'There\'ll be {NUMS[i-1]} green bottles hanging on the wall.', end='\n'*2)

if __name__ == '__main__':
  singAlongStartingNumberInput()