numbers = []
for i in range(9):
    value = int(input())
    numbers.append(value)
    
print(max(numbers))
print(numbers.index(max(numbers))+1)