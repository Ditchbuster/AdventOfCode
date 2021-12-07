from aocd import data    
#numbers = [16,1,2,0,4,2,7,1,2,14]
numbers = [int(x) for x in data.split(',')]
numbers.sort()
align = numbers[int(len(numbers)/2)]
fuel = sum([abs(x-align) for x in numbers])
print(align, fuel)