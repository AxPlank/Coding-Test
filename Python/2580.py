"""
백준 2580번: 스도쿠
"""

import sys

"""
자리에 특정 값이 들어갈 수 있는지를 점검하는 함수
"""
def check_x(x, num):
    if num in table[x]:
        return False
    return True

def check_y(y, num):
    for i in range(9):
        if table[i][y] == num:
            return False
    return True

def check_33box(x, y, num):
    for i in range((x//3)*3, (x//3+1)*3):
        for j in range((y//3)*3, (y//3+1)*3):
            if table[i][j] == num:
                return False
    return True

"""
스도쿠
"""
def sdocu(n):
    """
    point_0의 길이는 빈 칸의 수를 의미하므로, n의 값이 point_0라면 모든 자리가 다 채워졌음을 의미
    """
    if len(point_0) == n:
        for i in range(9):
            print(' '.join(map(str, table[i])))
        sys.exit()
    
    for i in range(1, 10):
        if check_x(point_0[n][0], i) and check_y(point_0[n][1], i) and check_33box(point_0[n][0], point_0[n][1], i):
            table[point_0[n][0]][point_0[n][1]] = i
            sdocu(n+1)
            table[point_0[n][0]][point_0[n][1]] = 0

table = []
for _ in range(9):
    table.append(list(map(int, sys.stdin.readline().strip().split())))
    
point_0 = []
for i in range(9):
    for j in range(9):
        if table[i][j] == 0:
            point_0.append((i, j))
            
sdocu(0)