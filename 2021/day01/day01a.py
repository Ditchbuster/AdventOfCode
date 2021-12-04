with open("input.txt") as f:
    lastline = int(f.readline())
    incCount = 0
    for l in f.readlines():
        line = int(l)
        if lastline < line:
            incCount += 1
            #print(incCount)
        lastline = line
    print(incCount)