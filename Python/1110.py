import sys

N = int(sys.stdin.readline().strip())
temp = N
cnt = 0

while True:
    cnt += 1
    temp_10 = temp // 10
    temp_1 = temp % 10
    temp_sum_1 = (temp_10 + temp_1) % 10
    temp = temp_1 * 10 + temp_sum_1
    
    if temp == N:
        print(cnt)
        break
        
    
"""
과정 및 함수 설명
함수

과정
1. 값을 입력받는다.
2. 주어진 연산을 반복해서 수행한다.
3. 원래 숫자로 돌아오면 연산을 반복한 횟수를 출력한다.
"""