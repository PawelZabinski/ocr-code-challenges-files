import datetime

# What’s the day?

# Design a program to take 3 inputs, one for day, one for month and one for year. Get your program to validate if this is an actual day, and, if it is, output the day of the week it is!

WEEK_DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

def main():
  day = int(input('Day: '))
  month = int(input('Month: '))
  year = int(input('Year: '))

  print()

  try:
    date = datetime.datetime(year=year, month=month, day=day)
    print(f'It is a {WEEK_DAYS[date.weekday()]}')
  except:
    print('Invalid Date.')

if __name__ == '__main__':
  main()