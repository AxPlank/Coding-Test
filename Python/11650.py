"""
백준 11650번: 좌표 정렬하기
"""

import sys

N = int(sys.stdin.readline())
coordinate_list = [0] * N

for i in range(N):
    coordinate_list[i] = tuple(map(int, sys.stdin.readline().strip().split()))

coordinate_list = sorted(coordinate_list)
for i in range(N):
    print(coordinate_list[i][0], coordinate_list[i][1])