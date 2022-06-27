"""
백준 10816번: 숫자 카드 2
"""
import sys

N = int(sys.stdin.readline())
N_dict = dict()

for i in list(map(int, sys.stdin.readline().strip().split())):
    try:
        N_dict[i] += 1
    except:
        N_dict[i] = 1
        
M = int(sys.stdin.readline())
        
for i in list(map(int, sys.stdin.readline().strip().split())):
    try:
        print(N_dict[i], end=' ')
    except:
        print(0, end=' ')