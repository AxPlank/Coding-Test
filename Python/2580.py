"""
백준 2580번: 스도쿠
"""

import sys

def box33_check(xmin, xmax, ymin, ymax, xidx, yidx):
    for i in range(xmin, xmax):
        for j in range(ymin, ymax):
            if sdocu_table[xidx][yidx] == sdocu_table[i][j]:
                return False
    return True

def y_check(xidx, yidx):
    for i in range(9):
        if sdocu_table[xidx][i] == sdocu_table[xidx][yidx]:
            return False
    return True

def x_check(xidx):
    if i in sdocu_table[xidx]:
        return False
    return True

def sdocu():
    for i in range(9):
        for j in range(9):
            if sdocu_table[i][j] == 0:
                for k in range(1, 10):
                    sdocu_table[i][j] = k
                    """
                    k가 들어갈 수 있는지 점검
                    """
                    if i >= 0 and i <= 2 and j >= 0 and j <= 2:
                        if box33_check(0, 3, 0, 3, i, j) and y_check(i, j) and x_check(i):
                            break
                        continue
                    if i >= 3 and i <= 5 and j >= 0 and j <= 2:
                        if box33_check(3, 6, 0, 3, i, j) and y_check(i, j) and x_check(i):
                            break
                        continue
                    if i >= 6 and i <= 8 and j >= 0 and j <= 2:
                        if box33_check(6, 9, 0, 3, i, j) and y_check(i, j) and x_check(i):
                            break
                        continue
                    if i >= 0 and i <= 2 and j >= 3 and j <= 5:
                        if box33_check(0, 3, 3, 6, i, j) and y_check(i, j) and x_check(i):
                            break
                        continue
                    if i >= 3 and i <= 5 and j >= 3 and j <= 5:
                        if box33_check(3, 6, 3, 6, i, j) and y_check(i, j) and x_check(i):
                            break
                        continue
                    if i >= 6 and i <= 8 and j >= 3 and j <= 5:
                        if box33_check(6, 9, 3, 6, i, j) and y_check(i, j) and x_check(i):
                            break
                        continue
                    if i >= 0 and i <= 2 and j >= 6 and j <= 8:
                        if box33_check(0, 3, 6, 9, i, j) and y_check(i, j) and x_check(i):
                            break
                        continue
                    if i >= 3 and i <= 5 and j >= 6 and j <= 8:
                        if box33_check(3, 6, 6, 9, i, j) and y_check(i, j) and x_check(i):
                            break
                        continue
                    if i >= 6 and i <= 8 and j >= 6 and j <= 9:
                        if box33_check(6, 9, 6, 9, i, j) and y_check(i, j) and x_check(i):
                            break
                        continue

sdocu_table = []
for i in range(9):
    sdocu_table.append(list(map(int, sys.stdin.readline().strip().split())))
    
sdocu()
    
for i in range(9):
    print(' '.join(map(str, sdocu_table[i])))