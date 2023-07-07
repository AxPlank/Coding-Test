"""
백준 11050번: 이항 계수 1
"""
"""
풀이 1: math.comb() 이용
"""
import sys
from math import comb

N, K = map(int, sys.stdin.readline().strip().split())
print(comb(N, K))

"""
풀이 2: 팩토리얼 이용
"""
import sys
from math import factorial

N, K = map(int, sys.stdin.readline().strip().split())
print(factorial(N)//factorial(N-K)//factorial(K))