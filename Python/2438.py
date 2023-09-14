# Sol 1
import sys

N = int(sys.stdin.readline().strip())

for i in range(1, N+1):
    print('*' * i)
    
# Sol 2
import sys

N = int(sys.stdin.readline45().strip())

for i in range(1, N+1):
    for j in range(0, i):
        if j == i - 1:
            print("*")
        else:
            print("*", end="")

"""
과정 및 함수 설명
함수

과정
1. 값을 입력받는다.
2. 반복문을 이용해 별들을 출력한다.
"""