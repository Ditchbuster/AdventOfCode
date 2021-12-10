from aocd import data, submit
#data = open('input.txt').read()
seg = [k.split() for k in [x.split('| ')[1] for x in data.splitlines()]]
count = 0
for line in seg:
    for s in line:
        if len(s) == 2 or len(s) == 3 or len(s) == 4 or len(s) == 7:
            count += 1
print(count)