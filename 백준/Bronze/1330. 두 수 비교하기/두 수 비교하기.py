#첫째 줄에 다음 세 가지 중 하나를 출력한다.
#A가 B보다 큰 경우에는 '>'를 출력한다.
#A가 B보다 작은 경우에는 '<'를 출력한다.
#A와 B가 같은 경우에는 '=='를 출력한다.

data = input().split(' ')
a = int(data[0])
b = int(data[1])

if a > b:
    print('>')
elif a < b:
    print('<')
else:
    print('==')