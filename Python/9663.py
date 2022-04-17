"""
백준 9663번: N-Queen
"""

import sys

def chess(chess_table, queen_count):
    global cnt
    if queen_count == 0:
        cnt += 1
        return
    
    temp_table = chess_table
    for i in range(N):
        for j in range(N):
            if chess_table[i][j]:
                queen_count -= 1
                chess_table[i][j] = False
                
                chess_table[i] = [False] * N
                for k in range(N):
                    chess_table[k][j] = False
                    
                    

N = int(sys.stdin.readline())
chess_table = [[True for _ in range(N)] for _ in range(N)]
queen_count = N
cnt = 0

chess(chess_table, queen_count)
print(cnt)