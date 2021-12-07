import math
from aocd import data    
#numbers = [16,1,2,0,4,2,7,1,2,14]
numbers = [int(x) for x in data.split(',')]
numbers.sort()
minFuel = 0
for x in range(numbers[0],numbers[-1]+1):
    fuel = 0
    for c in numbers:
        if (c==x):
            continue
        else:
            a = min(x,c)
            b = max(x,c)
            fuel += sum(range(b-a+1))
            #print(x,c,fuel)
    minFuel = min(fuel,minFuel) if minFuel != 0 else fuel
    print(x,numbers[-1])
print(minFuel)