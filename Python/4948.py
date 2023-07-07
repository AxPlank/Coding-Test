import sys

def isprime(n, N):
    N += 1
    prime_list = [True] * N
    N_sqrt = int(N ** 0.5)
    for i in range(2, N_sqrt+1):
        if prime_list[i] == True:
            if i == 0 or i == 1:
                prime_list[i] = False
            for j in range(2*i, N, i):
                if prime_list[j]:
                    prime_list[j] = False
                    
    print(prime_list[n+1:].count(prime_list[2]))

while 1:
    n = int(sys.stdin.readline().strip())
    if n == 0:
        break
    N = n * 2 + 1
    isprime(n, N)

"""
과정
1. 상한값과 하한값을 입력한다.
2. 에라스토테네스의 체를 이용해 소수가 아닌 것들을 걸러낸다.
3. 소수인 것들(리스트의 값이 True인 것들)의 인덱스를 출력한다.
"""