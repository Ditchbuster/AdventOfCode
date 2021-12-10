from aocd import data, submit
#data = open('input.txt').read()
seg = [k.split() for k in [x.split('| ')[0] for x in data.splitlines()]]
count = 0
for line in seg:
    decode = ['abcdefg']*7
    line = sorted(line, key=len)
    for c in line[0]: # num 1
        remove = [0,3,4,5,6]
        for r in remove:
            decode[r] = decode[r].replace(c,"")
    decode[1] = decode[2] = line[0]
    for c in line[1]: # num 7
        remove = [3,4,5,6]
        for r in remove:
            decode[r] = decode[r].replace(c,"")
        if c not in decode[1]:
            decode[0] = c
    decode[6] = ''
    decode[5] = ''
    for c in line[2]: # num 4
        remove = [0,3,4] # 0 not needed really
        for r in remove:
            decode[r] = decode[r].replace(c,"")
        if c not in decode[1]:
            decode[6] += c
            decode[5] += c
        
    print(decode)

    
