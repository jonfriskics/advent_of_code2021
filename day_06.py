import math
import os
from collections import Counter

dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path + '/inputs/day_06.txt', 'r')
input = file.read().strip().split(',')

star_input = [int(i) for i in input]

star1 = 0
star2 = 0

state_ = star_input

for day in range(0,80):
  new_state = []
  fish_to_add = 0
  for fish in state_:
    if fish > 0 and fish < 9:
      new_state.append(fish-1)
    elif fish == 0:
      new_state.append(6)
      fish_to_add += 1
  state_ = new_state
  for n in range(0,fish_to_add):
    state_.append(8)

star1 = len(state_)

state_ = star_input

for day in range(0,256):
  print(day)
  new_state = []
  fish_to_add = 0
  for fish in state_:
    if fish > 0 and fish < 9:
      new_state.append(fish-1)
    elif fish == 0:
      new_state.append(6)
      fish_to_add += 1
  state_ = new_state
  for n in range(0,fish_to_add):
    state_.append(8)
print(len(state_))

star_2 = len(state_)

print("star 1:", star1)
print("star 2:", star2)