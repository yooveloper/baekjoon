# Case #1: 1 + 1 = 2
# Case #2: 2 + 3 = 5
# Case #3: 3 + 4 = 7
# Case #4: 9 + 8 = 17
# Case #5: 5 + 2 = 7

size = int(input())

for i in range(1, size+1):
    a,b = map(int, input().split())
    print(f'Case #{i}: {a} + {b} = {a+b}')