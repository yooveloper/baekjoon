# 시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.

data = int(input())

if data >= 90:
    print('A')
elif data >= 80 and data < 90:
    print('B')
elif data >= 70 and data < 80:
    print('C')
elif data >= 60 and data < 70:
    print('D')
else:
    print('F')




