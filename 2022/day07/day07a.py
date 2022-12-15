import math
import logging
from collections import defaultdict


def sized(dirname):
    # print(dirname)
    if len(dir[dirname]) != 0:
        total = 0
        for d in dir[dirname]:
            total += sized(d)
        size[dirname] += total
    return size[dirname]


logging.basicConfig(level=logging.DEBUG)
logging.debug("Open file")
with open("input.txt") as f:
    data = f.read()
data = data.splitlines()
# logging.info(data)
dir = defaultdict(list)
size = defaultdict(int)
path = list()
for l in data:
    print(l)
    l = l.split()
    if l[0] == "$":
        if l[1] == "cd":
            if l[2] == "/":
                path.clear()
                path.append("/")
            elif l[2] == "..":
                path.pop()
            else:
                path.append(l[2])
        elif l[1] == "ls":
            continue
    elif l[0] == "dir":
        dir["".join(path)].append("".join(path) + l[1])
    else:
        size["".join(path)] += int(l[0])
print(dir)
print(size)
print(sized("/"))
print(size)
print(sum([x for x in size.values() if x <= 100000]))

