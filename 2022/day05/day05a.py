import math
import logging
from collections import defaultdict

logging.basicConfig(level=logging.DEBUG)
logging.debug("Open file")
with open("input.txt") as f:
    data = f.read()
data = data.splitlines()
# logging.info(data)
stacks = defaultdict(list)
for k, l in enumerate(data):
    if l[1].isnumeric():
        start = k + 2
        break
    for i, c in enumerate(l[1::4]):
        if c.isalpha():
            stacks[i].append(c)
logging.debug(stacks)

for l in data[start:]:
    l = l.split()
    n = int(l[1])
    f = int(l[3]) - 1
    t = int(l[5]) - 1
    i = stacks[f][:n]
    for ic in i:
        stacks[t].insert(0, ic)
    stacks[f] = stacks[f][n:]
    logging.debug(stacks)
out = ""
for i in range(len(stacks)):
    out += stacks[i][0]
print(out)
