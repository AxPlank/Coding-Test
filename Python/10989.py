import sys

N = int(sys.stdin.readline())
num_input = [0] * 10000

for _ in range(N):
    num = int(sys.stdin.readline())
    num_input[num-1] += 1

for i in range(10000):
    if num_input[i] != 0:
        for _ in range(num_input[i]):
            print(i)