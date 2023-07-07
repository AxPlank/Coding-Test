"""
백준 2004번: 조합 0의 개수
"""
import sys
from math import factorial, perm

n, m = map(int, sys.stdin.readline().strip().split())

def countNum(n, num):
    cnt = 0
    while n > 0:
        cnt += n // num
        n //= num
        
    return cnt

cnt_5 = countNum(n, 5) - countNum(m, 5) - countNum(n-m, 5)
cnt_2 = countNum(n, 2) - countNum(m, 2) - countNum(n-m, 2)

print(min(cnt_2, cnt_5))