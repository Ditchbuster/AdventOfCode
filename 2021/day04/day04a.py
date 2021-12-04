from collections import defaultdict

def checked(marked):
    for b in marked:
        mask = 0b11111
        for r in b:
            if (r == 0b11111):
                return (marked.index(b))
            mask &= r
        if (mask > 0b00000):
            return (marked.index(b))
    return False

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
    for d in draws:
        for coords in numbers[d]:
            marked[coords[0]][coords[1]] |= (1<<coords[2])
        b = checked(marked)
        if b:
            score = 0
            for i in range(5):
                for j in range(5):
                    score += int(boards[b][i][j]) if not marked[b][i]&(1<<j) else 0
            print(score*int(d))
            break

