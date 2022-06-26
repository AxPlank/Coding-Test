"""
백준 1620번: 나는야 포켓몬 마스터 이다솜
"""
import sys

N, M = map(int, sys.stdin.readline().strip().split())
pocketmon_dict = {}

for i in range(N):
    pocketmon = sys.stdin.readline().strip()
    pocketmon_dict[pocketmon] = i
    
keyss = list(pocketmon_dict.keys())
    
for i in range(M):
    check = sys.stdin.readline().strip()
    
    try:
        check = int(check)
        print(keyss[check-1])
    except:
        print(pocketmon_dict[check] + 1)