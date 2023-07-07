"""
백준 1676번: 팩토리얼 0의 개수
"""
"""
Sol 1: 팩토리얼 이용
"""
import sys
from math import factorial

N = str(factorial(int(sys.stdin.readline())))
cnt = 0

for i in range(len(N)-1, -1, -1):
    if N[i] == '0':
        cnt += 1
    else:
        print(cnt)
        break

"""
Sol 2: 2004번 응용 1
"""
import sys

def countNum(n, num):
    cnt = 0
    while n > 0:
        cnt += n // num
        n //= num
        
    return cnt

N = int(sys.stdin.readline())

print(min(countNum(N, 5), countNum(N, 2)))

"""
Sol 3: 2004번 응용 2
"""
import sys
from math import factorial

N = factorial(int(sys.stdin.readline()))
cnt = 0

while N % 10 == 0:
    cnt += 1
    N //= 10

print(cnt)