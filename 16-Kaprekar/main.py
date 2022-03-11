# Kaprekar

# Determine whether a number is a Kaprekar number or not. See http://mathworld.wolfram.com/KaprekarNumber.html for more information.

def isKaprekar(number):
  nums = [i for i in str(number ** 2)]
  count = len(nums)

  total = 0

  leading = nums[:count // 2]
  trailing = nums[count // 2:]

  leadingStr = ''.join(leading)
  trailingStr = ''.join(trailing)

  if leadingStr.isdigit(): total += int(leadingStr)
  if trailingStr.isdigit(): total += int(trailingStr)

  return total == number
  
number = int(input('Enter a number: '))
print(isKaprekar(number))