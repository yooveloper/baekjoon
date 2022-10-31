sub = int(input())
score = list(map(int, input().split()))

val = 0

for i in range(sub):
    val += score[i] / max(score) * 100
print(val/sub)