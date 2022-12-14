import math
import logging

logging.basicConfig(level=logging.DEBUG)
logging.debug("Open file")
with open("input.txt") as f:
    data = f.read()
data = data.splitlines()
# logging.info(data)
total = 0
for l in data:
    f = l[: len(l) // 2]
    s = l[len(l) // 2 :]
    logging.debug(f"{f} {s}")
    for c in f:
        if c in s:
            o = ord(c) - 38
            if o >= 59:
                o = o - 58
            total += o
            break


print(total)
