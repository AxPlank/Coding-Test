import sys

listt = []

for i in range(9):
    N = int(sys.stdin.readline().strip())
    listt.append(N)

print(max(listt))
print(listt.index(max(listt)) + 1)
    
"""
과정 및 함수 설명
함수

과정
1. 값을 입력받는다.
2. 최댓값을 출력한다.
"""