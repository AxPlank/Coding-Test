"""
백준 15652번: N과 M(4)
"""

import sys

N, M = map(int, sys.stdin.readline().strip().split())

num_arr = []

def backtracking():
    if len(num_arr) == M:
        print(' '.join(map(str, num_arr)))
        return
            
    for i in range(1, N+1):
        if len(num_arr) == 0:
            num_arr.append(i)
            backtracking()
            num_arr.pop()
            continue
            
        if i >= num_arr[-1]:
            num_arr.append(i)
            backtracking()
            num_arr.pop()
            
backtracking()