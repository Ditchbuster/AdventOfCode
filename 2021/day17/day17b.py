import math

with open("input.txt") as f:
    data = f.read()
data = data.splitlines()
data = data[0].split()
x1, x2 = [int(x) for x in data[2][2:-1].split("..")]
y1, y2 = [int(x) for x in data[3][2:].split("..")]

ey0 = math.sqrt((y1 - y2) * (y1 - y2) + (y1 + y2))
ex0 = math.sqrt(2 * (max([x1, y1])))
print(ey0, ex0)
maxs = []
for y0 in range(-500, 500):  # range(int(ey0 - 5), int(ey0 + 6)):
    for x0 in range(200):  # range(int(ex0 - 5), int(ex0 + 5)):
        y, x = (0, 0)
        ys = [0]
        vy = y0
        vx = x0
        while y >= y1 and x <= x2:
            y += vy
            if vx != 0:
                x += vx
                vx += 1 if vx < 0 else -1
            vy += -1
            if y >= y1 and y <= y2 and x >= x1 and x <= x2:
                maxs.append((x0, y0))
                break
print(len(maxs))
