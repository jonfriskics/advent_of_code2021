import math
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path + '/inputs/day_13.txt', 'r')
input = file.read().strip().split('\n\n')

# input = [int(i) for i in input]

star1 = 0
star2 = 0

def print_matrix(m):
  for l in range(len(m)):
    print(m[l])

coordinates = input[0].split('\n')

instructions = []
for inst in input[1].split('\n'):
  instruction = inst.split('fold along ')[1]
  instructions.append(instruction)

max_x = 0
max_y = 0
for c in coordinates:
  x = int(c.split(',')[0])
  y = int(c.split(',')[1])
  if(int(x) > max_x):
    max_x = x
  if(int(y) > max_y):
    max_y = y

matrix = []

for y in range(0,max_y+1):
  matrix.append([])
  for x in range(0,max_x+1):
    matrix[y].append('.')

for c in coordinates:
  col = int(c.split(',')[0])
  row = int(c.split(',')[1])
  matrix[row][col] = "#"



count = 0
for instruction in instructions:
  # uncomment for star 1
  #if(count == 1):
  #  break
  fold_direction = instruction.split('=')[0]
  fold_amount = int(instruction.split('=')[1])
  if(fold_direction == 'y'):
    for row in range(fold_amount+1, max_y+1):
      for col in range(0,max_x+1):
        offset = row - fold_amount
        if matrix[row][col] == '#':
          matrix[fold_amount-offset][col] = '#'
          matrix[row][col] = ' '
  elif(fold_direction == 'x'):
    for row in range(0, max_y+1):
      for col in range(fold_amount,max_x+1):
        offset = col - fold_amount
        if matrix[row][col] == '#':
          matrix[row][fold_amount-offset] = '#'
          matrix[row][col] = ' '
  count += 1

final_coords = []
for row in range(0, len(matrix)):
  for col in range(0, len(matrix[0])):
    if matrix[row][col] == '#':
      final_coords.append((row,col))
      star1 += 1

new_matrix = []
for row in range(0,6):
  new_matrix.append([])
  for col in range(0,40):
    new_matrix[row].append('-')

for row in range(0, 6):
  for col in range(0,40):
    new_matrix[row][col] = matrix[row][col]
    if matrix[row][col] == '.':
      new_matrix[row][col] = ' '

print("star 1:", star1)
print("star 2: see matrix printout")
print_matrix(new_matrix)