import math

with open("input.txt") as f:
    data = f.read()
data = data.splitlines()


def checkExplode(line):
    lvl = 0
    for i, c in enumerate(line):
        if c == "[":
            lvl += 1
        if c == "]":
            lvl += -1
        if lvl > 4:
            # explode
            s = line.index(",", i)
            rb = line.index("]", i)
            left = int(line[i + 1 : s])
            right = int(line[s + 1 : rb])
            # print(left, right)
            lstring = line[:i]
            for l in range(len(lstring) - 1, 0, -1):
                if lstring[l].isdigit():
                    x = l - 1
                    while x > 0 and lstring[x].isdigit():
                        x += -1
                    num = int(lstring[x + 1 : l + 1])
                    lstring = lstring[: x + 1] + str(num + left) + lstring[l + 1 :]
                    break
            rstring = line[rb + 1 :]
            for r in range(len(rstring)):
                if rstring[r].isdigit():
                    x = r + 1
                    while x < len(rstring) and rstring[x].isdigit():
                        x += 1
                    num = int(rstring[r:x])
                    rstring = rstring[:r] + str(num + right) + rstring[x:]
                    break
            return lstring + "0" + rstring, 0
    return (line, -1)


def split(line):
    for i, c in enumerate(line):
        if c.isdigit() and line[i + 1].isdigit():
            num = int(line[i : i + 2])
            if num > 9:
                lstring = line[:i]
                rstring = line[i + 2 :]
                left = math.floor(num / 2)
                right = math.ceil(num / 2)
                return lstring + "[" + str(left) + "," + str(right) + "]" + rstring, 0
    return line, -1


def mag(line):
    if line[0].isdigit():
        return int(line[0])
    lvl = 0
    for i, c in enumerate(line):
        if c == "[":
            lvl += 1
        if c == "]":
            lvl += -1
        if c == "," and lvl == 1:
            return mag(line[1:i]) * 3 + mag(line[i + 1 : -1]) * 2


prev = data[0]
for line in data[1:]:
    line = "[" + prev + "," + line + "]"
    err = 0
    while err == 0:
        line, err = checkExplode(line)
        if err == -1:
            line, err = split(line)
        # print(line)
    prev = line
print(mag(line))
