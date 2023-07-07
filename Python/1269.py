"""
백준 1269번: 대칭 차집합
"""
"""
Sol 1: 합집합과 교집합 이용
"""
import sys

numA, numB = map(int, sys.stdin.readline().strip().split())

A = set(map(int, sys.stdin.readline().strip().split()))
B = set(map(int, sys.stdin.readline().strip().split()))

union = A.union(B) #합집합
intersectionn = A.intersection(B) # 교집합
symmetric_diff = union.difference(intersectionn) # 대칭차집합
print(len(symmetric_diff))

"""
Sol 2: 합집합과 교집합 이용
"""
import sys

numA, numB = map(int, sys.stdin.readline().strip().split())

A = set(map(int, sys.stdin.readline().strip().split()))
B = set(map(int, sys.stdin.readline().strip().split()))

union = A.union(B)
intersectionn = A.intersection(B)
symmetric_diff = union - intersectionn
print(len(symmetric_diff))

"""
Sol 3: 차집합 이용
"""
import sys

numA, numB = map(int, sys.stdin.readline().strip().split())

A = set(map(int, sys.stdin.readline().strip().split()))
B = set(map(int, sys.stdin.readline().strip().split()))

diff_A = A.difference(B) # A-B
diff_B = B.difference(A) # B-A
symmetric_diff = diff_A.union(diff_B)
print(len(symmetric_diff))