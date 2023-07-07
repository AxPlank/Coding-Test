import sys
import time

def fibo_dynamic(n):
    
    if n == 1:
        return 1
    if n == 2:
        return 2
    if fibo_arr[n] != 0:
        return fibo_arr[n]
    
    fibo_arr[n] = fibo_dynamic(n-2) + fibo_dynamic(n-1)
    return fibo_arr[n]

N = int(sys.stdin.readline())
sys.setrecursionlimit(2**31-1)
fibo_arr = [0 for i in range(N+1)]
fibo_dynamic(N)
print(fibo_arr[-1] % 15746)