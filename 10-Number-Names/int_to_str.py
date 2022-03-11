def int_to_str(integer):
  below_20 = [
    'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen'
  ]

  below_100_tens = [
    'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety'
  ]

  above_100 = {
    100: 'hundred', 1_000: 'thousand', 1_000_000: 'million', 1_000_000_000: 'billion', 1_000_000_000_000: 'trillion'
  }

  if integer < 20:
    return below_20[integer]
    
  if integer < 100:
    first = below_100_tens[integer // 10 - 2]
    second = '-' + below_20[integer % 10] if integer % 10 != 0 else ''

    return first + second

  pivot = max([key for key in above_100.keys() if key <= integer])

  return f'{int_to_str(integer // pivot)} {above_100[pivot]}{" " + int_to_str(integer % pivot) if integer % pivot else ""}'
  