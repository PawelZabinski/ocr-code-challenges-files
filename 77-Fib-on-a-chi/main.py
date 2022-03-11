import itertools

# Fib on a chi

# The Fibonacci sequence is defined by the recurrence relation:
# Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

def fibonacciFind(x):
  if x == 1: return 0
  elif x == 2: return 2
    
  a = 1
  b = 1
  c = a + b

  for i in itertools.count(3):
    a, b = b, c
    c = a + b
    
    if c >= x:
      return i
  
def main():
  index = fibonacciFind(10 ** (1_000 - 1)) + 1
  print(index)

if __name__ == '__main__':
  main()