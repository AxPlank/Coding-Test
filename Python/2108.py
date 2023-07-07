"""
Sol 1: Counter 이용
"""
import sys
from collections import Counter
import statistics

N = int(sys.stdin.readline())

num_list = [0] * N
for i in range(N):
    num_list[i] = int(sys.stdin.readline())

# 평균
print(round(statistics.mean(num_list)))

# 중앙값
print(statistics.median(num_list))

# 최빈값
cnt_list = Counter(sorted(num_list)).most_common(2) # 정렬을 먼저 하고 해야 함

if len(cnt_list) == 1: # 단일 수로만 이뤄졌을 경우
    print(cnt_list[0][0])
else:
    if cnt_list[0][1] == cnt_list[1][1]: # 최빈값이 2개 이상
        print(cnt_list[1][0])
    else: #최빈값이 1개
        print(cnt_list[0][0])
        
# 범위
print(max(num_list) - min(num_list))

"""
Sol 2: 딕셔너리 이용
"""
import sys
import statistics

N = int(sys.stdin.readline())
num_cnt = {}
num_list = [0] * N
for i in range(N):
    num_list[i] = int(sys.stdin.readline())
    if num_list[i] not in num_cnt.keys():
        num_cnt[num_list[i]] = 1
    else:
        num_cnt[num_list[i]] += 1

# 평균
print(round(statistics.mean(num_list)))

# 중앙값
print(statistics.median(num_list))

# 최빈값
def modee(dictt):
    cnt = 0
    maxx = max(dictt.values())
    key_list = list(dictt.keys())
    for i in sorted(key_list):
        if dictt[i] == maxx:
            cnt += 1
        if cnt == 2: # 최빈값이 2개 이상
            print(i)
            break
        if i == max(dictt.keys()): # 최빈값이 1개
            idx = list(dictt.values()).index(maxx)
            print(key_list[idx])
            
modee(num_cnt)

# 범위
print(max(num_list) - min(num_list))