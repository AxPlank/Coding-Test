"""
백준 2981번: 검문
"""
import sys
from math import gcd, sqrt

N = int(sys.stdin.readline())
numbers = [int(sys.stdin.readline()) for _ in range(N)]

nums_interval = [] # 인접한 입력값들의 차이의 절댓값을 저장할 리스트
for i in range(1, N):
    nums_interval.append(abs(numbers[i]-numbers[i-1]))
    
nums_interval = sorted(list(set(nums_interval))) # 중복 제거 및 오름차순으로 정렬
GCD = 0 # 공차를 넣을 변수
if len(nums_interval) == 1:
    GCD = nums_interval[0]
else:
    GCD = gcd(nums_interval[0], nums_interval[1])

M = set() # 가능한 공차들을 넣을 집합
M.add(GCD)
for i in range(2, int(sqrt(GCD))+1):
    if GCD % i == 0:
        M.add(i)
        M.add(GCD//i)
        
nums_str = list(map(str, sorted(M)))
print(' '.join(nums_str))