"""
백준 2981번: 검문
"""

import sys
from math import gcd

N = int(sys.stdin.readline())
numbers = [int(sys.stdin.readline()) for _ in range(N)]
num_intervals = [abs(numbers[i]-numbers[i+1]) for i in range(N-1)]
GCD = 0

for i in range(N-2):
    GCD = gcd(num_intervals[i], num_intervals[i+1])
    
M_list = []
for i in range(2, int(GCD/2)+1):
    if GCD % i == 0:
        