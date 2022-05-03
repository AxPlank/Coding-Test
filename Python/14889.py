"""
백준 14889번: 스타트와 링크
"""
import sys
from itertools import combinations

N = int(sys.stdin.readline())
N_combinations = list(combinations([i for i in range(N)], N//2))
S = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

diff = sys.maxsize

for i in range(len(N_combinations)):
    star_stat = 0
    link_stat = 0
    for j in range(N):
        for k in range(N):
            if j in N_combinations[i] and k in N_combinations[i]:
                star_stat += S[j][k]
            if j not in N_combinations[i] and k not in N_combinations[i]:
                link_stat += S[j][k]
            
    diff = min(diff, abs(star_stat-link_stat))
    
print(diff)