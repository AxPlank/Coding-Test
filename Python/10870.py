import sys

def def_fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return def_fibo(n-1) + def_fibo(n-2)

n = int(sys.stdin.readline().strip())

print(def_fibo(n))

"""
과정
1. 값을 입력받는다.
2. 입력값에 대한 피보나치 수열을 출력한다.
"""