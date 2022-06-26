"""
백준 2477번: 참외밭
"""
import sys

K = int(sys.stdin.readline())

direction = [0, 0, 0, 0, 0]
direc_leng = []
small_square = 0
big_square = 1

# 방위와 변의 길이 입력
for i in range(6):
    direc, leng = map(int, sys.stdin.readline().strip().split())
    direc_leng.append((direc, leng))
    direction[direc] += 1

# 큰 사각형의 넓이    
for i in range(6):
    if direction[direc_leng[i][0]] == 1:
        big_square *= direc_leng[i][1]
        
# 작은 사각형의 넓이
for i in range(6):
    if direc_leng[i-1][0] == direc_leng[i-3][0] and direc_leng[i][0] == direc_leng[i-2][0]:
        small_square = direc_leng[i-1][1] * direc_leng[i-2][1]
        break
    
print(K * (big_square - small_square))