import enum
import random

# Printer problems

# A printing shop runs 16 batches (jobs) every week and each batch requires a sheet of
# special colour-proofing sheet of size A5.
# Every Monday morning, the foreman opens a new envelope, containing a large sheet of
# the special sheet with size A1.
# He proceeds to cut it in half, thus getting two sheets of size A2. Then he cuts one of them
# in half to get two sheets of size A3 and so on until he obtains the A5-size sheet needed for
# the first batch of the week.
# All the unused sheets are placed back in the envelope.
# At the beginning of each subsequent batch, he takes from the envelope one sheet of sheet
# at random. If it is of size A5, he uses it. If it is larger, he repeats the ‘cut-in-half’ procedure until
# he has what he needs and any remaining sheets are always placed back in the envelope.

class Colour(enum.Enum):
  green = '\x1b[0;30;42m'
  blue = '\x1b[0;30;44m'
  white = '\x1b[0m'

def _flat(array):
  # For each value of array, if the value is a list, recursively call the function and yield the elements, if not simply yield the value
  for element in array:
    if type(element) is list:
      yield from _flat(element)
    else:
      yield element

# Wrapper for flat function, returns using the list data type.
def flat(array):
  return [i for i in _flat(array)]

def cutSheet(size):
  if size >= 5: return 5

  return [cutSheet(size + 1), size + 1]

def show(msg, colour=None):
  print(f'{colour.value if colour else ""}{msg}{Colour.white.value}')
  input()
  
def showEnvelope(envelope):
  formattedEnvelope = [f'A{i}' for i in envelope]
  show(f"Envelope content: {', '.join(formattedEnvelope) if len(formattedEnvelope) else 'Emptiness..'}.", Colour.blue)

def stimulateWeek():
  jobs = 0
  envelope = [1]
  
  # Monday
  show('[ MONDAY ] - You open the envelope and obtain the A1 sheet of paper.')

  showEnvelope(envelope)
  
  show('You proceed to cut it repeatedly in half until you reach an A5 sheet.')
  envelope = flat(cutSheet(1))
  
  showEnvelope(envelope)
  
  show('You take the first batch of A5 sheet required for the printing job.')

  jobs += 1
  envelope.remove(5)

  showEnvelope(envelope)

  show('All the unused sheets were sealed back into the evelope.')

  while jobs != 16:
    show(f'Beginning of batch No.{jobs + 1}: ', Colour.green)
    
    randomSheet = envelope[random.randrange(len(envelope))]
    envelope.remove(randomSheet)

    show(f'A{randomSheet} has been selected from the envelope.')

    if randomSheet != 5:
      newSheets = flat(cutSheet(randomSheet))

      show(f'A{randomSheet} has been cut into: {", ".join([f"A{i}" for i in newSheets])}.')
      
      envelope += newSheets

      envelope.remove(5)

      show(f'A5 has been removed from the envelope for the printing job and other sheets were inserted back.')
    
    showEnvelope(envelope)

    jobs += 1

  show('All 16 batches have been completed.')

def main():
  while True:
    stimulateWeek()

    if input('Stimulate another week? ').lower() not in ('y', 'ye', 'yes', 'yeah'):
      break

    print('\n'*25)

if __name__ == '__main__':
  main()