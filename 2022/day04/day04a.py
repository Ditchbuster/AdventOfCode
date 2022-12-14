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
    f, s = l.split(",")
    f = [int(x) for x in f.split("-")]
    s = [int(x) for x in s.split("-")]
    logging.debug(f"{f} {s}")
    if (f[0] >= s[0] and f[1] <= s[1]) or (f[0] <= s[0] and f[1] >= s[1]):
        total += 1


print(total)
