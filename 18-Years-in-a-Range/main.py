# Years in a Range

# Write a program to count the number years in a range that has a repeated digit.

def characterOccurance(text):
  characterCount = dict()

  for char in text:
    if characterCount.get(char, 0) > 0:
      characterCount[char] += 1
    else:
      characterCount[char] = 1

  return characterCount

def checkRepeatingChar(text):
  characterCount = characterOccurance(text)

  for value in characterCount.values():
     if value >= 2: return True

  return False

lbYear = int(input('Enter the lower bound: '))
upYear = int(input('Enter the upper bound: '))

years = [year for year in range(lbYear, upYear) if checkRepeatingChar(str(year))]

print('DISCLAIMER: The range used is exclusive meaning the upper bound is not taken into consideration')
print(f'There are {len(years)} years in the range, which have a repeating digit.')