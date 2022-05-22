import math
import sys

filename = sys.argv[1]

nums = []

file = open(filename, "r")
for line in file:
    nums.append(int(line))
file.close()

average_round_down = math.floor(sum(nums) / len(nums))
average_round_up = average_round_down + 1

length = len(nums)
counter_c = 0
counter_f = 0

for number in nums:
    if number < average_round_down:
        counter_f += average_round_down - number
        counter_c += average_round_down - number + 1
    elif number > average_round_up:
        counter_c += number - average_round_up
        counter_f += number - average_round_up + 1
    elif number == average_round_down:
        counter_c += 1
    elif number == average_round_up:
        counter_f += 1

print(str(min(counter_c, counter_f)))
