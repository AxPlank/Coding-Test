import sys

A = int(sys.stdin.readline().strip())
B = int(sys.stdin.readline().strip())
C = int(sys.stdin.readline().strip())

listt = list(str(A * B * C))

for i in range(10):
    print(listt.count(f'{i}'))
    
"""
과정 및 함수 설명
함수

과정
1. 값을 입력받는다.
2. 최댓값을 출력한다.
"""