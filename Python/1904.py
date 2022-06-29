"""
백준 1904번: 01타일
"""
import sys

N = int(sys.stdin.readline())
N_fibo = [0 for i in range(N)]

for i in range(N):
    if i == 0:
        N_fibo[i] = 1
    elif i == 1:
        N_fibo[i] = 2
    else:
        N_fibo[i] = (N_fibo[i-1] + N_fibo[i-2]) % 15746
    
print(N_fibo[-1])