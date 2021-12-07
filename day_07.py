import math
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path + '/inputs/day_07.txt', 'r')
input = file.read().strip().split(',')

star1 = 0
star2 = 0

fuel_dict = {}

for align_position in range(0,400):
  fuel_counter = 0
  for crab_pos in input:
    diff = abs(int(crab_pos) - align_position)
    fuel_counter += diff
  fuel_dict[align_position] = fuel_counter

star1 = min(fuel_dict.values())

fuel_dict = {}

for align_position in range(0,500):
  fuel_counter = 0
  for crab_pos in input:
    diff = abs(int(crab_pos) - align_position)
    for n in range(1,diff+1):
      fuel_counter += n
  fuel_dict[align_position] = fuel_counter

star2 = min(fuel_dict.values())

print("star 1:", star1)
print("star 2:", star2)