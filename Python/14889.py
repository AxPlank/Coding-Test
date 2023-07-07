"""
백준 14889번: 스타트와 링크
"""
import sys
from itertools import combinations

sys.setrecursionlimit(200000) # 최대 재귀 횟수 수정

"""
능력치 차이 최솟값을 구하는 함수
"""
def dfs_soccer(diff, dep, star_stat, link_stat):
    if dep == N_combinations_len // 2:
        print(diff)
        return
    
    for i in N_combinations[dep]:
        for j in N_combinations[dep]:
            star_stat += S[i][j]
            
    for i in N_combinations[-(dep+1)]:
        for j in N_combinations[-(dep+1)]:
            link_stat += S[i][j]
                
    dfs_soccer(min(diff, abs(star_stat-link_stat)), dep+1, 0, 0)

N = int(sys.stdin.readline())
N_combinations = list(combinations([i for i in range(N)], N//2)) # 모든 경우의 수가 담길 리스트
S = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

N_combinations_len = len(N_combinations)

dfs_soccer(sys.maxsize, 0, 0, 0)