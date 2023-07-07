import sys

x, y, w, h = map(int, sys.stdin.readline().strip().split())

print(min(x, w-x, y, h-y))

"""
과정
1. 값을 입력한다.
2. 최단거리를 찾아 출력한다.
"""