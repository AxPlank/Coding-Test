import sys

A, B, C = map(int, sys.stdin.readline().strip().split())

if C <= B:
    print(-1)
else:
    print(int(A/(C-B))+1)

"""
과정
1. 문장을 입력한다.
2. 손익분기점일 때의 노트북 판매량을 출력한다.
"""