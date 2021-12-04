with open("input.txt") as f:
    hor = 0
    depth = 0
    for l in f.readlines():
        parts = l.split(' ')
        print(parts)
        if parts[0] == 'forward':
            hor += int(parts[1])
        elif parts[0] == 'down':
            depth += int(parts[1])
        elif parts[0] == 'up':
            depth -= int(parts[1])
    print(hor,depth,hor*depth)