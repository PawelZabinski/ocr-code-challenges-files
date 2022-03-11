# Spam filter

# Take a list of dishes from a menu and add “spam” to them. See https://en.wikipedia.org/wiki/Spam_(Monty_Python).

def main():
  try:
    dishCount = int(input('Enter number of dishes in menu > '))

    dishes = [input(f'Enter Dish No.{i + 1} > ') for i in range(dishCount)]
    dishes = [f'{dish} spam' for dish in dishes]

    for dish in dishes:
      print(dish)
  except:
    print('Invalid dish count. Please enter a positive integer')

if __name__ == '__main__':
  main()