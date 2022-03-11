# Travel club

# A group of people are member of a travel club. 
# The group shares expenses equally but it is not practical to share every expense as they happen, so all expenses are collated (such as taxis, train tickets etc) after the trip 
# The member cost is shared to within 1% between the group. 
# Create a programme that computes the net cost from a list of expenses and works out the minimum amount of money that must change hands in order for everybody to have paid the same amount (within 1%).

def recursiveInput(msg, until=''):
  while True:  
    string = input(msg)

    if string == until:
      print (f"\033[A{' '*len(msg + string)}\033[A")
      break
      
    yield string

def main():
  memberNames = [m for m in recursiveInput('Name of group member > ')]

  print()
  
  members = { m: float(input(f"{m}'s money £")) for m in memberNames }

  print()
  
  expenses = [float(e) for e in recursiveInput('Enter cost of an expense > ')]
  totalCost = sum(expenses)

  print()

  # Verifies that the group of people can afford all the expenses
  if totalCost > sum(members.values()):
    print("Total cost of expenses is too high, the group of people can't afford to pay for it")
    return
    
  costPerMember = totalCost / len(members)

  history = []
  moneyToChangeHands = 0

  for name, money in members.items():
    if (missingMoney := costPerMember - money) > 0:
      moneyToChangeHands += missingMoney

      history.append(f'£{missingMoney:.02f} has to be given to {name}')

  if moneyToChangeHands:
    print(f'A minimum of £{moneyToChangeHands:.02f} must change hands in order for everyone to have paid the same amount (of £{costPerMember:.02f}).')

    print('\nHistory:')

    for h in history:
      print(h)
  else:
    print('No money needs to change hands for everyone to have paid the same amount for expenses.')

if __name__ == "__main__":
  main()