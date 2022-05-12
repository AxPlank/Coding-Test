"""
백준 2981번: 검문
"""
import sys
from math import gcd

N = int(sys.stdin.readline()) # 입력할 수의 개수

nums = [] # 입력한 수를 저장할 리스트
for _ in range(N): # 입력값을 nums에 저장하는 반복문
    nums.append(int(sys.stdin.readline()))
    
nums.sort()
nums_interval = [] # 인접한 값 사이의 간격을 저장할 리스트
for i in range(N-1):
    nums_interval.append(abs(nums[i]-nums[i+1]))
    
GCD = 0 # 간격들의 최대공약수
print(nums_interval)
for i in range(N-1):
    print(GCD == gcd(nums_interval[0], nums_interval[i]))
    GCD = gcd(nums_interval[0], nums_interval[i])
    


