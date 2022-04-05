import sys

T = int(sys.stdin.readline().strip())

for i in range(T):
    H, W, N = map(int, sys.stdin.readline().strip().split())
    floor = N % H
    number = N // H + 1
    if floor == 0:
        floor = H
        number -= 1
    print(floor * 100 + number)


"""
과정
1. 값을 입력한다.
2. 손님이 체크인하실 방 번호를 출력한다.
"""