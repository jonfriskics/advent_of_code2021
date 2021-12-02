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
  if split[0] == "forward":
    horizontal_position += int(split[1])
  elif split[0] == "up":
    depth -= int(split[1])
  elif split[0] == "down":
    depth += int(split[1])

star1 = horizontal_position * depth

horizontal_position = 0
depth = 0
aim = 0

for i in input:
  split = i.split(" ")
  if split[0] == "forward":
    horizontal_position += int(split[1])
    depth = depth + aim * int(split[1])
  elif split[0] == "up":
    aim -= int(split[1])
  elif split[0] == "down":
    aim += int(split[1])

star2 = horizontal_position * depth

print("star 1:", star1)
print("star 2:", star2)