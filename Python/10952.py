# Sol 1
import sys

while True:
    A, B = map(int, sys.stdin.readline().strip().split())
    if A == 0 and B == 0:
        break
    print(A + B)
    
# Sol 2
import sys

while True:
    A, B = map(int, sys.stdin.readline().strip().split())
    if A + B == 0:
        break
    print(A + B)

"""
과정 및 함수 설명
함수

과정
1. 값을 입력받는다.
2. 두 수의 합을 출력한다.
"""