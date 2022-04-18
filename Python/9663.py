"""
백준 9663번: N-Queen
"""

import sys

def chess_queen(row):
    global cnt
    if row == N:
        cnt += 1
        return
    
    for i in range(N):
        chess_table[row] = i
        
        for j in range(row):
            if abs(row - j) == abs(i - chess_table[j]) or i == chess_table[j]:
                continue
            chess_queen(row+1)
            
cnt = 0
N = int(sys.stdin.readline())
chess_table = [0] * N

chess_queen(0)
print(cnt)