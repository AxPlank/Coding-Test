import sys

N = int(sys.stdin.readline())
divisor_list = list(map(int, sys.stdin.readline().strip().split()))
divisor_max = max(divisor_list)
divisor_list_len = len(divisor_list)

for i in range(2, 1000001):
    cnt = 0
    if i > divisor_max:
        for j in divisor_list:
            if i % j == 0:
                cnt += 1
            else:
                break
    
    if cnt == divisor_list_len:
        print(i)
        break