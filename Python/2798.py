# Sol 1
import sys

N, M = map(int, sys.stdin.readline().strip().split())
number_list = list(map(int, sys.stdin.readline().strip().split()))
maxx = 0

for i in range(len(number_list)-2):
    for j in range(i+1, len(number_list)-1):
        for k in range(j+1, len(number_list)):
            if i == j or j == i or k == i:
                continue
            elif number_list[i] + number_list[j] + number_list[k] > 500:
                continue
            else:
                maxx = max(maxx, number_list[i] + number_list[j] + number_list[k])
                
print(maxx)

# Sol 2
import sys
import itertools

N, M = map(int, sys.stdin.readline().strip().split())
number_list = list(map(int, sys.stdin.readline().strip().split()))
number_combination = list(itertools.combinations(number_list, 3))
maxx = 0

for i in number_combination:
    if sum(i) > M:
        continue
    else:
        maxx = max(maxx, sum(i))
        
print(maxx)

"""
과정
1. 값을 입력받는다.
2. M보다 작으면서, M에 가까운 조합의 패들의 합을 구한다.
"""