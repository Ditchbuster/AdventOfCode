import math
import logging
from collections import defaultdict

logging.basicConfig(level=logging.DEBUG)
logging.debug("Open file")
with open("input.txt") as f:
    data = f.read()
data = data.splitlines()
# logging.info(data)

for l in data:
    for i in range(4, len(l)):
        if len(set(l[i - 4 : i])) == 4:
            print(i)
            break
