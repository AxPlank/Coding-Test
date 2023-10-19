"""
백준 10811번: 바구니 뒤집기
"""
# Sol 1
import sys

N, M = map(int, sys.stdin.readline().rstrip().split(" "))
Boxes = [str(i+1) for i in range(N)]

for _ in range(M):
    i, j = map(int, sys.stdin.readline().rstrip().split(" "))
    temp = Boxes[i-1:j]
    temp.reverse()
    Boxes[i-1:j] = temp
    
print(" ".join(Boxes))
    