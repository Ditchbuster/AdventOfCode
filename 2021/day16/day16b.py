import numpy as np


def parse(i, line):

    ver = int(line[i : i + 3], 2)
    type = int(line[i + 3 : i + 6], 2)
    vers.append(ver)
    i += 6
    """ except IndexError:
        return len(line), 0
        # raise ValueError("Should be the end of the line")
    except ValueError:
        return len(line), 0 """
    # print(ver, type)
    if type == 4:
        endFlag = True
        num = ""
        while endFlag:
            endFlag = True if line[i] == "1" else False
            num += line[i + 1 : i + 5]
            i += 5
            val = int(num, 2)
        # print(int(num, 2))
    else:
        op = int(line[i], 2)
        i += 1
        if op == 0:
            num = int(line[i : i + 15], 2)
            i += 15
            start = i
            val = []
            while start + num > i:
                i, v = parse(i, line)
                val.append(v)
        else:
            num = int(line[i : i + 11], 2)
            i += 11
            val = []
            for _ in range(num):
                i, v = parse(i, line)
                val.append(v)
        if type == 0:
            val = sum(val)
        elif type == 1:
            val1 = val[0]
            for x in val[1:]:
                val1 = val1 * x
            val = val1
        elif type == 2:
            val = min(val)
        elif type == 3:
            val = max(val)
        elif type == 5:
            val = 1 if val[0] > val[1] else 0
        elif type == 6:
            val = 1 if val[0] < val[1] else 0
        elif type == 7:
            val = 1 if val[0] == val[1] else 0
    return i, val


with open("input.txt") as f:
    data = f.read()
data = data.splitlines()
for line in data:
    line = bin(int(line, 16))[2:].zfill(len(line) * 4)
    i = 0
    vers = []
    while i < len(line):
        try:
            i, v = parse(i, line)
            print(v)
        except IndexError:
            break
        except ValueError:
            break
    # print(sum(vers))

