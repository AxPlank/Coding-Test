import sys
from collections import Counter
import statistics

N = int(sys.stdin.readline())

num_list = []
for i in range(N):
    num = int(sys.stdin.readline())
    num_list.append(num)

# 평균
print(round(statistics.mean(num_list)))

# 중앙값
print(statistics.median(num_list))

# 최빈값
cnt_list = Counter(sorted(num_list)).most_common(2) # 정렬을 먼저 하고 해야 함

if len(cnt_list) == 1:
    print(cnt_list[0][0])
else:
    if cnt_list[0][1] == cnt_list[1][1]:
        print(cnt_list[1][0])
    else:
        print(cnt_list[0][0])
        
# 범위
print(max(num_list) - min(num_list))