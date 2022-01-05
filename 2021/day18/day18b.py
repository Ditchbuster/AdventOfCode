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


max = 0
for i, line in enumerate(data[:-1]):
    for j, line2 in enumerate(data[i + 1 :]):
        comb = "[" + line + "," + line2 + "]"
        err = 0
        while err == 0:
            comb, err = checkExplode(comb)
            if err == -1:
                comb, err = split(comb)
            # print(line)
        num = mag(comb)
        max = num if num > max else max
        comb = "[" + line2 + "," + line + "]"
        err = 0
        while err == 0:
            comb, err = checkExplode(comb)
            if err == -1:
                comb, err = split(comb)
            # print(line)
        num = mag(comb)
        max = num if num > max else max

print(max)
