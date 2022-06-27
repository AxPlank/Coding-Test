"""
백준 14425번: 문자열 집합
"""
"""
Sol 1
"""
import sys

def binarySearch(check):
    start = 0
    end = N - 1
    while start <= end:
        mid = (start + end) // 2
        
        if S[mid] == check:
            return 1
        elif S[mid] < check:
            start = mid + 1
        elif S[mid] > check:
            end = mid - 1
    return 0

N, M = map(int, sys.stdin.readline().strip().split())
S = []
M_list = []
cnt = 0

for _ in range(N):
    S.append(sys.stdin.readline().strip())

S = sorted(S)

for _ in range(M):
    M_list.append(sys.stdin.readline().strip())

for i in M_list:
    cnt += binarySearch(i)
    
print(cnt)

"""
Sol 2
"""
import sys

def binarySearch(check):
    start = 0
    end = N - 1
    while start <= end:
        mid = (start + end) // 2
        
        if S[mid] == check:
            return 1
        elif S[mid] < check:
            start = mid + 1
        elif S[mid] > check:
            end = mid - 1
    return 0

N, M = map(int, sys.stdin.readline().strip().split())
S = []
cnt = 0

for _ in range(N):
    S.append(sys.stdin.readline().strip())

S = sorted(S)

for _ in range(M):
    cnt += binarySearch(sys.stdin.readline().strip())
    
print(cnt)