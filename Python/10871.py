import sys

N, X = map(int, sys.stdin.readline().strip().split())
A = list(map(int, sys.stdin.readline().strip().split()))

for i in A:
    if X > i:
        print(i)

"""
과정 및 함수 설명
함수

과정
1. 값을 입력받는다.
2. 반복문을 이용해 각 요소와 X와의 대소비교를 실시하고 X가 더 클 경우, 해당 요소를 출력한다.
"""