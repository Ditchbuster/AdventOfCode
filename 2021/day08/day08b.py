from aocd import data, submit
#data = open('input.txt').read()
seg = [x.split('| ') for x in data.splitlines()]
count = 0
for s in seg:
    line = s[0].split()
    decode = {}
    line = sorted(line, key=len)
    decode[1] = set(line[0])
    decode[7] = set(line[1])
    decode[4] = set(line[2])
    decode[8] = set(line[9])
    decode[9] = set([x for x in line[6:9] if decode[4].issubset(x)][0])
    decode[2] = set([x for x in line[3:6] if not decode[9].issuperset(x)][0])
    decode[6] = set([x for x in line[6:9] if (decode[4]-decode[1]).issubset(x) and not decode[4].issubset(x)][0])
    decode[0] = set([x for x in line[6:9] if not (decode[4]-decode[1]).issubset(x)][0])
    decode[5] = set([x for x in line[3:6] if decode[6].issuperset(x)][0])
    decode[3] = set([x for x in line[3:6] if  not (decode[5].issuperset(x) or decode[2].issuperset(x))][0])
    #print(line)
    #print(decode)
    subTotal = 0
    number = ''
    #print(s[1])
    for out in s[1].split():
        t = set(out)
        #print(out)
        for k,v in decode.items():
            if len(t.symmetric_difference(v)) == 0:
                number += str(k)
                break
    subTotal += int(number)
    print(subTotal)
    count += subTotal
print(count)
