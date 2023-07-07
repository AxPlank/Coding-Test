import sys

while True:
    try:
        A, B = map(int, sys.stdin.readline().strip().split())
        print(A + B)
    except:
        break
    
"""
과정 및 함수 설명
함수

과정
1. 값을 입력받는다.
2. 두 수의 합을 출력한다.
"""