import sys

N = int(sys.stdin.readline().strip())

for i in range(1, N+1):
    print(' ' * (N-i) + '*' * i)

"""
과정 및 함수 설명
함수

과정
1. 값을 입력받는다.
2. 반복문을 이용해 별들을 출력한다.
"""