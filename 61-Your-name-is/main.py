# Your name is...

# Have the programme ask for your name, age and form. Have it tell them the information back in the format:
# Your name is (blank), you are (blank) years old, and you are in form (blank).

def main():
  name = input('Enter your name > ')
  age = input('Enter your age > ')
  form = input('Enter your form > ')

  format = f'Your name is {name}, you are {age} years old, and you are in form {form}'

  print(format)

  # Store in external txt file
  with open('entries.txt', 'a') as file:
    file.write(format + '\n')

if __name__ == '__main__':
  main()