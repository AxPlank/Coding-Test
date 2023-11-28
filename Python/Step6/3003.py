import sys

chess = list(map(int, sys.stdin.readline().strip().split()))
origin = [1, 1, 2, 2, 2, 8]

for i in range(6):
    origin[i] = origin[i] - chess[i]
    
print(*origin)