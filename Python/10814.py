"""
백준 10814번: 나이순 정렬
"""
import sys
from functools import cmp_to_key

def age_sort(arr):
    def sortt(a, b):
        if a[0] > b[0]:
            return 1
        elif a[0] == b[0]:
            return 0
        else:
            return -1
        
    arr = sorted(arr, key=cmp_to_key(sortt))
    for i in range(len(arr)):
        print(arr[i][0], arr[i][1])
        
N = int(sys.stdin.readline())
member_list = [0] * N

for i in range(N):
    member_list[i] = list(sys.stdin.readline().strip().split())
    member_list[i][0] = int(member_list[i][0])
    
age_sort(member_list)