def parse(i, line):
    try:
        ver = int(line[i : i + 3], 2)
        type = int(line[i + 3 : i + 6], 2)
        vers.append(ver)
        i += 6
    except IndexError:
        return len(line)
        # raise ValueError("Should be the end of the line")
    except ValueError:
        return len(line)
    # print(ver, type)
    if type == 4:
        endFlag = True
        num = ""
        while endFlag:
            endFlag = True if line[i] == "1" else False
            num += line[i + 1 : i + 5]
            i += 5
        # print(int(num, 2))
    else:
        op = int(line[i], 2)
        i += 1
        if op == 0:
            num = int(line[i : i + 15], 2)
            i += 15
            start = i
            while start + num > i:
                i = parse(i, line)
        else:
            num = int(line[i : i + 11], 2)
            i += 11
            for _ in range(num):
                i = parse(i, line)
    return i


with open("input.txt") as f:
    data = f.read()
data = data.splitlines()
for line in data:
    line = bin(int(line, 16))[2:].zfill(len(line) * 4)
    i = 0
    vers = []
    while i < len(line):
        try:
            i = parse(i, line)
        except IndexError:
            break
    print(sum(vers))

