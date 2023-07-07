"""
백준 10815번: 숫자 카드
"""
import sys

N = int(sys.stdin.readline())
N_list = sorted(list(map(int, sys.stdin.readline().strip().split())))
M = int(sys.stdin.readline())
M_list = list(map(int, sys.stdin.readline().strip().split()))

def binarySearch(check):
    start = 0
    end = N - 1
    while start <= end:
        mid = (start + end) // 2
        
        if N_list[mid] == check:
            return print(1, end=' ')
        elif N_list[mid] < check:
            start = mid + 1
        elif N_list[mid] > check:
            end = mid - 1
    return print(0, end=' ')

for i in M_list:
    binarySearch(i)