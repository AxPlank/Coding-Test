"""
백준 14889번: 스타트와 링크
"""
import sys
from itertools import combinations

sys.setrecursionlimit(200000)

def dfs_soccer(diff, dep, lenn, star_stat, link_stat):
    if dep == lenn:
        print(diff)
        return
    
    star_team = []
    link_team = []
    
    for i in range(N):
        if i in N_combinations[dep]:
            star_team.append(i)
        else:
            link_team.append(i)
    
    for i in star_team:
        for j in star_team:
            star_stat += S[i][j]
            
    for i in link_team:
        for j in link_team:
            link_stat += S[i][j]
                
    dfs_soccer(min(diff, abs(star_stat-link_stat)), dep+1, lenn, 0, 0)

N = int(sys.stdin.readline())
N_combinations = list(combinations([i for i in range(N)], N//2))
S = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

N_combinations_len = len(N_combinations)

dfs_soccer(sys.maxsize, 0, N_combinations_len, 0, 0)