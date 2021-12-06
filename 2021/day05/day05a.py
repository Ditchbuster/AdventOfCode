from collections import defaultdict
with open('input.txt') as f:
    counts = defaultdict(int)
    for line in f.readlines():
        p1, p2 = line.rstrip('\n').split(' -> ')
        x1,y1 = [int(x) for x in p1.split(',')]
        x2,y2 = [int(y) for y in p2.split(',')]
        print(x1,y1,x2,y2)
        if (x1 == x2 or y1 == y2):
            xIter = range(x1,x2+1) if x2>=x1 else range(x1,x2-1,-1)
            yIter = range(y1,y2+1) if y2>=y1 else range(y1,y2-1,-1)
            for x in xIter:
                for y in yIter: #ha this is so wrong if they werent horizontal or vertical
                    counts[(x,y)] += 1
                    print((x,y), counts[(x,y)])
    print(len([v for k,v in counts.items() if v > 1]))