import math
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path + '/inputs/day_08.txt', 'r')
input = file.read().strip().split('\n')

star1 = 0
star2 = 0

for i in input:
  left_side = []
  right_side = []

  left_side.append(i.split(" | ")[0])
  input_signals = left_side[0].split(" ")

  digits = dict()
  for n in range(0,10):
    digits[n] = ""

  bars = dict()
  bars["top_bar"] = ""
  bars["top_left_bar"] = ""
  bars["top_right_bar"] = ""
  bars["middle_bar"] = ""
  bars["bottom_left_bar"] = ""
  bars["bottom_right_bar"] = ""
  bars["bottom_bar"] = ""

  input_signals = sorted(input_signals, key=len)

  # get 1, 4, 7, 8
  for s in input_signals:
    if len(s) == 2:
      digits[1] = s
    elif len(s) == 4:
      digits[4] = s
    elif len(s) == 3:
      digits[7] = s
    elif len(s) == 7:
      digits[8] = s

  # top bar is letters in 7 minus letters in 1
  bars["top_bar"] = (set(digits[7]) - set(digits[1])).pop()

  # get 0 - contains all chars of 1 and 7, only 3 chars of 4
  for s in input_signals:
    if len(s) == 6:
      if \
        len(set(s).intersection(set(digits[1]))) == 2 and \
        len(set(s).intersection(set(digits[7]))) == 3 and \
        len(set(s).intersection(set(digits[4]))) == 3:
        digits[0] = s

  # what's not used in 0?  That's the middle
  bars["middle_bar"] = (set(digits[8]).difference(set(digits[0]))).pop()

  # 4 minus middle letter minus two letters in 1 = top left
  bars["top_left_bar"] = set(digits[4]).difference(set(bars["middle_bar"])).difference(set(digits[1])).pop()

  # get 6 - contains everything except 1 letter in 1
  for s in input_signals:
    if len(s) == 6:
      if(s != digits[0]):
        if len(set(s).difference(set(digits[1]))) == 5:
          digits[6] = s

  # top right is letter from 1 that's not in 6
  bars["top_right_bar"] = (set(digits[1]).difference(set(digits[6]))).pop()

  # bottom right is letter from 1 that's not top right
  bars["bottom_right_bar"] = (set(digits[1]).difference(set(bars["top_right_bar"]))).pop()

  # get 9 - other 6 digit input that's not 0 or 6
  for s in input_signals:
    if len(s) == 6:
      if s != digits[0] and s != digits[6]:
        digits[9] = s

  # bottom left is letter that's in 8 but not 9
  bars["bottom_left_bar"] = (set(digits[8]).difference(set(digits[9]))).pop()

  # bottom bar is only letter not used
  bars["bottom_bar"] = (set(digits[8]).difference(set(bars.values()))).pop()

  # get 5 - which is 9 minus top right
  temp_set = set(digits[9])
  temp_set.remove(bars["top_right_bar"])
  for s in input_signals:
    if len(s) == 5:
      if len(set(s).difference(temp_set)) == 0:
        digits[5] = s

  # get 3 - contains all chars of 1 and 7, exactly 5 chars of 9
  for s in input_signals:
    if len(s) == 5:
      if \
        len(set(s).intersection(set(digits[1]))) == 2 and \
        len(set(s).intersection(set(digits[7]))) == 3 and \
        len(set(s).intersection(set(digits[9]))) == 5:
        digits[3] = s

  # get 2 - the other 5 char number that's not 5 or 3
  for s in input_signals:
    if len(s) == 5:
      if s != digits[5] and s != digits[3]:
        digits[2] = s

  right_side.append(i.split(" | ")[1])
  output_signals = right_side[0].split(" ")

  # as long as we're here, add up the quantities of these numbers for star 1
  for signal in output_signals:
    if len(signal) == 2 or \
      len(signal) == 3 or \
      len(signal) == 4 or \
      len(signal) == 7:
      star1 += 1

  output_value = ""
  for rs in output_signals:
    for k,v in digits.items():
      if set(rs).issubset(set(v)) and \
        set(rs).issuperset(set(v)):
        output_value += str(k)

  star2 += int(output_value)

print("star 1:", star1)
print("star 2:", star2)