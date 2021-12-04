with open("input.txt") as f:
    hor = 0
    aim = 0
    depth = 0
    for l in f.readlines():
        parts = l.split(' ')
        print(parts)
        if parts[0] == 'forward':
            hor += int(parts[1])
            depth += aim*int(parts[1])
        elif parts[0] == 'down':
            aim += int(parts[1])
        elif parts[0] == 'up':
            aim -= int(parts[1])
    print(hor,aim,depth,hor*depth)