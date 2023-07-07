# Sol 1
n = int(input())
summ = 0

for i in range(1, n+1):
    summ += i
    
print(summ)

# Sol 2
def summ(n):
    if n == 1:
        return 1
    else:
        return n + summ(n-1)
    
n = int(input())
    
print(summ(n))

# Sol 3
n = int(input())

print(sum(range(1, n+1)))

"""
과정 및 함수 설명
함수

과정
1. 값을 입력받는다.
2. 솔루션을 이용해 합을 출력한다.
"""