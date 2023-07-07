"""
백준 1037번: 약수
"""

import sys

N = int(sys.stdin.readline())
divisors = list(map(int, sys.stdin.readline().strip().split()))

"""
찾는 수 출력
"""
print(min(divisors) * max(divisors))