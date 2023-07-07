import sys

N = int(sys.stdin.readline().strip())
sugar_pack = 0

while N >= 0:
    if N % 5 == 0:
        sugar_pack += N // 5
        print(sugar_pack)
        break
    sugar_pack += 1
    N -= 3
    if N < 0:
        print(-1)

"""
과정
1. 설탕의 양을 입력한다.
2. 설탕봉지 몇 개가 필요한지 출력한다.
"""