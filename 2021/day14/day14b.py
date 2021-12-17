from collections import defaultdict

with open("input.txt") as f:
    data = f.read()
rules = {}
data = data.splitlines()
poly = data[0]
pairs = defaultdict(int)
chars = defaultdict(int)
for line in data[2:]:
    p, i = line.split(" -> ")
    rules[p] = (p[0] + i, i + p[1], i)
for i in range(1, len(poly)):
    pair = poly[i - 1 : i + 1]
    pairs[pair] += 1
for c in poly:
    chars[c] += 1
for x in range(40):
    items = {key: value for key, value in pairs.items()}
    for k, v in items.items():
        chars[rules[k][2]] += v
        pairs[rules[k][0]] += v
        pairs[rules[k][1]] += v
        pairs[k] -= v

print(max(chars.values()) - min(chars.values()))
