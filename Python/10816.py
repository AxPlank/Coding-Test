"""
백준 10816번: 숫자 카드 2
"""
import sys

N = int(sys.stdin.readline())
N_dict = dict()

# N개의 정수 입력
for i in list(map(int, sys.stdin.readline().strip().split())):
    try:
        N_dict[i] += 1
    except:
        N_dict[i] = 1
        
M = int(sys.stdin.readline())

# M개의 정수 입력 후, 입력한 정수들에 대해 상근이가 각각 몇 개 들고있는지 출력
for i in list(map(int, sys.stdin.readline().strip().split())):
    try:
        print(N_dict[i], end=' ')
    except:
        print(0, end=' ')