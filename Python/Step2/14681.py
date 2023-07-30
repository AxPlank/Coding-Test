x = int(input())
y = int(input())

if x > 0 and y > 0:
    print(1)
elif x < 0 and y > 0:
    print(2)
elif x < 0 and y < 0:
    print(3)
else:
    print(4)

"""
과정 및 함수 설명
함수

과정
1. 좌표를 입력받는다.
2. 해당하는 사분면을 출력한다.
"""