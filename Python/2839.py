import sys
import math

T = int(sys.stdin.readline().strip())

for i in range(T):
    k = int(sys.stdin.readline().strip()) # 층수
    n = int(sys.stdin.readline().strip()) # 호수
    
    r_fac = math.factorial(k+1) # r!값
    n_r_fac = math.factorial(k+n-(k+1)) # (n-r)!값
    n_fac = math.factorial(k+n) # n!값
    print(int(n_fac/r_fac/n_r_fac)) # 조합 계산하여 출력


"""
과정
1. 방 호수를 입력한다.
2. 본인 포함 총 가족 수를 출력한다.
"""