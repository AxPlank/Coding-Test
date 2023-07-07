"""
백준 9663번: N-Queen
"""

import sys

def checkk(row):
    """
    해당 좌표에 퀸이 위치할 수 있는지 확인
    """
    for i in range(row):
        if chess_table[row] == chess_table[i] or abs(chess_table[row]-chess_table[i]) == abs(row-i):
            return False
    return True

def chess_queen(row):
    global cnt
    if row == N:
        cnt += 1
        return
    
    for i in range(N):
        chess_table[row] = i
        
        if checkk(row):
            chess_queen(row+1)
            
cnt = 0
N = int(sys.stdin.readline())
chess_table = [0] * N

chess_queen(0)
print(cnt)