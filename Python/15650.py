"""
백준 15650번: N과 M(2)
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
            if num_arr.index(i) == M - 1:
                print()
                return
            
    for i in range(1, N+1):
        if len(num_arr) == 0:
            num_arr.append(i)
            backtracking()
            num_arr.pop()
            continue
            
        if i > num_arr[-1]:
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
        if len(num_arr) == 0:
            num_arr.append(i)
            backtracking()
            num_arr.pop()
            continue
            
        if i > num_arr[-1]:
            num_arr.append(i)
            backtracking()
            num_arr.pop()
            
backtracking()