import math
import os
import time
import numpy as np

dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path + '/inputs/day_05.txt', 'r')
input = file.read().strip().split('\n')

star1 = 0

max_x = 0
max_y = 0

def slope(x1, y1, x2, y2):
  return int((y2 - y1) / (x2 - x1))

def print_matrix(m):
  for l in range(len(m)):
    print(m[l])

lines_arr = []

for i in input:
  lines = {}
  lines["x1"] = int(i.strip().split(" -> ")[0].split(',')[0])
  if lines["x1"] >= max_x:
    max_x = lines["x1"]

  lines["x2"] = int(i.strip().split(" -> ")[1].split(',')[0])
  if lines["x2"] >= max_x:
    max_x = lines["x2"]

  lines["y1"] = int(i.strip().split(" -> ")[0].split(',')[1])
  if lines["y1"] >= max_y:
    max_y = lines["y1"]

  lines["y2"] = int(i.strip().split(" -> ")[1].split(',')[1])
  if lines["y2"] >= max_y:
    max_y = lines["y2"]

  lines_arr.append(lines)

matrix = []
for x in range(0,int(max_x)+2):
  matrix.append([])
  for y in range(0,int(max_y)+2):
    matrix[x].append(0)

for line in lines_arr:
  x1 = int(line["x1"])
  x2 = int(line["x2"])
  y1 = int(line["y1"])
  y2 = int(line["y2"])

  direction = ""
  if x1 == x2:
    direction = "vertical"
  elif y1 == y2:
    direction = "horizontal"
  elif slope(x1,y1,x2,y2) == 1 or slope(x1,y1,x2,y2) == -1:
    direction = "diagonal"

  if direction == "horizontal":
    if(x1 > x2):
      for n in range(x2, x1+1):
        matrix[y1][n] += 1
    elif(x1 < x2):
      for n in range(x1, x2+1):
        matrix[y1][n] += 1
  elif direction == "vertical":
    if(y1 > y2):
      for n in range(y2, y1+1):
        matrix[n][x2] += 1
    elif(y1 < y2):
      for n in range(y1, y2+1):
        matrix[n][x2] += 1
  elif direction == "diagonal":
    # diagonal line
    pass
  else:
    # non-straight lines
    pass

count_above_1 = 0
for i in range(len(matrix)):
  for j in range(len(matrix[i])):
    if matrix[i][j] > 1:
      count_above_1 += 1

star1 = count_above_1
star2 = 0

print("star 1:", star1)
print("star 2:", star2)