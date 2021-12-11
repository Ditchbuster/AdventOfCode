from aocd import data, submit

""" with open("input.txt") as f:
    data = f.read() """
data = data.splitlines()
OPEN = ["(", "[", "{", "<"]
CLOSE = [")", "]", "}", ">"]
COST = [1, 2, 3, 4]


def checkLine(line):
    chunks = [line[0]]
    for c in line[1:]:
        if c in CLOSE:
            if OPEN[CLOSE.index(c)] == chunks.pop():
                continue
            else:
                return -1
        else:
            chunks.append(c)
    count = 0
    for c in reversed(chunks):
        count = count * 5 + COST[OPEN.index(c)]
    return count


out = []
for line in data:
    score = checkLine(line)
    if score > -1:
        out.append(score)
out = sorted(out)
print(out[int(len(out) / 2)])
