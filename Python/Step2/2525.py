H, M = map(int,input().split())
T = int(input())

# Sol 1
H += T // 60
M += T % 60

if M > 59:
    M -= 60
    H += 1

if H > 23:
    H -= 24
    
print(H, M)

# Sol 2
T += M
H = H + T // 60 - 24 if H + T // 60 > 23 else H + T // 60
M = T % 60

print(H, M)

"""
과정 및 함수 설명
함수

과정
1. 시간을 입력받는다.
2. 완료 예정 시간을 출력한다.
"""