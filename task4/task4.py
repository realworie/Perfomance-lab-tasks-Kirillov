import math
import sys

def count_steps(number_array, target_level):
    c = 0
    for number in number_array:
        c += abs(target_level - number)
    return c

filename = sys.argv[1]

nums = []

file = open(filename, "r")
for line in file:
    nums.append(int(line))
file.close()

average_round_down = math.floor(sum(nums) / len(nums))
average_round_up = average_round_down + 1

print(str(min(count_steps(nums, average_round_down), count_steps(nums, average_round_up))))
