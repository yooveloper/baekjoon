#Case #1: 2
#Case #2: 5
#Case #3: 7
#Case #4: 17
#Case #5: 7

size = int(input())

for i in range(1,size+1):
    a,b = map(int, input().split())
    print(f'Case #{i}: {a+b}')