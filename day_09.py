import math
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path + '/inputs/day_09.txt', 'r')
input = file.read().strip().split('\n')

# input = [int(i) for i in input]

star1 = 0
star2 = 0

def print_matrix(m):
  for l in range(len(m)):
    print(m[l])

matrix = []

for y in range(0,len(input)):
  matrix.append([])
  for x in range(0,len(input[0])):
    matrix[y].append(0)

for y, i in enumerate(input):
  chars = [char for char in i]
  for x, c in enumerate(chars):
    matrix[y][x] = c

# print_matrix(matrix)

low_points = []

row_max = len(matrix)-1
col_max = len(matrix[0])-1

for row in range(0, len(matrix)):
  for col in range(0, len(matrix[0])):
    if row == 0 and col == 0:
      right_one = matrix[row][col+1]
      down_one = matrix[row+1][col]
      if (
        matrix[row][col] < right_one and
        matrix[row][col] < down_one
      ):
        low_points.append(matrix[row][col])
    elif row == 0 and col == col_max:
      left_one = matrix[row][col-1]
      down_one = matrix[row+1][col]
      if (
        matrix[row][col] < left_one and
        matrix[row][col] < down_one
      ):
        low_points.append(matrix[row][col])
    elif row == row_max and col == 0:
      top_one = matrix[row-1][col]
      right_one = matrix[row][col+1]
      if (
        matrix[row][col] < top_one and
        matrix[row][col] < right_one
      ):
        low_points.append(matrix[row][col])
    elif row == row_max and col == col_max:
      top_one = matrix[row-1][col]
      left_one = matrix[row][col-1]
      if (
        matrix[row][col] < top_one and
        matrix[row][col] < left_one
      ):
        low_points.append(matrix[row][col])
    elif row == 0:
      left_one = matrix[row][col-1]
      down_one = matrix[row+1][col]
      right_one = matrix[row][col+1]
      if (
        matrix[row][col] < left_one and
        matrix[row][col] < down_one and
        matrix[row][col] < right_one
      ):
        low_points.append(matrix[row][col])
    elif row == row_max:
      left_one = matrix[row][col-1]
      top_one = matrix[row-1][col]
      right_one = matrix[row][col+1]
      if (
        matrix[row][col] < left_one and
        matrix[row][col] < top_one and
        matrix[row][col] < right_one
      ):
        low_points.append(matrix[row][col])
    elif col == 0:
      top_one = matrix[row-1][col]
      right_one = matrix[row][col+1]
      down_one = matrix[row+1][col]
      if (
        matrix[row][col] < top_one and
        matrix[row][col] < right_one and
        matrix[row][col] < down_one
      ):
        low_points.append(matrix[row][col])
    elif col == col_max:
      top_one = matrix[row-1][col]
      left_one = matrix[row][col-1]
      down_one = matrix[row+1][col]
      if (
        matrix[row][col] < top_one and
        matrix[row][col] < left_one and
        matrix[row][col] < down_one
      ):
        low_points.append(matrix[row][col])
    else:
      top_one = matrix[row-1][col]
      right_one = matrix[row][col+1]
      down_one = matrix[row+1][col]
      left_one = matrix[row][col-1]
      if (
        matrix[row][col] < top_one and
        matrix[row][col] < right_one and
        matrix[row][col] < down_one and
        matrix[row][col] < left_one
      ):
        low_points.append(matrix[row][col])

for p in low_points:
  star1 += int(p)+1

print("star 1:", star1)
print("star 2:", star2)