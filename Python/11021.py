import sys

T = int(sys.stdin.readline().strip())

for i in range(1, T+1):
    a, b = map(int, sys.stdin.readline().strip().split())
    print(f'Case #{i}: {a + b}')

"""
과정 및 함수 설명
함수

과정
1. 값을 입력받는다.
2. 두 수의 합을 출력한다.
"""