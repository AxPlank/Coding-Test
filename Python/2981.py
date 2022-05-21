"""
백준 2981번: 검문
"""
import sys
from math import gcd, sqrt
import rand

N = int(sys.stdin.readline())
numbers = [int(sys.stdin.readline()) for _ in range(N)]

nums_interval = []
for i in range(1, N):
    nums_interval.append(abs(numbers[i]-numbers[i-1]))
    
nums_interval = sorted(list(set(nums_interval)))
GCD = gcd(nums_interval[0], nums_interval[1])
M = set()
M.add(GCD)
for i in range(2, int(sqrt(GCD))+1):
    if GCD % i == 0:
        M.add(i)
        M.add(GCD//i)
        
nums_str = list(map(str, sorted(M)))
print(' '.join(nums_str))