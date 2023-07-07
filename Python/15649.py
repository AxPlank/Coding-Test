"""
백준 15649번: N과 M(1)
"""

"""
Sol 1: 반복문 이용
"""
import sys

N, M = map(int, sys.stdin.readline().strip().split())

num_arr = []

def backtracking():
    if len(num_arr) == M:
        for i in num_arr:
            print(i, end=' ')
            return
            
    for i in range(1, N+1):
        if i not in num_arr:
            num_arr.append(i)
            backtracking()
            num_arr.pop()
            
backtracking()

"""
Sol 2: join 이용
"""

import sys

N, M = map(int, sys.stdin.readline().strip().split())

num_arr = []

def backtracking():
    if len(num_arr) == M:
        print(' '.join(map(str, num_arr)))
        return
            
    for i in range(1, N+1):
        if i not in num_arr:
            num_arr.append(i)
            backtracking()
            num_arr.pop()
            
backtracking()