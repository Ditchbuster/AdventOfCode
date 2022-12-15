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
# print(data[0, 1 - 1 :: -1])
vis = np.zeros(data.shape, dtype=int)
for ri in range(1, data.shape[0] - 1):
    for ci in range(1, data.shape[1] - 1):
        cv = data[ri][ci]
        # right
        logging.debug(f"{ri} {ci}")
        if ci < data.shape[1] - 1:
            rvis = 0
            for iv in data[ri, ci + 1 :]:
                rvis += 1
                if iv >= cv:
                    break
        # left
        if ci > 0:
            lvis = 0
            for iv in data[ri, ci - 1 :: -1]:
                lvis += 1
                if iv >= cv:
                    break
        # down
        if ri < data.shape[0] - 1:
            dvis = 0
            for iv in data[ri + 1 :, ci]:
                dvis += 1
                if iv >= cv:
                    break
        # up
        if ri > 0:
            uvis = 0
            for iv in data[ri - 1 :: -1, ci]:
                uvis += 1
                if iv >= cv:
                    break
        vis[ri][ci] = rvis * lvis * dvis * uvis
        logging.debug(vis)
print(vis.max())
