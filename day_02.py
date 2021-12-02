import math
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path + '/inputs/day_02.txt', 'r')
input = file.read().strip().split('\n')

star1 = 0
star2 = 0

horizontal_position = 0
depth = 0

for i in input:
  split = i.split(" ")
  direction = split[0]
  value = int(split[1])

  if direction == "forward":
    horizontal_position += value
  elif direction == "up":
    depth -= value
  elif direction == "down":
    depth += value

star1 = horizontal_position * depth

horizontal_position = 0
depth = 0
aim = 0

for i in input:
  split = i.split(" ")
  direction = split[0]
  value = int(split[1])

  if direction == "forward":
    horizontal_position += value
    depth = depth + aim * value
  elif direction == "up":
    aim -= value
  elif direction == "down":
    aim += value

star2 = horizontal_position * depth

print("star 1:", star1)
print("star 2:", star2)