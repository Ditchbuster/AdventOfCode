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
p = np.zeros((10, 2), dtype=int)
vist[(0, 0)] = 1
for l in data:
    d, c = l.split()
    c = int(c)
    for i in range(c):
        if d == "R":
            p[0] = [p[0][0] + 1, p[0][1]]
        elif d == "U":
            p[0] = [p[0][0], p[0][1] + 1]
        elif d == "L":
            p[0] = [p[0][0] - 1, p[0][1]]
        elif d == "D":
            p[0] = [p[0][0], p[0][1] - 1]
        for i in range(1, len(p)):
            if (
                p[i][0] - p[i - 1][0] > 1
                or p[i][0] - p[i - 1][0] < -1
                or p[i][1] - p[i - 1][1] > 1
                or p[i][1] - p[i - 1][1] < -1
            ):
                if p[i][0] == p[i - 1][0]:
                    if p[i][1] > p[i - 1][1]:
                        p[i][1] -= 1
                    else:
                        p[i][1] += 1
                elif p[i][1] == p[i - 1][1]:
                    if p[i][0] > p[i - 1][0]:
                        p[i][0] -= 1
                    else:
                        p[i][0] += 1
                else:
                    if p[i][1] > p[i - 1][1]:
                        p[i][1] -= 1
                    else:
                        p[i][1] += 1
                    if p[i][0] > p[i - 1][0]:
                        p[i][0] -= 1
                    else:
                        p[i][0] += 1
                if i == len(p) - 1:
                    vist[(p[i][0], p[i][1])] += 1
            else:
                break
print(len(vist.keys()))
print(vist.keys())
