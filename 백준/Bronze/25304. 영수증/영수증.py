# 첫재 줄에는 영수증에 적힌 총 금액
x = int(input())

# 둘째줄에는 영수증에 적힌 구매한 물건의 종류의수 n이 주어진다.
n = int(input())

sum = 0 # 총 금액

# 이후 n개의 줄에는 각 물건의 가격 a와 개수 b가 공백을 사이에 두고 주어진다.
for i in range(n):
    a,b = map(int, input().split())
    sum += a*b # 가격 곱하기 개수

# 입력받은 영수증 총금액 x와 가격 곱하기 개수로 계산한 총금액이 같으면 Yes 아니면 No

if x == sum:
    print('Yes')
else:
    print('No')

