# Sol 1
import sys

S = sys.stdin.readline().strip()

for i in range(97, 123):
    if chr(i) in S:
        print(S.index(chr(i)), end=' ')
    else:
        print('-1', end=' ')

# Sol 2
import sys

S = sys.stdin.readline().strip()

for i in range(97, 123):
    print(S.find(chr(i)), end=' ')

"""
과정 및 함수 설명
함수

과정
1. 값을 입력받는다.
2. 조건에 맞춰 값을 출력한다.
"""