import sys

N, M = map(int, list(sys.stdin.readline().rstrip().split(" ")))
Box = [0 for _ in range(N)]

for m in range(M):
    i, j, k = map(int, list(sys.stdin.readline().rstrip().split(" ")))
    if i == j:
        Box[i-1] = k
    else:
        Box[i-1:j] = [k for _ in range(i-1, j)]
             
print(" ".join(map(str, Box)))