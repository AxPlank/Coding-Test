import sys

M = int(sys.stdin.readline().strip())
N = int(sys.stdin.readline().strip())

summ = sum(range(M, N+1, 1))
N_list = [int(i) for i in range(M, N+1)]
for i in range(M, N+1):
    if i == 1:
        summ -= 1
        N_list.remove(1)
    for j in range(2, i):
        if i % j == 0:
            summ -= i
            N_list.remove(i)
            break
        
if summ == 0:
    print(-1)
else:
    print(summ)
    print(min(N_list))

"""
과정
1. 상한값과 하한값을 입력한다.
2. 해당 값들이 소수인지 파악한다.
3. 소수인 값이 몇 개인지 출력한다.
"""