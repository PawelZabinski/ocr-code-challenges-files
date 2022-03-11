# Classification

# This project asks a series of Yes/No questions in order to work out what type of phone the person owns.
# Pawel Zabinski

class Node:
  def __init__(self, type, data, yes=None, no=None):
    # Type may be 'Q' or 'A' ('Q' is for Question, 'A' is for Answer)
    self.type = type

    # Data is the question to be asked, or the name of the animal
    self.data = data
    
    self.yes = yes
    self.no = no

  def execute(self):
    if not self.type == 'Q': return
      
    answer = input(f'{self.data} [Yes/No]: ').lower()

    if answer in ('y', 'ye', 'yes'):
      return 'yes'
    elif answer in ('n', 'no', 'nope'):
      return 'no'
    else:
      return 'invalid'

master = Node(
  'Q', 
  'Is the phone brand a Chinese company?',
  yes=Node(
    'Q',
    'Does your phone have an official IP rating?',
    yes=Node(
      'Q',
      'Does your phone have a headphone jack?',
      yes=Node('A', 'Xiaomi Redmi Note 11 Series'),
      no=Node(
        'Q',
        'Does your phone support 8K video?',
        yes=Node('A', 'OnePlus 9 Pro'),
        no=Node('A', 'Huawei P50 Series')
      )
    ),
    no=Node(
      'Q',
      'Is your phone foldable?',
      yes=Node('A', 'Oppo Find N'),
      no=Node('A', 'OnePlus 9')
    )
  ),
  no=Node(
    'Q',
    'Is the phone foldable?',
    yes=Node(
      'Q',
      'Does your phone have "bending" glass',
      yes=Node(
        'Q',
        'Does your phone have an under-display camera?',
        yes=Node('A', 'Samsung Galaxy Z Fold 3'),
        no=Node('A', 'Samsung Galaxy Z Flip 3')
      ),
      no=Node('A', 'Microsoft Surface Duo 2')
    ),
    no=Node(
      'Q',
      'Is the phone using an in-house CPU for all its models?',
      yes=Node(
        'Q',
        'Is the phone brand known for its internet browser?',
        yes=Node('A', 'Google Pixel 6 Series'),
        no=Node('A', 'Apple iPhone 13 Series')
      ),
      no=Node('A', 'Samsung Galaxy S21 Series')
    )
  )
)

def main():
  print('Welcome to Akinator...for phones')
  print('Disclaimer: Only the newest phones are available in this data set\n')
  
  pointer = master
  
  while not pointer is None:
    # If the node is an answer, break out of the loop and display the result
    if pointer.type == 'A':
      print(f'Your phone is {pointer.data}')
      break
  
    # If the node is a question, execute it and change the pointer respectively
    result = pointer.execute()
  
    if result == 'yes':
      pointer = pointer.yes
    elif result == 'no':
      pointer = pointer.no

if __name__ == '__main__':
  main()