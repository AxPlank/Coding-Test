"""
백준 1934: 최소공배수
"""

import sys

def getGCD(a, b):
    while b > 0:
        a, b = b, a % b
    return a

T = int(sys.stdin.readline())

for _ in range(T):
    A, B = map(int, sys.stdin.readline().strip().split())
    LCM = (A * B) // getGCD(max(A, B), min(A, B))
    print(LCM)