

# 먼저 카드의 장수 N 변수와 카드의 합인 M 변수 선언
N, M = map(int, input().split())

# N장 카드의 숫자를 입력받아 변수에 저장
card = list(map(int, input().split()))

# 카드의 합을 저장할 변수
result = 0

# 입력받은 카드의 길이
length = len(card)

# ex) [3,4,5,6,7] 이라면 3을 기준으로 4,5를 더하고 4를 기준으로 5,6을 더하고 이런식으로
# 기준점을 잡고 3번쨰 카드까지 더함

for i in range(0, length):
    for j in range(i+1, length):
        for k in range(j+1, length):
            sum = card[i] + card[j] + card[k]
            if sum <= M:
                result = max(result, sum)

print(result)
