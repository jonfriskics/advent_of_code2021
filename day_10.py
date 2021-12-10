import math
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path + '/inputs/day_10.txt', 'r')
input = file.read().strip().split('\n')

star1 = 0
star2 = 0

bad_chars = []
incomplete_lines = []
closing_strings = []

for line in input:
  broke_line = False
  opens = []
  open_count = 0
  closed_count = 0
  for c in line:
    if c in set(["[","(","{","<"]):
      opens.append(c)
    else:
      if c == "]" and opens[-1] == "[":
        opens.pop()
      elif c == "}" and opens[-1] == "{":
        opens.pop()
      elif c == ")" and opens[-1] == "(":
        opens.pop()
      elif c == ">" and opens[-1] == "<":
        opens.pop()
      else:
        bad_chars.append(c)
        broke_line = True
        break
  if broke_line == False:
    incomplete_lines.append(line)

for c in bad_chars:
  if c == ")":
    star1 += 3
  elif c == "]":
    star1 += 57
  elif c == "}":
    star1 += 1197
  elif c == ">":
    star1 += 25137

for line in incomplete_lines:
  opens = []
  chars_added = ""
  for c in line:
    if c in set(["[","(","{","<"]):
      opens.append(c)
    else:
      if c == "]" and opens[-1] == "[":
        opens.pop()
      elif c == "}" and opens[-1] == "{":
        opens.pop()
      elif c == ")" and opens[-1] == "(":
        opens.pop()
      elif c == ">" and opens[-1] == "<":
        opens.pop()

  opens.reverse()
  closing_string = ""

  for c in opens:
    if c == "[":
      closing_string += "]"
    elif c == "{":
      closing_string += "}"
    elif c == "(":
      closing_string += ")"
    elif c == "<":
      closing_string += ">"
  
  closing_strings.append(closing_string)

score_vals = []

for chars in closing_strings:
  score = 0
  for c in chars:
    score *= 5
    if c == "]":
      score += 2
    elif c == ")":
      score += 1
    elif c == "}":
      score += 3
    elif c == ">":
      score += 4
  score_vals.append(score)

score_vals.sort()
star2 = score_vals[(len(score_vals)-1)/2]

print("star 1:", star1)
print("star 2:", star2)