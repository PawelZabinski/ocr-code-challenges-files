
# Credit Card Validator

# Takes in a credit card number from a common credit card vendor (Visa, MasterCard, American Express, Discoverer) and validates it to make sure that it is a valid number
# (look into how credit cards use a checksum).

def validate_card(card_number):
  numbers = [int(i) for i in card_number]

  for i in range(len(numbers)):
    if i & 1: continue

    new_number = numbers[i] * 2

    if new_number >= 10:
      new_number = sum([int(i) for i in str(new_number)])
  
    numbers[i] = new_number
  
  digit_sum = sum(numbers)

  return digit_sum % 10 == 0

def main():
  card_number = input('Enter Card Number: ')

  if validate_card(card_number):
    print('Your card is valid')
  else:
    print('Your card is invalid')

if __name__ == '__main__':
  main()