from aocd import data, submit
from collections import deque
import numpy
""" with open('input.txt') as f:
    data = f.read() """
data = [[int(c) for c in line] for line in data.splitlines()]
sizes = []
basin = {}
def basinSearch(p):
    y, x = p
    #print(p)
    val = data[y][x]
    try:
        basin[p]
    except KeyError:
        if (val != 9):
            basin[p] = True
            count = 1
            count += basinSearch((y,x+1)) if x < len(data[y]) - 1 else 0
            count += basinSearch((y+1,x)) if y < len(data) - 1 else 0
            count += basinSearch((y,x-1)) if x > 0 else 0
            count += basinSearch((y-1,x)) if y > 0 else 0
            return(count)
    return 0
for y in range(len(data)):
    for x in range(len(data[y])):
        sizes.append(basinSearch((y,x)))    
sizes = sorted(sizes)
print(sizes[-3:], numpy.prod(sizes[-3:]))
submit(numpy.prod(sizes[-3:]))
