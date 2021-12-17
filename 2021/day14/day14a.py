with open("input.txt") as f:
    data = f.read()
rules = {}
data = data.splitlines()
poly = data[0]
for line in data[2:]:
    p, i = line.split(" -> ")
    rules[p] = i
for x in range(10):
    newPoly = poly[0]
    for i in range(1, len(poly)):
        pair = poly[i - 1 : i + 1]
        try:
            newPoly += rules[pair]
        except KeyError:
            pass
        newPoly += poly[i]
    poly = newPoly
print(poly)
chars = [poly.count(x) for x in poly]
print(max(chars) - min(chars))
