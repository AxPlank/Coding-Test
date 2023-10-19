"""
백준 10807번: 개수 세기
"""

import sys

N = int(sys.stdin.readline().rstrip())
Arr = list(map(int, sys.stdin.readline().rstrip().split(" ")))
v = int(sys.stdin.readline().rstrip())

print(Arr.count(v))