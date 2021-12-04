def shifting(bitlist):
    out = 0
    for bit in bitlist:
        out = (out << 1) | bit
    return out
with open("input.txt") as f:
    lines = []
    for l in f.read().splitlines():
        lines.append([ int(x) for x in l]) 
    ox = lines.copy()
    for i in range(len(ox[0])):
        oxI = [o[i] for o in ox]
        if sum(oxI) >= len(ox)/2:
            ox = [o for o in ox if o[i] == 1]
        else:
            ox = [o for o in ox if o[i] == 0]
        if len(ox) == 1:
            #print(ox)
            break
    co = lines.copy()
    for i in range(len(co[0])):
        coI = [o[i] for o in co]
        if sum(coI) < len(co)/2:
            co = [o for o in co if o[i] == 1]
        else:
            co = [o for o in co if o[i] == 0]
        if len(co) == 1:
            #print(co)
            break    
    ox = shifting(ox[0])
    co = shifting(co[0])
    print(co*ox)