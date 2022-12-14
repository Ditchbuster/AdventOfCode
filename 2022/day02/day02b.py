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
    n, p = l.split()
    if p == "Y":
        p = chr(ord(n) + 23)
    elif p == "X":
        p = chr(ord(n) + 22)
        if p < "X":
            p = "Z"
    elif p == "Z":
        p = chr(ord(n) + 24)
        if p > "Z":
            p = "X"

    if ord(n) == ord(p) - 23:
        # draw
        logging.debug(f"{n} {p} were a draw")
        total += 3
    elif ord(n) == ord(p) - 24 or ord(n) == ord(p) - 21:
        # p wins
        logging.debug(f"{n} {p} p wins")
        total += 6
    elif ord(n) == ord(p) - 22 or ord(n) == ord(p) - 23:
        # n wins
        logging.debug(f"{n} {p} n wins")
    total += ord(p) - 87

print(total)
