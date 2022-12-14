import math
import logging

logging.basicConfig(level=logging.DEBUG)
logging.debug("Open file")
with open("input.txt") as f:
    data = f.read()
data = data.splitlines()
data = zip(
    *[iter(data)] * 3
)  # i = iter(lst)   # Create iterable from list #zip(i, i, i)    # zip the iterable 3 times, giving chunks of the original list in 3
# logging.info(data)
total = 0
for l in data:  # l should be a tuple of 3 lists
    logging.debug(l)
    c = set(l[0]).intersection(set(l[1]), l[2]).pop()
    o = ord(c) - 38
    if o >= 59:
        o = o - 58
    total += o


print(total)
