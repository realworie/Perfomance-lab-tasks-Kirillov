import math
import statistics
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

print(count_steps(nums, math.floor(statistics.median(nums))))
