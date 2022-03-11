import json
import random
import os

# Quiz Maker

# Make an application which takes various questions from a file, picked randomly, and puts together a quiz for students. Each quiz can be different and then reads a key to grade
# the quizzes.

QUESTIONS_COUNT = 5

def get_list(file):
  with open(file, 'r') as f:
    return json.loads(f.read())

def calculate_grade(correct_count):
  grades = ['F', 'E', 'D', 'C', 'B', 'A']
  return grades[min(5, correct_count)]

def clear_screen(): 
  os.system('clear')

questions = get_list(file='questions.json')
random.shuffle(questions)

total_correct = 0

for question in questions[0:QUESTIONS_COUNT]:
  title = question['text']
  correct_answer = question['correct_answer']
  options = [correct_answer, *question['incorrect_answers']]

  random.shuffle(options)
  
  print(title)

  for i, option in enumerate(options):
    print(f' - [{i}] {option}')

  selection = int(input('\nEnter a number: '))

  if options[selection] == correct_answer:
    total_correct += 1
    print('Your answer was correct')
  else:
    print("Your answer was incorrect, correct answer was '{correct_answer}'")

  input()
  clear_screen()

grade = calculate_grade(total_correct)

print(f'Thanks for taking the quiz, your result was {total_correct}/{QUESTIONS_COUNT}')
print(f'You have achieved a grade {grade}.')