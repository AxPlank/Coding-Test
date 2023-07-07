"""
백준 24416: 알고리즘 수업 - 피보나치 수 1
"""
import sys

n = int(sys.stdin.readline())
cnt_recursion = 0
cnt_dynamic = 0

# 일반적인 재귀 함수
def fibo_recursion(n):
    global cnt_recursion
    
    if n == 1 or n == 2:
        cnt_recursion += 1
        return 1
    
    return fibo_recursion(n-1) + fibo_recursion(n-2)

# 동적 프로그래밍
fibo_arr = [0 for i in range(n+1)]
def fibo_dynamic(n):
    global cnt_dynamic
    
    if n == 1 or n == 2:
        return 1
    if fibo_arr[n] != 0:
        return fibo_arr[n]
    
    cnt_dynamic += 1
    fibo_arr[n] = fibo_dynamic(n-2) + fibo_dynamic(n-1)
    print(f'{n} {fibo_arr[n]} {cnt_dynamic}')
    return fibo_arr[n]

fibo_recursion(n)
fibo_dynamic(n)
print(f'{cnt_recursion} {cnt_dynamic}')