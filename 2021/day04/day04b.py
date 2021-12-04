from collections import defaultdict

def checked(marked, won):
    c = []
    for i in range(len(marked)):
        #print(i, won, (i not in won), len(marked))
        if (i not in won):    
            mask = 0b11111
            for r in marked[i]:
                if (r == 0b11111):
                    #print('me',marked[i],i)
                    c.append(i)
                mask &= r
            if (mask > 0b00000):
                #print('i',r)
                c.append(i)
    return c 

with open('input.txt') as f:
    draws = f.readline().rstrip('\n').split(',')
    #print(draws)
    numbers = defaultdict(list)
    boards = []
    marked = []
    bIndex = -1
    input = f.read().splitlines()
    for i in range(len(input)):
        if input[i] == '':
            bIndex += 1
            boards.append([])
            marked.append([])
            continue
        row = [x for x in input[i].split()]
        boards[bIndex].append(row)
        marked[bIndex].append(0b00000)
        for r in range(len(row)):
            numbers[row[r]].append([bIndex,len(boards[bIndex])-1,r])
            #print(row[r],bIndex,len(boards[bIndex]),r)
    won = []
    lastD = 0
    for d in draws:
        for coords in numbers[d]:
            marked[coords[0]][coords[1]] |= (1<<coords[2])
        b = checked(marked,won)
        print(d,':',b)
        if len(b)>0:
            for y in b:
                won.append(y)
                score = 0
                for i in range(5):
                    for j in range(5):
                        score += int(boards[y][i][j]) if not marked[y][i]&(1<<j) else 0
                lastD = int(d)*score
            

    
    print(lastD)
    

