# Ordering

# Create a program that allows entry of 10 numbers and then sorts them into ascending or descending order, based on user input.

def main():
  isNumber = input('Do you want to enter numbers or a string: [N/S] ').upper()

  if isNumber == 'N':
    nums = [int(input('Enter a number: ')) for _ in range(10)]

    order = input('Do you want to order in ascending or descending order [A/D]: ').upper()

    if order == 'A':
      nums.sort()
    elif order == 'D':
      nums.sort(reverse=True)
    
    print(nums)
  elif isNumber == 'S':
    string = [i for i in input('Enter a string: ')]

    order = input('Do you want to order in ascending or descending order [A/D]: ').upper()

    if order == 'A':
      string.sort()
    elif order == 'D':
      string.sort(reverse=True)
    
    print(''.join(string))

if __name__ == '__main__':
  main()