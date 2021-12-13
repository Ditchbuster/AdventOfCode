from aocd import data

with open("input.txt") as f:
    data = f.read()
points = {}
data = data.splitlines()
for line in data:
    if len(line) == 0:
        continue
    elif line[0].isdigit():
        x, y = [int(x) for x in line.split(",")]
        points[(x, y)] = True
    elif line[0] == "f":
        line = line.split()
        d, i = line[-1].split("=")
        i = int(i)
        if d == "y":
            move = [k for k in points.keys() if k[1] >= i]
            for p in move:
                points.pop(p)
                if p[1] != i:
                    points[(p[0], i - (p[1] - i))] = True
        if d == "x":
            move = [k for k in points.keys() if k[0] >= i]
            for p in move:
                points.pop(p)
                if p[0] != i:
                    points[(i - (p[0] - i)), p[1]] = True
        break
print(len(points))
