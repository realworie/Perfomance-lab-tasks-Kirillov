import itertools
import sys

n = int(sys.argv[1])
m = int(sys.argv[2])

loop_array = itertools.cycle(range(1, n + 1, 1))

path = "1"
c = 1

for entry in loop_array:
    if c == m:
        if entry == 1:
            break
        path += str(entry)
        c = 1
    c += 1

print(path)