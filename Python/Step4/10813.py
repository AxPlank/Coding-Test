import sys

N, M = map(int, list(sys.stdin.readline().rstrip().split(" ")))
Box = [i+1 for i in range(N)]

for _ in range(M):
    i, j = map(int, list(sys.stdin.readline().rstrip().split(" ")))
    
    if i != j:
        Box[i-1], Box[j-1] = Box[j-1], Box[i-1]
             
print(" ".join(map(str, Box)))