import math
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path + '/inputs/day_01.txt', 'r')
input = file.read().strip().split('\n')

star_input = [int(i) for i in input]

star1_times = 0

for n, i in enumerate(star_input):
  if i >= 1:
    if star_input[n] > star_input[n-1]:
      star1_times += 1

star2_times = 0
sliding_windows = []

for n, i in enumerate(star_input):
  if i >= 2:
    sliding_windows.append(star_input[n] + star_input[n-1] + star_input[n-2])

for n, i in enumerate(sliding_windows):
  if i>= 1:
    if sliding_windows[n] > sliding_windows[n-1]:
      star2_times += 1

print("star 1:", star1_times)
print("star 2:", star2_times)
