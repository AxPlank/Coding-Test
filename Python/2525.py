H, M = map(int,input().split())
T = int(input())

H += T // 60
M += T % 60

if M > 59:
    M -= 60
    H += 1

if H > 23:
    H -= 24
    
print(H, M)

"""
과정 및 함수 설명
함수

과정
1. 시간을 입력받는다.
2. 완료 예정 시간을 출력한다.
"""