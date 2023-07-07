"""
백준 2609번: 최대공약수와 최소공배수
"""
"""
풀이 1: 유클리드 호제법 이용
"""
import sys

"""
최대공약수를 구하는 함수
"""
def getGCD(a, b):
    while b > 0:
        a, b = b, a % b
    return a
    
A, B = map(int, sys.stdin.readline().strip().split())

GCD = getGCD(max(A, B), min(A, B)) # 최대공약수
LCM = (A * B) // GCD # 최소공배수
print(GCD)
print(LCM)

"""
풀이 2: math 라이브러리 이용
"""
from math import gcd, lcm
import sys

A, B = map(int, sys.stdin.readline().strip().split())

GCD = gcd(A, B)
LCM = lcm(A, B)

print(GCD)
print(LCM)

"""
풀이 3: 소인수분해 이용
"""
import sys

"""
소인수분해 함수
"""
def factorizationn(n):
    factor_list = [0] * (max(n1, n2) + 1) # 소인수분해를 시도할 때, 각 소수의 지수를 담을 리스트
    i = 2
    while n > 2 and i <= n:
        if n % i == 0:
            factor_list[i] += 1
            n = n / i
        else:
            i += 1
    
    return factor_list

n1, n2 = map(int, sys.stdin.readline().strip().split())

arr1 = factorizationn(n1)
arr2 = factorizationn(n2)

"""
최대공약수, 최소공배수 출력
"""
GCD = 1
LCM = 1
for i in range(2, max(n1, n2)+1):
    GCD *= i ** min(arr1[i], arr2[i])
    LCM *= i ** max(arr1[i], arr2[i])
    
print(GCD)
print(LCM)