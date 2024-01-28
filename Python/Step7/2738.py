import sys

N, M = map(int, sys.stdin.readline().rstrip().split(" "))

ret = [[0 for j in range(M)] for i in range(N)]

for i in range(2):
    for j in range(N):
        ipt = list(map(int, sys.stdin.readline().rstrip().split(" ")))
        
        for k in range(M):
            ret[j][k] += ipt[k]
            
for i in range(N):
    print(" ".join(map(str, ret[i])))