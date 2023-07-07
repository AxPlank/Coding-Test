import sys

N = int(sys.stdin.readline().strip())
N_list = list(map(int, sys.stdin.readline().strip().split()))
cnt = 0

for i in N_list:
    if i == 1:
        cnt += 1
    for j in range(2, i):
        if i % j == 0:
            cnt += 1
            break
        
print(N-cnt)

"""
과정
1. 값들을 입력한다.
2. 해당 값들이 소수인지 파악한다.
3. 소수인 값이 몇 개인지 출력한다.
"""