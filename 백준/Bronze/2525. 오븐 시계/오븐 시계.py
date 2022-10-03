hour,min = map(int, input().split())
c = int(input())

hour += c // 60
min += c % 60

if min >= 60:
    min -= 60
    hour += 1
if hour >= 24:
    hour -= 24
    
print(hour,min)
    