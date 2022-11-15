a,b = map(int, input().split())

result = []

for i in range(1, b + 1):
    for j in range(i):
        result.append(i)

print(sum(result[a - 1:b]))
        

