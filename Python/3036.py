"""
백준 3036번: 링
"""
import sys
from math import lcm

N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().strip().split()))

for i in range(1, N):
    LCM = lcm(numbers[0], numbers[i])
    print(f'{LCM//numbers[i]}/{LCM//numbers[0]}')