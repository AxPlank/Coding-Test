import sys

T = int(sys.stdin.readline().strip())

for i in range(T):
    a, b = map(int, sys.stdin.readline().strip().split())
    print(a + b)

"""
과정 및 함수 설명
함수

과정
1. 값을 입력받는다.
2. 두 수의 합을 출력한다.
"""