with open("input.txt") as f:
    data = f.read()
data = [[int(c) for c in line] for line in data.splitlines()]
# print(data)


def printGrid(data):
    for line in data:
        print("".join(str(x) for x in line))


def flash(y, x):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if not (i == 0 and j == 0) and (
                y + i >= 0 and y + i < len(data) and x + j >= 0 and x + j < len(data[y])
            ):
                data[y + i][x + j] += 1
                if data[y + i][x + j] == 10:
                    powered.append((y + i, x + j))
                    count += 1
    return count


# printGrid(data)
count = 0
for step in range(100):
    powered = []
    for y in range(len(data)):
        for x in range(len(data[y])):
            data[y][x] += 1
            if data[y][x] == 10:
                powered.append((y, x))
                count += 1
    for p in powered:
        count += flash(p[0], p[1])
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] > 9:
                data[y][x] = 0
    # printGrid(data)
print(count)
