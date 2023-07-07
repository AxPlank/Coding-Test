"""
백준 1764번: 듣보잡
"""
"""
Sol 1
"""
import sys

N, M = map(int, sys.stdin.readline().strip().split())

set_N = set()
for _ in range(N):
    set_N.add(sys.stdin.readline().strip())
    
set_M = set()
for _ in range(M):
    set_M.add(sys.stdin.readline().strip())
    
NM = sorted(set_N & set_M)
print(len(NM))
for i in NM:
    print(i)
    
"""
Sol 2
"""
import sys

N, M = map(int, sys.stdin.readline().strip().split())

set_N = set()
for _ in range(N):
    set_N.add(sys.stdin.readline().strip())
    
set_M = set()
for _ in range(M):
    set_M.add(sys.stdin.readline().strip())
    
NM = sorted(set_N.intersection(set_M))
print(len(NM))
for i in NM:
    print(i)    
