"""
백준 3036번: 링
"""
import sys
from math import lcm

N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().strip().split())) # 입력되는 원들의 반지름을 담을 리스트

for i in range(1, N):
    LCM = lcm(numbers[0], numbers[i]) # 최소공배수
    print(f'{LCM//numbers[i]}/{LCM//numbers[0]}')