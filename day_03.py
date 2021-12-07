import math
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path + '/inputs/day_03.txt', 'r')
input = file.read().strip().split('\n')

star1 = 0
star2 = 0

gamma = ""
epsilon = ""

matrix = []
for i in input:
  l = list()
  for s in i:
    l.append(s)
  matrix.append(l)

def invert_binary_string(s):
  o = ""
  for c in s:
    if c == "0":
      o += "1"
    else:
      o += "0"
  return o

for n in range(0,len(matrix[0])):
  count_0 = 0
  count_1 = 0
  for i in matrix:
    if i[n] == "0":
      count_0 += 1
    else:
      count_1 += 1
  if count_0 >= count_1:
    gamma += "0"
  else:
    gamma += "1"
  epsilon = invert_binary_string(gamma)

star1 = int(gamma, 2) * int(epsilon, 2)

oxygen_rating = 0
co2_rating = 0

most_commons = []
least_commons = []
for n in range(0, len(matrix[0])):
  count_0 = 0
  count_1 = 0
  number_to_look_for = -1
  for i in matrix:
    if i[n] == "0":
      count_0 += 1
    else:
      count_1 += 1
  if count_0 >= count_1:
    number_to_look_for = 0
  else:
    number_to_look_for = 1
  for i in matrix:
    if i[n] == str(number_to_look_for):
      pass

print("star 1:", star1)
print("star 2:", star2)