import math

def all_same(list):
    return list.count(list[0]) == len(list)

filename = sys.argv[1]

nums = []

file = open(filename, "r")
for line in file:
    nums.append(int(line))
file.close()

sum = 0
for number in nums:
    sum += number

average_c = math.ceil(sum / len(nums))
average_f = math.floor(sum / len(nums))

nums_c = nums.copy()
nums_f = nums.copy()
length = len(nums)
counter_c = 0
counter_f = 0

while not all_same(nums_c):
    for i in range(length):
        if nums_c[i] == average_c:
            continue
        counter_c += 1
        if nums_c[i] > average_c:
            nums_c[i] -= 1
        else:
            nums_c[i] += 1

while not all_same(nums_f):
    for i in range(length):
        if nums_f[i] == average_f:
            continue
        counter_f += 1
        if nums_f[i] > average_f:
            nums_f[i] -= 1
        else:
            nums_f[i] += 1

print(str(min(counter_c, counter_f)))
