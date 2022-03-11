# Even more Odd

# Create a program that accepts and random integer array (at least 10 integers) and orders them firstly by size, (small to large), and then puts all the even numbers AFTER the odd
# numbers within the array. It then echos the original array and the modified array to screen. E.g. an array 1,2,3,4,5,6,7,8,9,10 would be output 1,3,5,7,9,2,4,6,8,10.

def arrayInput(message=''):
  return input(message).split(', ')

def main():
  nums = arrayInput('Enter an array: ')

  chars = [i for i in nums if not i.isdigit()]
  evenNums = [int(i) for i in nums if i.isdigit() and int(i)%2==0]
  oddNums = [int(i) for i in nums if i.isdigit() and int(i)%2!=0]

  chars.sort(reverse=True)
  evenNums.sort()
  oddNums.sort()

  newNums = [str(i) for i in chars+oddNums+evenNums]
  print(f"New array: {', '.join(newNums)}")

if __name__ == '__main__':
  main()