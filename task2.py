import sys
import math
import re

_threshold = 0.0000000000001

def float_equals(a, b):
    if abs(a - b) < _threshold:
        return True
    else:
        return False

def distance(x_1, y_1, x_2, y_2):
    return math.sqrt((x_2 - x_1)**2 + (y_2 - y_1)**2)


circle_file = sys.argv[1]
points_file = sys.argv[2]

file = open(circle_file, "r")
match = re.findall("^(-?\d+[\.\,]?\d*) (-?\d+[\.\,]?\d*)\n(-?\d+[\.\,]?\d*)", file.read())
circle_x = float(match[0][0])
circle_y = float(match[0][1])
circle_r = float(match[0][2])
file.close()

file = open(points_file, "r")
points = re.findall("(-?\d+[\.\,]?\d*) (-?\d+[\.\,]?\d*)", file.read())
file.close()

for point in points:
    x = float(point[0])
    y = float(point[1])
    d = distance(circle_x, circle_y, x, y)
    if float_equals(d, circle_r):
        print(0)
    elif d < circle_r:
        print(1)
    else:
        print(2)