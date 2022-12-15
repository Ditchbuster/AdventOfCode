import math
import logging
from collections import defaultdict

logging.basicConfig(level=logging.DEBUG)
logging.debug("Open file")
with open("input.txt") as f:
    data = f.read()
data = data.splitlines()
# logging.info(data)
PLENGTH = 14
for l in data:
    for i in range(PLENGTH, len(l)):
        if len(set(l[i - PLENGTH : i])) == PLENGTH:
            print(i)
            break
