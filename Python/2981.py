"""
백준 2981번: 검문
"""

import sys

N = int(sys.stdin.readline())
numbers = [int(sys.stdin.readline()) for _ in range(N)]
numbers_len = len(numbers)
numbers_min = min(numbers)
remainders = []

for i in range(2, numbers_min+1):
    cnt = 0
    remainderr = numbers[0] % i
    for j in numbers:
        if j % i != remainderr:
            break
        cnt += 1
        
    if cnt == numbers_len:
        remainders.append(str(i))

if len(remainders) > 0:
    print(' '.join(remainders))