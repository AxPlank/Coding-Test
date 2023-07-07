"""
백준 11650번: 좌표 정렬하기
"""
"""
Sol 1: sorted() 이용
"""
import sys

N = int(sys.stdin.readline())
coordinate_list = [0] * N

for i in range(N):
    coordinate_list[i] = tuple(map(int, sys.stdin.readline().strip().split()))

coordinate_list = sorted(coordinate_list)
for i in range(N):
    print(coordinate_list[i][0], coordinate_list[i][1])

"""
Sol 2: lambda func. 이용
"""
import sys

N = int(sys.stdin.readline())
coordinate_list = [0] * N

for i in range(N):
    coordinate_list[i] = tuple(map(int, sys.stdin.readline().strip().split()))
    
coordinate_list.sort(key=lambda x: (x[0], x[1]))
for i in range(N):
    print(coordinate_list[i][0], coordinate_list[i][1])

"""
Sol 3. 커스텀함수 이용
"""
from functools import cmp_to_key
import sys

def coordinate_sort(a, b):
    if a[0] > b[0]:
        return 1
    elif a[0] == b[0]:
        if a[1] > b[1]:
            return 1
        elif a[1] == b[1]:
            return 0
        else:
            return -1
    else:
        return -1
    
N = int(sys.stdin.readline())
coordinate_list = [0] * N

for i in range(N):
    coordinate_list[i] = tuple(map(int, sys.stdin.readline().strip().split()))
    
coordinate_list = sorted(coordinate_list, key=cmp_to_key(coordinate_sort))
for i in range(N):
    print(coordinate_list[i][0], coordinate_list[i][1])