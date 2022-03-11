import random
import json
import os

# Arithmetic Test (Arithmetic Assassin)

# A primary school teacher wants a computer program to test the basic arithmetic skills of her students. Generate random questions (2 numbers only) consisting of addition,
# subtraction, multiplication and division.
# The system should ask the student’s name and then ask ten questions. The program should feed back if the answers are correct or not, and then generate a final score at
# the end.

#
# Question Manager is pretty self-explanatory, it manages the questions asked to the students
# It generates a random question from addition, subtraction, multiplication, and divison
#

RED = '\033[31m'
UNDERLINE = '\033[4m'
NORMAL = '\033[0m'

class QuestionManager:
  @classmethod
  def random(cls):
    questions = (cls.addition, cls.subtraction, cls.multiplication, cls.division)

    return random.choice(questions)()

  def addition():
    num_one = random.randint(1, 50)
    num_two = random.randint(1, 50)

    return (f'{num_one} + {num_two}', num_one + num_two)

  def subtraction():
    num_one = random.randint(1, 50)
    num_two = random.randint(1, 50)

    nums = (num_one, num_two)

    num_one = max(nums)
    num_two = min(nums)

    return (f'{num_one} - {num_two}', num_one - num_two)

  def multiplication():
    num_one = random.randint(1, 12)
    num_two = random.randint(1, 12)

    return (f'{num_one} x {num_two}', num_one * num_two)

  def division():
    num_one = random.randint(1, 12)
    num_two = random.randint(1, 12)

    return (f'{num_one * num_two} ÷ {num_two}', num_one)

#
# Console Manager is pretty self-explanatory too, it manages the content printed onto the console
# It contains helper functions to display questions, ask for input, display special messages etc.
#

class ConsoleManager:
  def display_question(question):
    user_input = input(f'{question} = ')

    try:
      return int(user_input)
    except ValueError:
      return ConsoleManager.display_question(question)

  def display_scores(scores):
    for score in scores:
      print(f' - {score["student_name"]} {score["score"]}/10')

  def display_system_message(message):
    print(f'{RED}(System){NORMAL} {message}')

  def display_header():
    print('<-----[ Arithmetic Assassin ]----->', end='\n'*2)

  def clear_screen():
    os.system('clear')

  def press_enter_to_continue():
    input('Press "Enter" to continue. ')

  def name_input():
    name = input('What is your name? ')

    if len(name):
      return name

    return ConsoleManager.name_input()

  def status_input():
    # Checks if the user is a teacher or student
    status = input('Are you a Teacher or a Student? ').lower()

    if status in ('teacher', 'student'): 
      return status

    return ConsoleManager.status_input()

  def class_name_input():
    # Validates the class name entered
    class_name = input('What is your class\'s name? ')

    if len(list(filter(lambda x: x['class_name'] == class_name, DataManager.fetch_classes()))):
      return class_name

    return ConsoleManager.class_name_input()

#
# DataManager manages the flow of data in the program, and the persistant storage
#
    
class DataManager:
  def fetch_classes():
    with open('db.json', 'r') as f:
      json_data = f.read()
      result = json.loads(json_data)

      return result

  def fetch_scores(class_name):
    return [i for i in DataManager.fetch_classes() if i['class_name'] == class_name][0]['scores']

  def update_classes(classes):
    with open('db.json', 'w') as f:
      result = json.dumps(classes)
      f.write(result)

  def append_result(class_name, result):
    classes = map(lambda x: { 
      'class_name': x['class_name'], 
      'scores': [*x['scores'], result] 
    } if x['class_name'] == class_name else x, DataManager.fetch_classes())

    DataManager.update_classes(list(classes))
    
#
# UserManager is responsible for managing the program logic for the individual user
#
class UserManager:
  @classmethod
  def login(cls):
    status = ConsoleManager.status_input()

    if status == 'teacher':
      return cls.teacher
    elif status == 'student':
      return cls.student

    raise ValueError(f'Invalid status type "{status}"')
      
  def teacher():
    ConsoleManager.display_system_message(f'You are signed in as a {UNDERLINE}Teacher{NORMAL}\n')
    class_name = ConsoleManager.class_name_input()

    ConsoleManager.clear_screen()
    ConsoleManager.display_header()
    
    ConsoleManager.display_system_message(f'You are signed in to "{class_name}"\n')

    ConsoleManager.display_scores(DataManager.fetch_scores(class_name))

    

  def student():
    ConsoleManager.display_system_message(f'You are signed in as a {UNDERLINE}Student{NORMAL}\n')

    student_name = ConsoleManager.name_input()
    class_name = ConsoleManager.class_name_input()

    ConsoleManager.clear_screen()
    ConsoleManager.display_header()
    
    ConsoleManager.display_system_message(f'You are signed in to "{class_name}"\n')

    # Quiz
    correct_answers = 0

    for _ in range(10):
      question = QuestionManager.random()

      result = ConsoleManager.display_question(question[0])
      is_correct = result == question[1]

      if is_correct:
        correct_answers += 1

    print()

    # Display result
    ConsoleManager.display_system_message(f'Quiz completed, you got {correct_answers}/10 correct answers')

    DataManager.append_result(class_name, { "student_name": student_name, "score": correct_answers })
      
#
# Main Function - This scope is where the program logic will be executed
#

def main():
  ConsoleManager.clear_screen()
  
  ConsoleManager.display_header()
  start = UserManager.login()

  ConsoleManager.clear_screen()

  ConsoleManager.display_header()
  start()

if __name__ == '__main__':
  main()