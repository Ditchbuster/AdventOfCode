import math
import logging

logging.basicConfig(level=logging.DEBUG)
logging.debug("Open file")
with open("input.txt") as f:
    data = f.read()
data = data.splitlines()
logging.info(data)
cals = list()
cals.append(0)
mx = 0
for l in data:
    if l == "":
        mx = max(cals[-1], mx)
        cals.append(0)
        continue
    cals[-1] += int(l)
print(mx)
