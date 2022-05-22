import math
import statistics
import sys

filename = sys.argv[1]

nums = []

file = open(filename, "r")
for line in file:
    nums.append(int(line))
file.close()

counter = 0
median = int(statistics.median(nums))
for number in nums:
    counter += abs(median - number)

print(counter)
