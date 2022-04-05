import sys

def solvee(n):
    if n < 100:
        return 1
    else:
        str_n = str(n)
        interval = int(str_n[0]) - int(str_n[1])
        for i in range(len(str_n)-1):
            if int(str_n[i]) - int(str_n[i+1]) == interval:
                continue
            else:
                return 0
        return 1

N = int(sys.stdin.readline().strip())
cnt = 0

for i in range(1, N+1):
    cnt += solvee(i)
    
print(cnt)       

"""
과정 및 함수 설명
함수

과정
1. 수를 입력받는다.
2. 반복문을 이용해서, 범위 내의 각 수가 한수의 조건을 만족하는지 확인한다.
3. 범위 안 한수의 개수를 출력한다.
"""