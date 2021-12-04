def shifting(bitlist):
    out = 0
    for bit in bitlist:
        out = (out << 1) | bit
    return out

with open("input.txt") as f:
    lineCount = 1
    count = [int(x) for x in f.readline().rstrip('\n')]
    #print(count)
    
    for l in f.readlines():
        count = [x+y for x, y in zip(count, [int(x) for x in l.rstrip('\n')])]
        lineCount += 1
    
    g = [1 if x > lineCount/2 else 0 for x in count]
    g = shifting(g)
    e = [0 if x > lineCount/2 else 1 for x in count]
    e = shifting(e)
    print (count, lineCount, g*e)