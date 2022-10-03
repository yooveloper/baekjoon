a = list(map(int, input().split(' ')))

ascending = True
descending = True

# range 1부터 시작하는 이유는 배열의 두번째부터 시작해서 앞에놈이랑 비교하려고
# ex) [1,3,5,8,1,2] 면 3과 1을 비교해서 오름차순인지 내림차순인지 알수있게
for i in range(1, 8):
    if a[i] > a[i-1]:
        descending = False
    elif a[i] < a[i-1]:
        ascending = False
        
if ascending:
    print('ascending')
elif descending:
    print('descending')
else:
    print('mixed')
    