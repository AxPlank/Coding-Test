# Sol 1
H, M = map(int,input().split())

if M - 45 < 0:
    M = (M - 45) + 60
    H -= 1
    if H < 0:
        H = 23
    print(H, M)
else:
    M -= 45
    print(H, M)

# Sol 2
H, M = map(int,input().split())

M -= 45

if M < 0:
    M += 60
    H -= 1
    if H < 0:
        H = 23
    print(H, M)
else:
    print(H, M)
    
# Sol 3
H, M = map(int,input().split())

if M > 44:
    print(H, M - 45)
elif M < 45 and H > 0:
    print(H - 1, M + 15)
else:
    print(23, M + 15)

"""
과정 및 함수 설명
함수

과정
1. 시간을 입력받는다.
2. 45분을 뺀 값을 출력한다.
"""