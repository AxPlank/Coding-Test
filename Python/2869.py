import sys

A, B, V = map(int, sys.stdin.readline().strip().split())
day = (V-A) / (A-B)

if day == int(day):
    print(int(day) + 1)
else:
    print(int(day) + 2)

"""
과정
1. 값을 입력한다.
2. 끝까지 올라가는데 걸린 날 수를 출력한다.
"""