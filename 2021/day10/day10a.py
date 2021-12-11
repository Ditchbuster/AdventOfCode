from aocd import data, submit
""" with open('input.txt') as f:
    data = f.read()"""
data = data.splitlines()
OPEN = ["(","[","{","<"]
CLOSE = [")","]","}",">"]
COST = [3,57,1197,25137]

def checkLine(line):
    chunks = [line[0]]
    for c in line[1:]:
        if c in CLOSE:
            if OPEN[CLOSE.index(c)] == chunks.pop():
                continue
            else:
                return COST[CLOSE.index(c)]
        else:
            chunks.append(c)
    return 0

submit(sum([checkLine(line) for line in data]))    