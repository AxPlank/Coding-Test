"""
백준 1358번: 하키
"""
import sys
from math import sqrt

cnt = 0
W, H, X, Y, P = map(int, sys.stdin.readline().strip().split())

# 좌표가 원 안에 있는지 확인하는 함수
def distancee(center, x, y, r):
    distance_x = abs(center[0] - x)
    distance_y = abs(center[1] - y)
    if sqrt(distance_x**2 + distance_y**2) <= r:
        return True
    return False

for _ in range(P):
    x, y = map(int, sys.stdin.readline().strip().split())
    if (X <= x <= X+W) and (Y <= y <= Y+H):
        cnt += 1
    else:
        center1 = (X, Y+H//2)
        center2 = (X+W, Y+H//2)
        r = H // 2
        if distancee(center1, x, y, r) or distancee(center2, x, y, r):
            cnt += 1

print(cnt)