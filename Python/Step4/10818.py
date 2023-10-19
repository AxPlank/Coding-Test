import sys

N = int(sys.stdin.readline().strip())
N_list = list(map(int, sys.stdin.readline().strip().split()))

print(min(N_list), max(N_list))
    
"""
과정 및 함수 설명
함수

과정
1. 값을 입력받는다.
2. 최댓값과 최솟값을 출력한다.
"""