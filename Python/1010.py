"""
백준 1010번: 다리 놓기
"""
import sys
from math import comb

T = int(sys.stdin.readline())

for _ in range(T):
    N, M = map(int, sys.stdin.readline().strip().split())
    print(comb(M, N))