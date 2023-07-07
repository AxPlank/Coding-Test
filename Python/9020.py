# Sol 1
import sys

def isprime(n):
    n += 1
    prime_list = [1] * n
    n_sqrt = int(n ** 0.5)
    for i in range(n_sqrt+1):
        if i == 0 or i == 1:
            prime_list[i] == 0
            continue
        if prime_list[i] == 1:
            for j in range(2*i, n, i):
                if prime_list[j] == 1:
                    prime_list[j] = 0
    
    return prime_list

T = int(sys.stdin.readline().strip())

for i in range(T):
    n = int(sys.stdin.readline().strip())
    listt = isprime(n)
    A = n // 2
    while A > 1:
        if listt[A] == 1 and listt[n-A] == 1:
            if A > n - A:
                print(n - A, A)
                break
            else:
                print(A, n - A)
                break
        else:
            A -= 1

# Sol 2
import sys

def isprime(n):
    n += 1
    prime_list = [1] * n
    n_sqrt = int(n ** 0.5)
    for i in range(n_sqrt+1):
        if i == 0 or i == 1:
            prime_list[i] == 0
            continue
        if prime_list[i] == 1:
            for j in range(2*i, n, i):
                if prime_list[j] == 1:
                    prime_list[j] = 0
    
    return prime_list

T = int(sys.stdin.readline().strip())

for i in range(T):
    n = int(sys.stdin.readline().strip())
    listt = isprime(n)
    A = n // 2
    for i in range(A, 1, -1):
        if listt[i] == 1 and listt[n-i] == 1:
            if i > n - i:
                print(n - i, i)
                break
            else:
                print(i, n - i)
                break

# Sol 3
import sys

def isprime(n):
    n += 1
    prime_list = [1] * n
    n_sqrt = int(n ** 0.5)
    for i in range(n_sqrt+1):
        if i == 0 or i == 1:
            prime_list[i] == 0
            continue
        if prime_list[i] == 1:
            for j in range(2*i, n, i):
                if prime_list[j] == 1:
                    prime_list[j] == 0
    
    return prime_list

T = int(sys.stdin.readline().strip())

for i in range(T):
    n = int(sys.stdin.readline().strip())
    listt = isprime(n)
    A = n // 2
    for i in range(2, A+1):
        if listt[i] == 1 and listt[n-i] == 1:
            if A > n - i:
                print(n - i, i)
                break
            else:
                print(i, n - i)
                break

"""
과정
1. 값을 입력한다.
2. 에라토스테네스의 체를 이용하여 범위 내의 모든 값의 소수 여부를 판단한다.
3. 범위의 중간값에 제일 가까우며, 최댓값에 대한 골드바흐의 추측을 만족시키는 소수의 조합을 출력한다.
"""