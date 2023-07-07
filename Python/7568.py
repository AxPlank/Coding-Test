import sys

N = int(sys.stdin.readline().strip())
stat_list = []
rank_list = []

for _ in range(N):
    stat = tuple(map(int, sys.stdin.readline().strip().split()))
    stat_list.append(stat)
    
for i in range(N):
    rank = 1
    for j in range(N):
        if i == j:
            continue
        if stat_list[i][0] < stat_list[j][0] and stat_list[i][1] < stat_list[j][1]:
            rank += 1
    rank_list.append(rank)
    
for i in range(N):
    print(rank_list[i], end=' ')
        
        

"""
과정
1. 값을 입력받는다.
2. 순위를 정한다.
3. 순위를 출력한다.
"""