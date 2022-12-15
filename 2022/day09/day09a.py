import numpy as np
import logging
from collections import defaultdict

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s:\n%(message)s")
logging.debug("Open file")
with open("input.txt") as f:
    data = f.read()
data = data.splitlines()
# logging.info(data)
# data = np.array([[int(x) for x in l] for l in data])
vist = defaultdict(int)
h = [0, 0]
hl = [0, 0]
t = [0, 0]
vist[(0, 0)] = 1
for l in data:
    d, c = l.split()
    c = int(c)
    for i in range(c):
        hl = h
        if d == "R":
            h = [h[0] + 1, h[1]]
        elif d == "U":
            h = [h[0], h[1] + 1]
        elif d == "L":
            h = [h[0] - 1, h[1]]
        elif d == "D":
            h = [h[0], h[1] - 1]
        if t[0] - h[0] > 1 or t[0] - h[0] < -1 or t[1] - h[1] > 1 or t[1] - h[1] < -1:
            t = [hl[0], hl[1]]
            vist[(t[0], t[1])] += 1
print(len(vist.keys()))
