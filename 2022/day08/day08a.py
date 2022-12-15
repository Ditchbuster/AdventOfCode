import numpy as np
import logging
from collections import defaultdict

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s:\n%(message)s")
logging.debug("Open file")
with open("input.txt") as f:
    data = f.read()
data = data.splitlines()
# logging.info(data)
data = np.array([[int(x) for x in l] for l in data])
logging.debug(data)
vis = np.zeros(data.shape, dtype=int)
# check from left
for ri, rv in enumerate(data):
    rmax = -1
    for ci, cv in enumerate(rv):
        if cv > rmax:
            rmax = cv
            vis[ri][ci] = 1
# check from top
for ci in range(data.shape[1]):
    cmax = -1
    for ri, rv in enumerate(data[:, ci]):
        if rv > cmax:
            cmax = rv
            vis[ri, ci] = 1
# check from bottom
for ci in range(data.shape[1]):
    cmax = -1
    for ri in range(data.shape[0] - 1, -1, -1):
        rv = data[ri, ci]
        if rv > cmax:
            cmax = rv
            vis[ri, ci] = 1
# check from left
for ri in range(data.shape[0]):
    rmax = -1
    for ci in range(data.shape[1] - 1, -1, -1):
        cv = data[ri, ci]
        if cv > rmax:
            rmax = cv
            vis[ri, ci] = 1
logging.debug(vis)
print(sum(sum(vis)))
