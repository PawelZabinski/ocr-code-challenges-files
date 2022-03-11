from int_to_str import int_to_str

# Number Names

# Show how to spell out a number in English. You can use a pre-existing implementation or make your own, but you should support inputs up to at least one million (or the maximum value
# of your language’s default bounded integer type, if that’s less).


def main():
  integer = (int)(''.join(list(filter(lambda x: x not in ',_ ', input('Enter an integer: ')))))
  
  integer_str = ('negative ' if integer < 0 else '') + int_to_str(abs(integer))
  integer_str = " ".join([i.title() for i in integer_str.split(' ')])
  
  print(integer_str)

if __name__ == '__main__':
  main()