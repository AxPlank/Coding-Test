import sys

N = sys.stdin.readline().strip()
N_int = int(N)

if N_int <= 20:
    for i in range(N_int):
        N_i = sum(map(int, list(str(i)))) + i
        if N_i == N_int:
            print(i)
            break
        if i == N_int - 1:
            print(0)
else:
    start_num = N_int - len(N) * 9
    for i in range(start_num, N_int):
        N_i = sum(map(int, list(str(i)))) + i
        if N_i == N_int:
            print(i)
            break
        if i == N_int - 1:
            print(0)

"""
과정
1. 값을 입력받는다.
2. 분해합을 구해 출력한다. 없다면 0을 출력한다.
"""