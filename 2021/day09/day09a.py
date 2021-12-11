from aocd import data, submit
""" with open('input.txt') as f:
    data = f.read() """
data = [[int(c) for c in line] for line in data.splitlines()]
count = 0
risk_total = 0
for y in range(len(data)):
    for x in range(len(data[y])):
        lowest = True
        val = data[y][x]
        if (x > 0 and data[y][x-1] <= val):
            lowest = False
        if (y > 0 and data[y-1][x]<=val):
            lowest = False
        #print(y,x, len(data[y]))
        if (x < len(data[y]) - 1 and data[y][x+1] <= val):
            lowest = False
        if (y < len(data) - 1 and data[y+1][x] <= val):
            lowest = False
        if (lowest):
            count += 1
            risk_total += data[y][x] + 1
            print(y,x,data[y][x])
    print(risk_total)
print(count,risk_total)
submit(risk_total)           
