import sys

def isprime(M, N):
    N += 1
    prime_list = [True] * N
    N_sqrt = int(N ** 0.5)
    for i in range(2, N_sqrt+1):
        if prime_list[i]:
            if i != 2 and i % 2 == 0:
                continue
            for j in range(2*i, N, i):
                if prime_list[j]:
                    prime_list[j] = False
    
    for i in range(M, N):
        if i > 1 and prime_list[i] == True:
            print(i)

M, N = map(int, sys.stdin.readline().strip().split())

isprime(M, N)

"""
실패
for i in range(M, N+1):
    if i == 1:
        continue
    for j in range(2, i):
        if i % j == 0:
            break
        elif j == i - 1:
            print(i)
"""

"""
과정
1. 상한값과 하한값을 입력한다.
2. 에라스토테네스의 체를 이용해 소수가 아닌 것들을 걸러낸다.
3. 소수인 것들(리스트의 값이 True인 것들)의 인덱스를 출력한다.
"""