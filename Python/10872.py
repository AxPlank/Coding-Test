import sys

def def_factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * def_factorial(n-1)

n = int(sys.stdin.readline().strip())

print(def_factorial(n))

"""
과정
1. 값을 입력받는다.
2. 함수를 이용해 팩토리얼을 구해서 출력한다.
"""