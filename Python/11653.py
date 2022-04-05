import sys

N = int(sys.stdin.readline().strip())
i = 2

while N != 1:
    if N % i == 0:
        N /= i
        print(i)
    else:
        i += 1

"""
과정
1. 정수를 입력한다.
2. 2부터 시작하여 정수를 나눴을 때, 나머지가 0이라면 나눈 수를 출력한다.
"""