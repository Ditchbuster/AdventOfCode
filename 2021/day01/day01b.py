with open("input.txt") as f:
    lines =  [int(l) for l in f.readlines()]   
    count = 0
    for x in range(4, len(lines)+1):
        if (sum(lines[x-4:x-1])<sum(lines[x-3:x])):
            count +=1
    print(count)
