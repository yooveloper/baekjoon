size, x = map(int, input().split())

arr = list(map(int, input().split()))

for i in range(size):
    if arr[i] < x:
        print(arr[i], end=' ')

