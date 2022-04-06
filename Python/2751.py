"""
Sol 1. 병합 정렬
"""
import sys

N = int(sys.stdin.readline().strip())
num_list = []

for i in range(N):
    num = int(sys.stdin.readline().strip())
    num_list.append(num)
    
def mergesort(num_list):
    if len(num_list) == 1:
        return num_list
    
    mid = len(num_list) // 2
    left_num_list = mergesort(num_list[:mid])
    right_num_list = mergesort(num_list[mid:])
    merge_num_list = []
    l = 0
    r = 0
    while l < len(left_num_list) and r < len(right_num_list):
        if left_num_list[l] > right_num_list[r]:
            merge_num_list.append(right_num_list[r])
            r += 1
        else:
            merge_num_list.append(left_num_list[l])
            l += 1
    if l == len(left_num_list):
        merge_num_list += right_num_list[r:]
        return merge_num_list
    if r == len(right_num_list):
        merge_num_list += left_num_list[l:]
        return merge_num_list
    
for i in mergesort(num_list):
    print(i)

"""
Sol 2. 힙 정렬
"""

import sys

N = int(sys.stdin.readline().strip())
num_list = []

def heapsort(arr):
    for i in range(N):
        num = int(sys.stdin.readline().strip())
        num_list.append(num)

    for i in range(len(num_list)):
        d = i
        while d != 0:
            u = (d-1) // 2

            if num_list[u] < num_list[d]:
                num_list[u], num_list[d] = num_list[d], num_list[u]
            else:
                break
            d = u


    for i in range(len(num_list)-1, -1, -1):
        num_list[0], num_list[i] = num_list[i], num_list[0]
        u = d = 0   
        while d < i:
            d = 2 * u + 1
            if d < i - 1 and num_list[d] < num_list[d+1]:
                d += 1

            if d < i and num_list[u] < num_list[d]:
                num_list[u], num_list[d] = num_list[d], num_list[u]
            else:
                break
                
            u = d

heapsort(num_list)
for i in num_list:
    print(i)