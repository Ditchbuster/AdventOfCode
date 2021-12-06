with open('input.txt') as f:
    init = [int(x) for x in f.readline().rstrip().split(',')]
    count = [init.count(x) for x in range(9)]
    days = 256
    for d in range(days):
        born = count[0]
        for i in range(len(count)-1):
            count[i] = count[i+1]
        count[6] += born
        count[8] = born
        #print(count)
    print(sum(count))
