"""
백준 11051번: 이항 계수 2
"""
import sys

def combb(n):
    if n <= 1:
        return 1
    
    return n * combb(n-1)

N, K = map(int, sys.stdin.readline().strip().split())

Binomm = combb(N) // (combb(N-K) * combb(K))
print(Binomm % 10007)